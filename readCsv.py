import numpy as np 
import pandas as pd
import csv

def readCsvNumpy(csvFilePath):
    # method1. numpy
    from numpy import genfromtxt
    import numpy as np     # installed with matplotlib
    my_data = genfromtxt(csvFilePath, delimiter=',')

def readCsvNumpy2(csvFilePath):
    data = numpy.loadtxt(fname=csvFilePath, delimiter=',')

def readCsvPandas(csvFilePath): 
    df = pd.read_csv(csvFilePath, keep_default_na=False, na_values=['NA', 'NULL', 'NaN'] ) 
    df = df.fillna(0)
    return df
    

def readCsvOneLine(csvFilePath, extra_check=True):
    data = [np.array(map(int, line.split())) for line in open(csvFilePath)] 
     
    return data

def readCsvWithCsv(csvFilePath):
    with open(csvFilePath) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

def readCsvByLine(csvFilePath):
    with open(csvFilePath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1

breakInt = 0 
# my_data = readCsvNumpy('./Omega-Fats.csv')
# my_data = readCsvOneLine('./Omega-Fats.csv')
df = readCsvPandas('./Omega-Fats.csv')
# my_data = readCsvWithCsv('./Omega-Fats.csv')
# my_data = readCsvByLine('./Omega-Fats.csv') 


#첫행 출력
print(df[:1])
#지정 col 출력.
#print(df[['NDB_No','Fat']])

print("-"*20)

#컬럼명 리스트화
#colNames = list(df.columns.values.tolist()) 
print(list(df) )
