# I-ll_think_about_it_later

## Unscript 2022 - Hackathon

Unscript-Rookies-Hackathon-2k22
Team Members - Kunal Wagh
               Yash Wakekar
               gamingflexer
               Adwait Gawade

## use model

```python
import pickle
loaded_model = pickle.load(open('path of model', 'rb'))
r=loaded_model.predict(test_array)
print(r)
```


## features 

```
['step', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest',
 'newbalanceDest', 'errorBalanceOrg', 'errorBalanceDest', 'HourOfDay']
      
