# read temperature
# https://picozero.readthedocs.io/en/latest/recipes.html#internal-temperature-sensor
# In the Thonny Python editor, choose View->Plotter to plot the output of print().
from time import sleep
from picozero import pico_temp_sensor

while True:
    #print(f'Temp: {pico_temp_sensor.temp}')
    print(pico_temp_sensor.temp)
    sleep(1)