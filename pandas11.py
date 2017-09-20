import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = '4FqPQe_2E9xruyoa78DA'

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


fig = plt.figure()
ax1 = plt.subplot2grid((2,1), (0,0))
ax2 = plt.subplot2grid((2,1), (1,0), sharex =ax1)

pickle_in = open('fiddy_states.pickle', 'rb')
HPI_data = pickle.load(pickle_in)

HPI_data['TX12MA'] = pd.rolling_mean(HPI_data['TX'],12)
HPI_data['TX12std'] = pd.rolling_std(HPI_data['TX'],12)

print(HPI_data[['TX','TX12MA']].head())
print(HPI_data[['TX','TX12MA', 'TX12std']].head())


HPI_data[['TX','TX12MA']].plot(ax = ax1)
HPI_data['TX12std'].plot(ax = ax2)

plt.legend(loc=4)
plt.show()












