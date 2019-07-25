# TabPy Saved Functions

Instead of embedding your entire Algorithmia call into your Tableau
worksheet, you can create a wrapper function and save it inside your
TabPy instance. This both simplifies the code inside your Tableau
worksheet, and allows you to hide your Algorithmia API Key so that it is
not saved within the worksheet itself.

First, modify and run the code in
[deploy_saved_function_tabpy.py](deploy_saved_function_tabpy.py) -- this
injects the wrapper code into your running TabPy instance.

Then, modify the code in your Tableau worksheet so that it calls the
wrapper function, e.g.:


```
SCRIPT_REAL(
"
algoname = 'TimeSeries/SimpleMovingAverage/0.2.0'
input = [_arg1,3]
return tabpy.query('algorithmia',algoname,input)['response']
",
ATTR([admitted])
)
```

```
SCRIPT_STR(
"
algoname = 'demo/Hello/0.1.0'
results = list()
for input in _arg1:
    result = tabpy.query('algorithmia',algoname,input)['response']
    results.append(result)
return results
",
ATTR([admitted])
)
```
