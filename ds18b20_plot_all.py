from ds18b20_functions import *

df = get_data('ds18b20.log')
clean_up_data(df)

plot_obj = df.plot(x = 'Date', y = 'Temp', figsize = (10,7), title = 'DS18B20 Temperature Reading', grid = True, legend = None, rot = 30)
plot_obj.set_ylabel('Temperature (Degree C)')
plt.show()

