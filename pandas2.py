import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,53,34,45,65,64],
             'Bounce_Rate':[43,53,72,65,54,66]}

df = pd.DataFrame(web_stats)

#print(df)
#print(df.head())
#print(df.tail(2))

#print(df.set_index('Day'))

#print(df.head())


#print(df['Visitors'])

#print(df.Visitors)

#print(df[['Visitors','Bounce_Rate']])

#print(df.Visitors.tolist())

print(np.array(df[['Visitors','Bounce_Rate']]))

df2 = pd.DataFrame(np.array(df[['Visitors','Bounce_Rate']]))

print(df2)
