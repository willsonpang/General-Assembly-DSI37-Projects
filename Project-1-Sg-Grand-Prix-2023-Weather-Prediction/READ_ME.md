README.md
# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: Exploring climate data of Singapore

### Project Objectives:
Conduct a preliminary analysis on the provided Singapore weather datasets to determine what kind of weather that the F1 team I am working for, should anticipate and plan for ahead of time for the Singapore Grand Prix 2023 that will be held on 17th September 2023 to get the most advantage possible over the team's other competitors

---

### Data used:
The weather data that were given dating from 2022 back to 1982. The included features in the data are as such: Maximum rainfall in a day (mm), Number of raindays in a month (day), Total rainfall (mm), Monthly mean relative humidity (%), Monthly mean daily sunshine duration (hour), and Monthly mean daily sunshine duration (hours), and Monthly mean surface air temperature (celsius).

However, the data mention above was collected at Changi (not Marina Barrage, where the Singapor GP will be held), and the data given were only for monthly. As such, additional data were brought in to supplement the preliminary analysis. These additional datasets were sourced from the a Singapore government website called weather.gov.sg (http://www.weather.gov.sg/climate-historical-daily/). 

These supplementary data includes features such as: Daily rainfall total (mm), Highest 30 min rainfall (mm), Highest 60 min rainfall (mm), Highest 120 min rainfall (mm), Mean temperature (celsius), Maximum temperature (celsius), Minimum temperature (celsius), Mean wind speed (km/h), and Max wind speed (km/h). These supplementary data that would be used as the secondary data are collected in days, which allowed me to be able to look into the data of the days in the month of September of the past 10 years (2012 - 2022).

Details of these datasets can be found in the data dictionary below:

Primary data: merged-sg-weather.csv
Secondary data: sept_week3_sun.csv

|Feature|Type|Dataset|Description|
|---|---|---|---|
|max_rain|float|rainfall-monthly-highest-daily-total|Maximum rainfall in a day in mm|
|n_rain_days|int|rainfall-monthly-number-of-rain-days|Number of rain days in a month|
|total_rain|float|rainfall-monthly-total|Total rainfall in mm| 
|mean_rh|float|relative-humidity-monthly-mean|Monthly mean relative humidity in %|
|mean_ss|float|sunshine-duration-monthly-mean-daily-duration|Monthly mean daily sunshine duration in hours|
|mean_temp|float|surface-air-temperature-monthly-mean|Monthly mean surface air temperature in degree celsius|
|Daily Rainfall Total (mm)|float|DAILYDATA_S108_202209 - DAILYDATA_S108_201209|Daily Rainfall Total in mm|
|Highest 30 Min Rainfall (mm)|float|DAILYDATA_S108_202209 - DAILYDATA_S108_201209|Highest 30 Min Rainfall in mm|
|Highest 60 Min Rainfall (mm)|float|DAILYDATA_S108_202209 - DAILYDATA_S108_201209|Highest 60 Min Rainfall in mm|
|Highest 120 Min Rainfall (mm)|float|DAILYDATA_S108_202209 - DAILYDATA_S108_201209|Highest 120 Min Rainfall mm|
|Mean Temperature (celsius)|float|DAILYDATA_S108_202209 - DAILYDATA_S108_201209|Mean Temperature in degree celsius|
|Maximum Temperature (celsius)|float|DAILYDATA_S108_202209 - DAILYDATA_S108_201209|Max Temperature in degree celsius|
|Minimum Temperature (celsius)|float|DAILYDATA_S108_202209 - DAILYDATA_S108_201209|Min Temperature in degree celsius|
|Mean Wind Speed (km/h)|float|DAILYDATA_S108_202209 - DAILYDATA_S108_201209|Mean Wind Speed in km/h|
|Max Wind Speed (km/h)|float|DAILYDATA_S108_202209 - DAILYDATA_S108_201209|Max Wind Speed in km/h|

---

### Key takeaways from the analysis:

1. The correlation between features in the primary data are found to be within what was expected. However the data contains a lot of outliers on the high end, which made the distribution of the data such as the Maximum rainfall in a day, and the total rainfall in a month to be positively skewed.

2. The trend that was observed in both the primary and secondary data were mostly in line with the El Nino Southern Oscillation (ENSO) record of each past year.

---

### Recommendation:
Seeing how the mean rainfall rate of the past years have recorded a higher rain rate than the rain rate that stopped the 2022 Japan Grand Prix, it is recommended that the F1 strategy team to make the necessary preparation to anticipate racing in an intermediate / wet condition for the upcoming 2023 Singapore Grand Prix

**Future study recommendation:**
As the rain pattern observed in Singapore for the past 10 years has somewhat coincide with the ENSO records, it is recommended for future study to delve deeper into studying the trend of ENSO along with the Singapore weather as this current study was not able to do that due to time constraint issues.