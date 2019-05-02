# Algorithmia + Tableau 

This code is experimental. Stay tuned for more from Tableau and Algorithmia.

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

See [Algorithmia's List of Integrations](https://algorithmia.com/developers/integrations) for more information.
