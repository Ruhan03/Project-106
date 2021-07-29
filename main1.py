import csv
import numpy as np
import plotly.express as px
def plotFigure(dataPath):
    with open(dataPath) as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="week",y="Coffee in ml")
        fig.show()
def getDataSource(dataPath):
    Coffee_ml,week=[],[]
    with open(dataPath) as f:
        csvReader=csv.DictReader(f)
        for row in csvReader:
            Coffee_ml.append(float(row["Coffee in ml"]))
            week.append(float(row["week"]))
    return{"x":Coffee_ml,"y":week}
def findCorelation(dataSource):
    corelation=np.corrcoef(dataSource["x"],dataSource["y"])
    print (corelation[0,1])
def functionSetup():
    dataPath="./data1.csv"
    dataSource=getDataSource(dataPath)
    findCorelation(dataSource)
    plotFigure(dataPath)
functionSetup()      