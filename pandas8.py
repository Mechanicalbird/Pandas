import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = 'api_key'

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0] [0] [1:]

def grab_initial_state_data():
        states = state_list()
	main_df = pd.DataFrame()

	for abbv in states:
	    query='FMAC/HPI_'+str(abbv)
	    df = quandl.get(query, authtoken=api_key)
	    df.columns=[str(abbv)]

	    df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] *100.0

	    if main_df.empty:
		main_df = df
	    else:
		main_df = main_df.join(df)

	print(main_df.head())

        pickle_out = open('fiddy_states.pickle', 'wb')
	pickle.dump(main_df, pickle_out)
        pickle_out.close()


def HPI_benchmark():
    df = quandl.get('FMAC/HPI_USA', authtoken=api_key)
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] *100.0
    return df

#grab_initial_state_data()


#fig = plt.figure()
#ax1 = plt.subplot2grid((1,1), (0,0))

pickle_in = open('fiddy_states.pickle', 'rb')
HPI_data = pickle.load(pickle_in)

#benchmark = HPI_benchmark()

#HPI_data.plot(ax = ax1)
#benchmark.plot(ax=ax1, color='k', linewidth=10)

#plt.legend().remove()
#plt.show()


HPI_State_Correlation = HPI_data.corr()
print(HPI_State_Correlation)

print(HPI_State_Correlation.describe())
