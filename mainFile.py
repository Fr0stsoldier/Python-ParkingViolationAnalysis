import csv
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns

#open csv file
exampleFile = open('parkingviolations.csv')
#pass the contents of the file to a variable
exampleReader = csv.reader(exampleFile)
#pass contents as a list
exampleData = list(exampleReader)
#Creates a list variable
timeValues = []
#the data was passed to the exampleData as a two dimensional list, this passes the values
#into a one-dimensional list
for i in range(len(exampleData)):
    try:
        timeValues.append(exampleData[i][0])
    except ValueError:
        pass
#creates a list variable, passes datetime to convert to military time
worldValues = []
for i in range(len(timeValues)):
    try:
        worldValues.append(datetime.strptime(timeValues[i], '%I%M%p').strftime('%H:%M'))
    except ValueError:
        pass
#converting to a pandas dataframe
df = pd.DataFrame(worldValues, columns=['timestamp'])
#counts the frequency of each time value
df = df.groupby(['timestamp'])['timestamp'].count()
df.index=pd.to_datetime(df.index)

#Creates a plot
sns.set(style="darkgrid")
hourly = df.resample('H').sum()
sns.lineplot(x=hourly.index, y=hourly)
plt.show()
