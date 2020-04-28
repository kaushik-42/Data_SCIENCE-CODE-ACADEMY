#TELL THE BEST TIME TO VISIT LONDON BY USING 2 SIMPLE MEASURES OF STATISTICS LIKE VARIANCE AND STD:
import pandas as pd
import numpy as np
from weather_data import london_data
print(london_data.head())
print(len(london_data))
temp=london_data["TemperatureC"]
avg_temp=np.mean(temp)
print(avg_temp)
temp_var=np.var(temp)
print(temp_var)
temp_std=np.std(temp)
print(temp_std)
print(london_data.columns)
june = london_data.loc[london_data["month"] == 6]["TemperatureC"]
print(june)
july=london_data.loc[london_data["month"]==7]["TemperatureC"]
print(july)
print(np.mean(june))
print(np.mean(july))
print(np.std(june))
print(np.std(july))
for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")
