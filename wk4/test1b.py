import numpy as np
import pandas as pd

from bokeh.io import output_notebook, show
from bokeh.charts import *
output_notebook()

from nose.tools import *


def get_sample_mean_distribution(data, n, m=1000, seed=543210):
    # YOUR CODE HERE
    # 1) given data... data = pd.Series([5, 5, 5, 5, 5, 4, 5, 4, 5, 4, 5, 5, 3, 4, 4, 5, 5, 5, 4, 5, 5, 5, 5, 4, 2, 4, 5, 5, 4, 5])
    # 2) given n :  20. 
    # 3) given m: 1000
    # 4) 
    
    resultList = []
    for i in range(0, m):
#         print('seed::', seed)
        low = data.min()
        high = data.max()+1
#         print('low:',low, ' // high:',high)
        
        # 4) init RandomState
        rs = np.random.RandomState(seed)
        randList = rs.randint( low, high, size = 20)
#         print('randList::', randList)
        sampleMean = pd.Series(randList).mean()
#         sampleMean = pd.Series(data).mean()
        resultList.append(sampleMean) 
#     print('resultList::', resultList)
    resultSeries = pd.Series(resultList)
 
    return resultSeries
    raise NotImplementedError()

def quiz1c():
    # You don't need to write anything here
    m = 1000
    n = 20
    data = pd.Series([5, 5, 5, 5, 5, 4, 5, 4, 5, 4, 5, 5, 3, 4, 4, 5, 5, 5, 4, 5, 5, 5, 5, 4, 2, 4, 5, 5, 4, 5])
    seed = 123456
    actual_output = get_sample_mean_distribution(data, n, m, seed)

    assert_equal(len(actual_output), 1000)
    assert_equal(round(actual_output.sum(),4), 4528.6)

    # Check randomness is working:
    # The same seed should lead to the same result
    seed_test_equal = get_sample_mean_distribution(data, n, m, seed)
    assert_equal(actual_output.mean(), seed_test_equal.mean())

    # A different seed should not be equal
    seed_test_not_equal = get_sample_mean_distribution(data, n, m, 54321)
    assert_not_equal(actual_output.mean(), seed_test_not_equal.mean())

    print('All tests successfully passed')


m = 1000
n = 20
data = pd.Series([5, 5, 5, 5, 5, 4, 5, 4, 5, 4, 5, 5, 3, 4, 4, 5, 5, 5, 4, 5, 5, 5, 5, 4, 2, 4, 5, 5, 4, 5])
seed = 123456

print('data.mean()::', data.mean(), ' ==? ', 4.5286)
print(round(get_sample_mean_distribution(data, n, m, seed).sum(),4), ' ==? ', 4528.6 )

# quiz1c()





