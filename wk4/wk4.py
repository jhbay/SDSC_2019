import numpy as np
import pandas as pd

from bokeh.io import output_notebook, show
from bokeh.charts import *
output_notebook()

from nose.tools import *

## mongoDB client와 data가 존재해야 사용가능
# import pymongo
# from pymongo import MongoClient
# client = MongoClient('mongodb://cpduser:M13pV5woDW@mongodb/health_data', 27017)
# db = client.health_data

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# print('All libraries successfully loaded')

def evaluate_random_data(n, evaluation, seed=543210):
    # YOUR CODE HERE
#     print("seed:", seed)
    rs = np.random.RandomState(seed)
    randList = rs.randint(0,101, n)
    randSeries = pd.Series(randList)
#     print("randList :: ", randList)
    
    result = []
    if(evaluation =='mean'):
        result = randSeries.mean()
    elif(evaluation =='median'):
        result = randSeries.median()
    elif(evaluation =='std'):
        result = randSeries.std()
#     print("result :: ", result)
    return result

    raise NotImplementedError()


def quiz1a():
    # Check a RandomState object is instantiated
    tmp_rs = np.random.RandomState
    del np.random.RandomState

    try:
        evaluate_random_data(100, 'mean')
    except AttributeError:
        print('The function correctly uses RandomState')
    else:
        raise AssertionError('The function does not use RandomState')
    finally:
        np.random.RandomState = tmp_rs

        
    assert_equal(evaluate_random_data(100, 'mean', 511419), 47.39)
    assert_equal(evaluate_random_data(100, 'mean', 364235), 48.45)

    assert_equal(evaluate_random_data(100, 'median', 511419), 46)
    assert_equal(evaluate_random_data(100, 'median', 364235), 44)

    output = evaluate_random_data(100, 'std', 511419)
    "{0:.4f}".format(round(output,4))
    assert_equal("{0:.4f}".format(round(output,4)), '29.2968')

    output = evaluate_random_data(100, 'std', 364235)
    "{0:.4f}".format(round(output,4))
    assert_equal("{0:.4f}".format(round(output,4)), '30.5159')

    print('All tests successfully passed')


# db - not defined by pymongo...
def get_data(collection):
    cursor = db[collection].find({},{'RatingValue': 1, '_id':0})
    rating_values = pd.DataFrame(list(cursor))['RatingValue']
    return rating_values


# 이해안됨. 왜 굳이? You should use the function from Question 1(a) to get a `Series` object of the `RatingValue`

# db - not defined by pymongo...
def get_means(n):
    # YOUR CODE HERE
#     print("get_data(collection):: ", get_data(collection))
    colNames = sorted(db.collection_names() )
    
    resultList = []
    for colName in colNames[ :n ]:
        resultList.append(get_data(colName).mean())
#         RatingValueMeans = evaluate_random_data(n , 'mean', seed=543210)
    
    RatingValueMeans = pd.Series(resultList)
    return RatingValueMeans
    
    raise NotImplementedError()


def quiz1b():
    # You don't need to write anything here
    means = get_means(10)

    assert_equal(type(means), pd.Series)
    assert_equal(len(means), 10)
    assert_equal(round(means.sum(), 4), 27.2436)
    means = get_means(12)
    assert_equal(len(means), 12)
    assert_equal(round(means.sum(), 4), 36.2604)
    print('All tests passed successfully')


# 'seed = 543210', this value is the default setting for seed
def get_sample_mean_distribution(data, n, m=1000, seed=543210):
    # YOUR CODE HERE
    
    resultList = []
    iLi = []
    for i in range(0, m):
        # init RandomState
#         print('seed::', seed)
        rs = np.random.RandomState(seed)
        randList = rs.randint(data.min(), data.max()+1, size = n)
        print('randList::', randList)
        sampleMean = pd.Series(randList).mean()
        resultList.append(sampleMean)
#     print('resultList::', resultList)
    resultSeries = pd.Series(resultList)

    return resultSeries
    raise NotImplementedError()

    
    
# m = 1000
# n = 20
# data = pd.Series([5, 5, 5, 5, 5, 4, 5, 4, 5, 4, 5, 5, 3, 4, 4, 5, 5, 5, 4, 5, 5, 5, 5, 4, 2, 4, 5, 5, 4, 5])
# seed = 123456

# print(round(get_sample_mean_distribution(data, n, m, seed).sum(),4), ' ==? ', 4528.6 )




###########################################################
# quiz1a() 
# quiz1b()



