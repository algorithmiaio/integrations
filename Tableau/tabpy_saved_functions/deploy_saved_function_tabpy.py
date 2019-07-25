import Algorithmia
import tabpy_client

ALGORITHMIA_API_KEY = 'YOUR_API_KEY' #algorithmia.com/user#credentials
TABPY_SERVER_URL = 'http://localhost:9004/'
DEBUG = True


def algorithmia(algorithm_name, input):
    if DEBUG: print("algorithm: %sinput: %s\n"%(algorithm_name,input))
    try:
        client = Algorithmia.client(ALGORITHMIA_API_KEY)
        algo = client.algo(algorithm_name)
        result = algo.pipe(input).result
    except Exception as x:
        if DEBUG: print(x)
        raise Exception(str(x))
    if DEBUG: print("result: %s"%result)
    return result


tabpy_conn = tabpy_client.Client(TABPY_SERVER_URL)
tabpy_conn.deploy('algorithmia', algorithmia, 'Run a function on Algorithmia: algorithmia(algorithm_name, input)', override=True)