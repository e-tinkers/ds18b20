from ds18b20_functions import *

df = get_data('ds18b20.log')
clean_up_data(df)

# Get the data for a particular date, e.g. '2017-07-22'
df['Time'] = [timestr.time() for timestr in df['Date']]
df['Temp SMA'] = df['Temp'].rolling(window=6).mean()
july22 = df.loc['2017-07-22 00:00:00':'2017-07-22 23:59:59']
plot_obj = july22.plot(x = 'Time', y = ['Temp','Temp SMA'], figsize = (10,7), title = 'DS18B20 Temperature Reading on July 22', grid = True, rot = 30)
plot_obj.set_ylabel('Temperature (Degree C)')
plt.show()

