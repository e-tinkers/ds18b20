from ds18b20_functions import *

df = get_data('ds18b20.log')
clean_up_data(df)

theDate = df.loc['2017-07-22':'2017-07-22']
# Resample the temperature data to hourly average
temp_resample = theDate.Temp.resample('H').mean()
dt_range = pd.date_range('2017-07-22', periods = 24, freq = 'H')
# Create a new data frame withe the resampled data
hourly_average = pd.DataFrame({'Time': dt_range, 'Temp': np.array(temp_resample)}, index = dt_range)

plot_obj = hourly_average.plot(x = 'Time', y = 'Temp', figsize = (10,7), title = 'DS18B20 Temperatures for July 22 with Hourly Average', legend = None, grid = True, rot = 30)
plot_obj.set_ylabel('Hourly Average Temperature (Degree C)')
plt.show()

