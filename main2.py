import csv
import numpy as np
import plotly.express as px
def plotFigure(dataPath):
    with open(dataPath) as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Roll No",y="Marks In Percentage,Days Present")
        fig.show()
def getDataSource(dataPath):
    Marks,RollNo=[],[]
    with open(dataPath) as f:
        csvReader=csv.DictReader(f)
        for row in csvReader:
            Marks.append(float(row["Marks In Percentage,Days Present"]))
            RollNo.append(float(row["Roll No"]))
    return{"x":Marks,"y":RollNo}
def findCorelation(dataSource):
    corelation=np.corrcoef(dataSource["x"],dataSource["y"])
    print (corelation[0,1])
def functionSetup():
    dataPath="./data2.csv"
    dataSource=getDataSource(dataPath)
    findCorelation(dataSource)
    plotFigure(dataPath)
functionSetup()    