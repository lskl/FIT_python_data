#----------------------------------------------------------------------
def temperature_sum( temp_avgs, temp_base ):

    temperatures_above = []
    for element in temp_avgs:
        temperatures_above = temperatures_above + [ element - temp_base ]

    temperature_sum = 0
    for element in temperatures_above:
        if element>0:
            temperature_sum = temperature_sum + element

    return temperature_sum

#----------------------------------------------------------------------
def day_temperature_sums( temp_avgs, temp_base ):
    
    day_temperature_sums = []
    for i in range(len(temp_avgs)):
        current_sum = temperature_sum( temp_avgs[:i+1], temp_base )
        day_temperature_sums = day_temperature_sums + [ current_sum ]

    return day_temperature_sums

#----------------------------------------------------------------------
def plant_height( temperature_sum, hm, b0, b1 ):
    
    import numpy as np
    
    return hm / ( 1 + b0 * np.exp( -1 * b1 * temperature_sum ) )
