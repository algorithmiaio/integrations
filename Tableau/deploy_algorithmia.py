ALGORITHMIA_API_KEY = 'YOUR_API_KEY'
TABPY_SERVER_URL = 'http://localhost:9004/'
DEBUG = True

import Algorithmia
import tabpy_client

tabpy_conn = tabpy_client.Client(TABPY_SERVER_URL)
global algorithmia_client
algorithmia_client = None

def get_client():
    global algorithmia_client
    if algorithmia_client is None:
        algorithmia_client = Algorithmia.client(ALGORITHMIA_API_KEY)
    return algorithmia_client


def raise_exception(error):
    print("Error: %s" % error)
    x = Exception(str(error))
    x.message = str(error) #legacy
    raise x

def print_debug(message):
    if DEBUG:
        print(message)

# EXAMPLE CALL FROM TABLEAU:
# SCRIPT_REAL(
#   "return tabpy.query('algorithmia',_arg1,[_arg2,3])['response']",
#   "TimeSeries/SimpleMovingAverage/0.2.0",
#   ATTR([timeseries_data])
# )
def algorithmia(algorithm_name, input):
    if isinstance(algorithm_name, list):
        algorithm_name = algorithm_name[0]
    print_debug("algorithm_name: %s"%algorithm_name)
    print_debug("input: %s"%input)
    try:
        algo = get_client().algo(algorithm_name)
        result = algo.pipe(input).result
    except Exception as x:
        raise_exception(x)
    print_debug("result: %s"%result)
    return result

# EXAMPLE CALL FROM TABLEAU:
# SCRIPT_STR(
#   "return tabpy.query('algorithmia_each',_arg1,_arg2)['response']",
#   "demo/Hello",
#   ATTR([singular_data])
# )
def algorithmia_each(algorithm_name, input):
    if isinstance(algorithm_name, list):
        algorithm_name = algorithm_name[0]
    print_debug("algorithm_name: %s"%algorithm_name)
    print_debug("input: %s"%input)
    results = list()
    try:
        algo = get_client().algo(algorithm_name)
        for input_single in input:
            results.append(algo.pipe(input_single).result)
    except Exception as x:
        raise_exception(x)
    print_debug("results: %s"%results)
    return results


tabpy_conn.deploy('algorithmia', algorithmia, 'Run a function on Algorithmia: algorithmia(algorithm_name, input)', override=True)
tabpy_conn.deploy('algorithmia_each', algorithmia_each, 'Run a function on Algorithmia once for each input: algorithmia(algorithm_name, input[])', override=True)