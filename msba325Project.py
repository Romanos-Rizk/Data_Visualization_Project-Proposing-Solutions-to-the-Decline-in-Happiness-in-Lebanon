# Importing relevant libraries for the project:
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#read the happiness data:
df_happiness_2015 = pd.read_csv("https://raw.githubusercontent.com/Romanos-Rizk/MSBA325-Project/main/MSBA%20325-happiness2-2015.csv")
df_happiness_2016 = pd.read_csv("https://raw.githubusercontent.com/Romanos-Rizk/MSBA325-Project/main/MSBA%20325-happiness2-2016.csv")
df_happiness_2017 = pd.read_csv("https://raw.githubusercontent.com/Romanos-Rizk/MSBA325-Project/main/MSBA%20325-happiness2-2017.csv")
df_happiness_2018 = pd.read_csv("https://raw.githubusercontent.com/Romanos-Rizk/MSBA325-Project/main/MSBA%20325-happiness2-2018.csv")
df_happiness_2019 = pd.read_csv("https://raw.githubusercontent.com/Romanos-Rizk/MSBA325-Project/main/MSBA%20325-happiness2-2019.csv")
df_happiness_2020 = pd.read_csv("https://raw.githubusercontent.com/Romanos-Rizk/MSBA325-Project/main/MSBA%20325-happiness2-2020.csv")
df_happiness_2021 = pd.read_csv("https://raw.githubusercontent.com/Romanos-Rizk/MSBA325-Project/main/MSBA%20325-happiness2-2021.csv")
df_happiness_2022 = pd.read_csv("https://raw.githubusercontent.com/Romanos-Rizk/MSBA325-Project/main/MSBA%20325-happiness2-2022.csv")
df_happiness_2023 = pd.read_csv("https://raw.githubusercontent.com/Romanos-Rizk/MSBA325-Project/main/MSBA%20325-happiness2-2023.csv")

#Show data:
# st.write(df_happiness_2015.head())
# st.write(df_happiness_2016.head())
# st.write(df_happiness_2017.head())
# st.write(df_happiness_2018.head())
# st.write(df_happiness_2019.head())
# st.write(df_happiness_2020.head())
# st.write(df_happiness_2021.head())
# st.write(df_happiness_2022.head())
# st.write(df_happiness_2023.head())

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Happiness per region in 2015
happiness_2015_MENA = round(df_happiness_2015.loc[df_happiness_2015['Region'] == 'MENA', 'Happiness Score'].sum() / (df_happiness_2015['Region'] == 'MENA').sum(),2)
happiness_2015_southernAsia = round(df_happiness_2015.loc[df_happiness_2015['Region'] == 'Southern Asia', 'Happiness Score'].sum() / (df_happiness_2015['Region'] == 'Southern Asia').sum(),2)
happiness_2015_centralandEasternEurope = round(df_happiness_2015.loc[df_happiness_2015['Region'] == 'Central and Eastern Europe', 'Happiness Score'].sum() / (df_happiness_2015['Region'] == 'Central and Eastern Europe').sum(),2)
happiness_2015_latinAmericaAndCaribbean = round(df_happiness_2015.loc[df_happiness_2015['Region'] == 'Latin America and Caribbean', 'Happiness Score'].sum() / (df_happiness_2015['Region'] == 'Latin America and Caribbean').sum(),2)
happiness_2015_australiaAndNewZealand = round(df_happiness_2015.loc[df_happiness_2015['Region'] == 'Australia and New Zealand', 'Happiness Score'].sum() / (df_happiness_2015['Region'] == 'Australia and New Zealand').sum(),2)
happiness_2015_westernEurope = round(df_happiness_2015.loc[df_happiness_2015['Region'] == 'Western Europe', 'Happiness Score'].sum() / (df_happiness_2015['Region'] == 'Western Europe').sum(),2)
happiness_2015_subSaharanAfrica = round(df_happiness_2015.loc[df_happiness_2015['Region'] == 'Sub-Saharan Africa', 'Happiness Score'].sum() / (df_happiness_2015['Region'] == 'Sub-Saharan Africa').sum(),2)
happiness_2015_northAmerica = round(df_happiness_2015.loc[df_happiness_2015['Region'] == 'North America', 'Happiness Score'].sum() / (df_happiness_2015['Region'] == 'North America').sum(),2)
happiness_2015_easternAsia = round(df_happiness_2015.loc[df_happiness_2015['Region'] == 'Eastern Asia', 'Happiness Score'].sum() / (df_happiness_2015['Region'] == 'Eastern Asia').sum(),2)
happiness_2015_southeasternAsia = round(df_happiness_2015.loc[df_happiness_2015['Region'] == 'Southeastern Asia', 'Happiness Score'].sum() / (df_happiness_2015['Region'] == 'Southeastern Asia').sum(),2)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Happiness per region in 2016
happiness_2016_MENA = round(df_happiness_2016.loc[df_happiness_2016['Region'] == 'MENA', 'Happiness Score'].sum() / (df_happiness_2016['Region'] == 'MENA').sum(),2)
happiness_2016_southernAsia = round(df_happiness_2016.loc[df_happiness_2016['Region'] == 'Southern Asia', 'Happiness Score'].sum() / (df_happiness_2016['Region'] == 'Southern Asia').sum(),2)
happiness_2016_centralandEasternEurope = round(df_happiness_2016.loc[df_happiness_2016['Region'] == 'Central and Eastern Europe', 'Happiness Score'].sum() / (df_happiness_2016['Region'] == 'Central and Eastern Europe').sum(),2)
happiness_2016_latinAmericaAndCaribbean = round(df_happiness_2016.loc[df_happiness_2016['Region'] == 'Latin America and Caribbean', 'Happiness Score'].sum() / (df_happiness_2016['Region'] == 'Latin America and Caribbean').sum(),2)
happiness_2016_australiaAndNewZealand = round(df_happiness_2016.loc[df_happiness_2016['Region'] == 'Australia and New Zealand', 'Happiness Score'].sum() / (df_happiness_2016['Region'] == 'Australia and New Zealand').sum(),2)
happiness_2016_westernEurope = round(df_happiness_2016.loc[df_happiness_2016['Region'] == 'Western Europe', 'Happiness Score'].sum() / (df_happiness_2016['Region'] == 'Western Europe').sum(),2)
happiness_2016_subSaharanAfrica = round(df_happiness_2016.loc[df_happiness_2016['Region'] == 'Sub-Saharan Africa', 'Happiness Score'].sum() / (df_happiness_2016['Region'] == 'Sub-Saharan Africa').sum(),2)
happiness_2016_northAmerica = round(df_happiness_2016.loc[df_happiness_2016['Region'] == 'North America', 'Happiness Score'].sum() / (df_happiness_2016['Region'] == 'North America').sum(),2)
happiness_2016_easternAsia = round(df_happiness_2016.loc[df_happiness_2016['Region'] == 'Eastern Asia', 'Happiness Score'].sum() / (df_happiness_2016['Region'] == 'Eastern Asia').sum(),2)
happiness_2016_southeasternAsia = round(df_happiness_2016.loc[df_happiness_2016['Region'] == 'Southeastern Asia', 'Happiness Score'].sum() / (df_happiness_2016['Region'] == 'Southeastern Asia').sum(),2)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Happiness per region in 2017
happiness_2017_MENA =  round(df_happiness_2017.loc[df_happiness_2017['Region'] == 'MENA', 'Happiness Score'].sum() / (df_happiness_2017['Region'] == 'MENA').sum(),2)
happiness_2017_southernAsia =  round(df_happiness_2017.loc[df_happiness_2017['Region'] == 'Southern Asia', 'Happiness Score'].sum() / (df_happiness_2017['Region'] == 'Southern Asia').sum(),2)
happiness_2017_centralandEasternEurope =  round(df_happiness_2017.loc[df_happiness_2017['Region'] == 'Central and Eastern Europe', 'Happiness Score'].sum() / (df_happiness_2017['Region'] == 'Central and Eastern Europe').sum(),2)
happiness_2017_latinAmericaAndCaribbean =  round(df_happiness_2017.loc[df_happiness_2017['Region'] == 'Latin America and Caribbean', 'Happiness Score'].sum()  / (df_happiness_2017['Region'] == 'Latin America and Caribbean').sum(),2)
happiness_2017_australiaAndNewZealand =  round(df_happiness_2017.loc[df_happiness_2017['Region'] == 'Australia and New Zealand', 'Happiness Score'].sum() / (df_happiness_2017['Region'] == 'Australia and New Zealand').sum(),2)
happiness_2017_westernEurope =  round(df_happiness_2017.loc[df_happiness_2017['Region'] == 'Western Europe', 'Happiness Score'].sum() / (df_happiness_2017['Region'] == 'Western Europe').sum(),2)
happiness_2017_subSaharanAfrica =  round(df_happiness_2017.loc[df_happiness_2017['Region'] == 'Sub-Saharan Africa', 'Happiness Score'].sum() / (df_happiness_2017['Region'] == 'Sub-Saharan Africa').sum(),2)
happiness_2017_northAmerica =  round(df_happiness_2017.loc[df_happiness_2017['Region'] == 'North America', 'Happiness Score'].sum() / (df_happiness_2017['Region'] == 'North America').sum(),2)
happiness_2017_easternAsia =  round(df_happiness_2017.loc[df_happiness_2017['Region'] == 'Eastern Asia', 'Happiness Score'].sum() / (df_happiness_2017['Region'] == 'Eastern Asia').sum(),2)
happiness_2017_southeasternAsia =  round(df_happiness_2017.loc[df_happiness_2017['Region'] == 'Southeastern Asia', 'Happiness Score'].sum() / (df_happiness_2017['Region'] == 'Southeastern Asia').sum(),2)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Happiness per region in 2018

happiness_2018_MENA = round(df_happiness_2018.loc[df_happiness_2018['Region'] == 'MENA', 'Happiness Score'].sum() / (df_happiness_2018['Region'] == 'MENA').sum(),2)
happiness_2018_southernAsia = round(df_happiness_2018.loc[df_happiness_2018['Region'] == 'Southern Asia', 'Happiness Score'].sum() / (df_happiness_2018['Region'] == 'Southern Asia').sum(),2)
happiness_2018_centralandEasternEurope = round(df_happiness_2018.loc[df_happiness_2018['Region'] == 'Central and Eastern Europe', 'Happiness Score'].sum() / (df_happiness_2018['Region'] == 'Central and Eastern Europe').sum(),2)
happiness_2018_latinAmericaAndCaribbean = round(df_happiness_2018.loc[df_happiness_2018['Region'] == 'Latin America and Caribbean', 'Happiness Score'].sum() / (df_happiness_2018['Region'] == 'Latin America and Caribbean').sum(),2)
happiness_2018_australiaAndNewZealand = round(df_happiness_2018.loc[df_happiness_2018['Region'] == 'Australia and New Zealand', 'Happiness Score'].sum() / (df_happiness_2018['Region'] == 'Australia and New Zealand').sum(),2)
happiness_2018_westernEurope = round(df_happiness_2018.loc[df_happiness_2018['Region'] == 'Western Europe', 'Happiness Score'].sum() / (df_happiness_2018['Region'] == 'Western Europe').sum(),2)
happiness_2018_subSaharanAfrica = round(df_happiness_2018.loc[df_happiness_2018['Region'] == 'Sub-Saharan Africa', 'Happiness Score'].sum() / (df_happiness_2018['Region'] == 'Sub-Saharan Africa').sum(),2)
happiness_2018_northAmerica = round(df_happiness_2018.loc[df_happiness_2018['Region'] == 'North America', 'Happiness Score'].sum() / (df_happiness_2018['Region'] == 'North America').sum(),2)
happiness_2018_easternAsia = round(df_happiness_2018.loc[df_happiness_2018['Region'] == 'Eastern Asia', 'Happiness Score'].sum() / (df_happiness_2018['Region'] == 'Eastern Asia').sum(),2)
happiness_2018_southeasternAsia = round(df_happiness_2018.loc[df_happiness_2018['Region'] == 'Southeastern Asia', 'Happiness Score'].sum() / (df_happiness_2018['Region'] == 'Southeastern Asia').sum(),2)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Happiness per region in 2019
happiness_2019_MENA = round(df_happiness_2019.loc[df_happiness_2019['Region'] == 'MENA', 'Happiness Score'].sum() / (df_happiness_2019['Region'] == 'MENA').sum(),2)
happiness_2019_southernAsia = round(df_happiness_2019.loc[df_happiness_2019['Region'] == 'Southern Asia', 'Happiness Score'].sum() / (df_happiness_2019['Region'] == 'Southern Asia').sum(),2)
happiness_2019_centralandEasternEurope = round(df_happiness_2019.loc[df_happiness_2019['Region'] == 'Central and Eastern Europe', 'Happiness Score'].sum() / (df_happiness_2019['Region'] == 'Central and Eastern Europe').sum(),2)
happiness_2019_latinAmericaAndCaribbean = round(df_happiness_2019.loc[df_happiness_2019['Region'] == 'Latin America and Caribbean', 'Happiness Score'].sum() / (df_happiness_2019['Region'] == 'Latin America and Caribbean').sum(),2)
happiness_2019_australiaAndNewZealand = round(df_happiness_2019.loc[df_happiness_2019['Region'] == 'Australia and New Zealand', 'Happiness Score'].sum()/ (df_happiness_2019['Region'] == 'Australia and New Zealand').sum(),2)
happiness_2019_westernEurope = round(df_happiness_2019.loc[df_happiness_2019['Region'] == 'Western Europe', 'Happiness Score'].sum() / (df_happiness_2019['Region'] == 'Western Europe').sum(),2)
happiness_2019_subSaharanAfrica = round(df_happiness_2019.loc[df_happiness_2019['Region'] == 'Sub-Saharan Africa', 'Happiness Score'].sum() / (df_happiness_2019['Region'] == 'Sub-Saharan Africa').sum(),2)
happiness_2019_northAmerica = round(df_happiness_2019.loc[df_happiness_2019['Region'] == 'North America', 'Happiness Score'].sum() / (df_happiness_2019['Region'] == 'North America').sum(),2)
happiness_2019_easternAsia = round(df_happiness_2019.loc[df_happiness_2019['Region'] == 'Eastern Asia', 'Happiness Score'].sum() / (df_happiness_2019['Region'] == 'Eastern Asia').sum(),2)
happiness_2019_southeasternAsia = round(df_happiness_2019.loc[df_happiness_2019['Region'] == 'Southeastern Asia', 'Happiness Score'].sum() / (df_happiness_2019['Region'] == 'Southeastern Asia').sum(),2)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Happiness per region in 2020

happiness_2020_MENA = round(df_happiness_2020.loc[df_happiness_2020['Region'] == 'MENA', 'Happiness Score'].sum() / (df_happiness_2020['Region'] == 'MENA').sum(),2)
happiness_2020_southernAsia = round(df_happiness_2020.loc[df_happiness_2020['Region'] == 'Southern Asia', 'Happiness Score'].sum() / (df_happiness_2020['Region'] == 'Southern Asia').sum(),2)
happiness_2020_centralandEasternEurope = round(df_happiness_2020.loc[df_happiness_2020['Region'] == 'Central and Eastern Europe', 'Happiness Score'].sum() / (df_happiness_2020['Region'] == 'Central and Eastern Europe').sum(),2)
happiness_2020_latinAmericaAndCaribbean = round(df_happiness_2020.loc[df_happiness_2020['Region'] == 'Latin America and Caribbean', 'Happiness Score'].sum() / (df_happiness_2020['Region'] == 'Latin America and Caribbean').sum(),2)
happiness_2020_australiaAndNewZealand = round(df_happiness_2020.loc[df_happiness_2020['Region'] == 'Australia and New Zealand', 'Happiness Score'].sum() / (df_happiness_2020['Region'] == 'Australia and New Zealand').sum(),2)
happiness_2020_westernEurope = round(df_happiness_2020.loc[df_happiness_2020['Region'] == 'Western Europe', 'Happiness Score'].sum() / (df_happiness_2020['Region'] == 'Western Europe').sum(),2)
happiness_2020_subSaharanAfrica = round(df_happiness_2020.loc[df_happiness_2020['Region'] == 'Sub-Saharan Africa', 'Happiness Score'].sum() / (df_happiness_2020['Region'] == 'Sub-Saharan Africa').sum(),2)
happiness_2020_northAmerica = round(df_happiness_2020.loc[df_happiness_2020['Region'] == 'North America', 'Happiness Score'].sum() / (df_happiness_2020['Region'] == 'North America').sum(),2)
happiness_2020_easternAsia = round(df_happiness_2020.loc[df_happiness_2020['Region'] == 'Eastern Asia', 'Happiness Score'].sum() / (df_happiness_2020['Region'] == 'Eastern Asia').sum(),2)
happiness_2020_southeasternAsia = round(df_happiness_2020.loc[df_happiness_2020['Region'] == 'Southeastern Asia', 'Happiness Score'].sum() / (df_happiness_2020['Region'] == 'Southeastern Asia').sum(),2)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Happiness per region in 2021
happiness_2021_MENA = round(df_happiness_2021.loc[df_happiness_2021['Region'] == 'MENA', 'Happiness Score'].sum() / (df_happiness_2021['Region'] == 'MENA').sum(),2)
happiness_2021_southernAsia = round(df_happiness_2021.loc[df_happiness_2021['Region'] == 'Southern Asia', 'Happiness Score'].sum() / (df_happiness_2021['Region'] == 'Southern Asia').sum(),2)
happiness_2021_centralandEasternEurope = round(df_happiness_2021.loc[df_happiness_2021['Region'] == 'Central and Eastern Europe', 'Happiness Score'].sum() / (df_happiness_2021['Region'] == 'Central and Eastern Europe').sum(),2)
happiness_2021_latinAmericaAndCaribbean = round(df_happiness_2021.loc[df_happiness_2021['Region'] == 'Latin America and Caribbean', 'Happiness Score'].sum() / (df_happiness_2021['Region'] == 'Latin America and Caribbean').sum(),2)
happiness_2021_australiaAndNewZealand = round(df_happiness_2021.loc[df_happiness_2021['Region'] == 'Australia and New Zealand', 'Happiness Score'].sum() / (df_happiness_2021['Region'] == 'Australia and New Zealand').sum(),2)
happiness_2021_westernEurope = round(df_happiness_2021.loc[df_happiness_2021['Region'] == 'Western Europe', 'Happiness Score'].sum() / (df_happiness_2021['Region'] == 'Western Europe').sum(),2)
happiness_2021_subSaharanAfrica = round(df_happiness_2021.loc[df_happiness_2021['Region'] == 'Sub-Saharan Africa', 'Happiness Score'].sum() / (df_happiness_2021['Region'] == 'Sub-Saharan Africa').sum(),2)
happiness_2021_northAmerica = round(df_happiness_2021.loc[df_happiness_2021['Region'] == 'North America', 'Happiness Score'].sum() / (df_happiness_2021['Region'] == 'North America').sum(),2)
happiness_2021_easternAsia = round(df_happiness_2021.loc[df_happiness_2021['Region'] == 'Eastern Asia', 'Happiness Score'].sum() / (df_happiness_2021['Region'] == 'Eastern Asia').sum(),2)
happiness_2021_southeasternAsia = round(df_happiness_2021.loc[df_happiness_2021['Region'] == 'Southeastern Asia', 'Happiness Score'].sum() / (df_happiness_2021['Region'] == 'Southeastern Asia').sum(),2)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Happiness per region in 2022
happiness_2022_MENA = round(df_happiness_2022.loc[df_happiness_2022['Region'] == 'MENA', 'Happiness Score'].sum() / (df_happiness_2022['Region'] == 'MENA').sum(),2)
happiness_2022_southernAsia = round(df_happiness_2022.loc[df_happiness_2022['Region'] == 'Southern Asia', 'Happiness Score'].sum() / (df_happiness_2022['Region'] == 'Southern Asia').sum(),2)
happiness_2022_centralandEasternEurope = round(df_happiness_2022.loc[df_happiness_2022['Region'] == 'Central and Eastern Europe', 'Happiness Score'].sum() / (df_happiness_2022['Region'] == 'Central and Eastern Europe').sum(),2)
happiness_2022_latinAmericaAndCaribbean = round(df_happiness_2022.loc[df_happiness_2022['Region'] == 'Latin America and Caribbean', 'Happiness Score'].sum() / (df_happiness_2022['Region'] == 'Latin America and Caribbean').sum(),2)
happiness_2022_australiaAndNewZealand = round(df_happiness_2022.loc[df_happiness_2022['Region'] == 'Australia and New Zealand', 'Happiness Score'].sum() / (df_happiness_2022['Region'] == 'Australia and New Zealand').sum(),2)
happiness_2022_westernEurope = round(df_happiness_2022.loc[df_happiness_2022['Region'] == 'Western Europe', 'Happiness Score'].sum() / (df_happiness_2022['Region'] == 'Western Europe').sum(),2)
happiness_2022_subSaharanAfrica = round(df_happiness_2022.loc[df_happiness_2022['Region'] == 'Sub-Saharan Africa', 'Happiness Score'].sum() / (df_happiness_2022['Region'] == 'Sub-Saharan Africa').sum(),2)
happiness_2022_northAmerica = round(df_happiness_2022.loc[df_happiness_2022['Region'] == 'North America', 'Happiness Score'].sum() / (df_happiness_2022['Region'] == 'North America').sum(),2)
happiness_2022_easternAsia = round(df_happiness_2022.loc[df_happiness_2022['Region'] == 'Eastern Asia', 'Happiness Score'].sum() / (df_happiness_2022['Region'] == 'Eastern Asia').sum(),2)
happiness_2022_southeasternAsia = round(df_happiness_2022.loc[df_happiness_2022['Region'] == 'Southeastern Asia', 'Happiness Score'].sum() / (df_happiness_2022['Region'] == 'Southeastern Asia').sum(),2)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Happiness per region in 2023
happiness_2023_MENA = round(df_happiness_2023.loc[df_happiness_2023['Region'] == 'MENA', 'Happiness Score'].sum() / (df_happiness_2023['Region'] == 'MENA').sum(),2)
happiness_2023_southernAsia = round(df_happiness_2023.loc[df_happiness_2023['Region'] == 'Southern Asia', 'Happiness Score'].sum() / (df_happiness_2023['Region'] == 'Southern Asia').sum(),2)
happiness_2023_centralandEasternEurope = round(df_happiness_2023.loc[df_happiness_2023['Region'] == 'Central and Eastern Europe', 'Happiness Score'].sum() / (df_happiness_2023['Region'] == 'Central and Eastern Europe').sum(),2)
happiness_2023_latinAmericaAndCaribbean = round(df_happiness_2023.loc[df_happiness_2023['Region'] == 'Latin America and Caribbean', 'Happiness Score'].sum() / (df_happiness_2023['Region'] == 'Latin America and Caribbean').sum(),2)
happiness_2023_australiaAndNewZealand = round(df_happiness_2023.loc[df_happiness_2023['Region'] == 'Australia and New Zealand', 'Happiness Score'].sum() / (df_happiness_2023['Region'] == 'Australia and New Zealand').sum(),2)
happiness_2023_westernEurope = round(df_happiness_2023.loc[df_happiness_2023['Region'] == 'Western Europe', 'Happiness Score'].sum() / (df_happiness_2023['Region'] == 'Western Europe').sum(),2)
happiness_2023_subSaharanAfrica = round(df_happiness_2023.loc[df_happiness_2023['Region'] == 'Sub-Saharan Africa', 'Happiness Score'].sum() / (df_happiness_2023['Region'] == 'Sub-Saharan Africa').sum(),2)
happiness_2023_northAmerica = round(df_happiness_2023.loc[df_happiness_2023['Region'] == 'North America', 'Happiness Score'].sum() / (df_happiness_2023['Region'] == 'North America').sum(),2)
happiness_2023_easternAsia = round(df_happiness_2023.loc[df_happiness_2023['Region'] == 'Eastern Asia', 'Happiness Score'].sum() / (df_happiness_2023['Region'] == 'Eastern Asia').sum(),2)
happiness_2023_southeasternAsia = round(df_happiness_2023.loc[df_happiness_2023['Region'] == 'Southeastern Asia', 'Happiness Score'].sum() / (df_happiness_2023['Region'] == 'Southeastern Asia').sum(),2)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Creating 9 datasets: for the average happiness per region for each year


#Creating a data frame containing the Region and their respecting Average Happiness rate for 2015
# df_happinessAvg_2015 = df = pd.DataFrame({'Region':(np.array(['MENA','Southern Asia','Central and Eastern Europe','Latin America and Caribbean','Australia and New Zealand','Western Europe', 'Sub-Saharan Africa', 'North America', 'Eastern Asia', 'Southeastern Asia'])), 
#                                           'Average Score':(np.array([happiness_2015_MENA,happiness_2015_southernAsia,happiness_2015_centralandEasternEurope,happiness_2015_latinAmericaAndCaribbean,happiness_2015_australiaAndNewZealand, happiness_2015_westernEurope,happiness_2015_subSaharanAfrica,happiness_2015_northAmerica,happiness_2015_easternAsia,happiness_2015_southeasternAsia])),
#                                           'Latitude':(np.array([30.594644,25.395994,54.713718,-9.419912,-26.464188, 49.282356,4.976322,48.345077,42.012740,35.657967])),
#                                           'Longitude':(np.array([32.908213,77.747315,32.538976,-59.438476,136.822983, 7.365950,20.524435,-104.236806,104.131055,127.740093]))})
# #st.write(df_happinessAvg_2015)

# #Creating a data frame containing the Region and their respecting Average Happiness rate for 2016
# df_happinessAvg_2016 = pd.DataFrame({'Region': np.array(['MENA', 'Southern Asia', 'Central and Eastern Europe', 'Latin America and Caribbean', 'Australia and New Zealand', 'Western Europe', 'Sub-Saharan Africa', 'North America', 'Eastern Asia', 'Southeastern Asia']),
#                                      'Average Score': np.array([happiness_2016_MENA, happiness_2016_southernAsia, happiness_2016_centralandEasternEurope, happiness_2016_latinAmericaAndCaribbean, happiness_2016_australiaAndNewZealand, happiness_2016_westernEurope, happiness_2016_subSaharanAfrica, happiness_2016_northAmerica, happiness_2016_easternAsia, happiness_2016_southeasternAsia]),
#                                      'Latitude':(np.array([30.594644,25.395994,54.713718,-9.419912,-26.464188, 49.282356,4.976322,48.345077,42.012740,35.657967])),
#                                      'Longitude':(np.array([32.908213,77.747315,32.538976,-59.438476,136.822983, 7.365950,20.524435,-104.236806,104.131055,127.740093]))})
# #st.write(df_happinessAvg_2016)

# #Creating a data frame containing the Region and their respecting Average Happiness rate for 2017
# df_happinessAvg_2017 = pd.DataFrame({'Region': np.array(['MENA', 'Southern Asia', 'Central and Eastern Europe', 'Latin America and Caribbean', 'Australia and New Zealand', 'Western Europe', 'Sub-Saharan Africa', 'North America', 'Eastern Asia', 'Southeastern Asia']),
#                                      'Average Score': np.array([happiness_2017_MENA, happiness_2017_southernAsia, happiness_2017_centralandEasternEurope, happiness_2017_latinAmericaAndCaribbean, happiness_2017_australiaAndNewZealand, happiness_2017_westernEurope, happiness_2017_subSaharanAfrica, happiness_2017_northAmerica, happiness_2017_easternAsia, happiness_2017_southeasternAsia]),
#                                      'Latitude':(np.array([30.594644,25.395994,54.713718,-9.419912,-26.464188, 49.282356,4.976322,48.345077,42.012740,35.657967])),
#                                      'Longitude':(np.array([32.908213,77.747315,32.538976,-59.438476,136.822983, 7.365950,20.524435,-104.236806,104.131055,127.740093]))})
# #st.write(df_happinessAvg_2017)

# #Creating a data frame containing the Region and their respecting Average Happiness rate for 2018
# df_happinessAvg_2018 = pd.DataFrame({'Region': np.array(['MENA', 'Southern Asia', 'Central and Eastern Europe', 'Latin America and Caribbean', 'Australia and New Zealand', 'Western Europe', 'Sub-Saharan Africa', 'North America', 'Eastern Asia', 'Southeastern Asia']),
#                                      'Average Score': np.array([happiness_2018_MENA, happiness_2018_southernAsia, happiness_2018_centralandEasternEurope, happiness_2018_latinAmericaAndCaribbean, happiness_2018_australiaAndNewZealand, happiness_2018_westernEurope, float(4.212), happiness_2018_northAmerica, happiness_2018_easternAsia, happiness_2018_southeasternAsia]),
#                                      'Latitude':(np.array([30.594644,25.395994,54.713718,-9.419912,-26.464188, 49.282356,4.976322,48.345077,42.012740,35.657967])),
#                                      'Longitude':(np.array([32.908213,77.747315,32.538976,-59.438476,136.822983, 7.365950,20.524435,-104.236806,104.131055,127.740093]))})
# #st.write(df_happinessAvg_2018)

# #Creating a data frame containing the Region and their respecting Average Happiness rate for 2019
# df_happinessAvg_2019 = pd.DataFrame({'Region': np.array(['MENA', 'Southern Asia', 'Central and Eastern Europe', 'Latin America and Caribbean', 'Australia and New Zealand', 'Western Europe', 'Sub-Saharan Africa', 'North America', 'Eastern Asia', 'Southeastern Asia']),
#                                      'Average Score': np.array([happiness_2019_MENA, happiness_2019_southernAsia, happiness_2019_centralandEasternEurope, happiness_2019_latinAmericaAndCaribbean, happiness_2019_australiaAndNewZealand, happiness_2019_westernEurope, happiness_2019_subSaharanAfrica, happiness_2019_northAmerica, happiness_2019_easternAsia, happiness_2019_southeasternAsia]),
#                                      'Latitude':(np.array([30.594644,25.395994,54.713718,-9.419912,-26.464188, 49.282356,4.976322,48.345077,42.012740,35.657967])),
#                                      'Longitude':(np.array([32.908213,77.747315,32.538976,-59.438476,136.822983, 7.365950,20.524435,-104.236806,104.131055,127.740093]))})
# #st.write(df_happinessAvg_2019)

# #Creating a data frame containing the Region and their respecting Average Happiness rate for 2020
# df_happinessAvg_2020 = pd.DataFrame({'Region': np.array(['MENA', 'Southern Asia', 'Central and Eastern Europe', 'Latin America and Caribbean', 'Australia and New Zealand', 'Western Europe', 'Sub-Saharan Africa', 'North America', 'Eastern Asia', 'Southeastern Asia']),
#                                      'Average Score': np.array([happiness_2020_MENA, happiness_2020_southernAsia, happiness_2020_centralandEasternEurope, happiness_2020_latinAmericaAndCaribbean, happiness_2020_australiaAndNewZealand, happiness_2020_westernEurope, happiness_2020_subSaharanAfrica, happiness_2020_northAmerica, happiness_2020_easternAsia, happiness_2020_southeasternAsia]),
#                                      'Latitude':(np.array([30.594644,25.395994,54.713718,-9.419912,-26.464188, 49.282356,4.976322,48.345077,42.012740,35.657967])),
#                                      'Longitude':(np.array([32.908213,77.747315,32.538976,-59.438476,136.822983, 7.365950,20.524435,-104.236806,104.131055,127.740093]))})
# #st.write(df_happinessAvg_2020)

# #Creating a data frame containing the Region and their respecting Average Happiness rate for 2021
# df_happinessAvg_2021 = pd.DataFrame({'Region': np.array(['MENA', 'Southern Asia', 'Central and Eastern Europe', 'Latin America and Caribbean', 'Australia and New Zealand', 'Western Europe', 'Sub-Saharan Africa', 'North America', 'Eastern Asia', 'Southeastern Asia']),
#                                      'Average Score': np.array([happiness_2021_MENA, happiness_2021_southernAsia, happiness_2021_centralandEasternEurope, happiness_2021_latinAmericaAndCaribbean, happiness_2021_australiaAndNewZealand, happiness_2021_westernEurope, happiness_2021_subSaharanAfrica, happiness_2021_northAmerica, happiness_2021_easternAsia, happiness_2021_southeasternAsia]),
#                                      'Latitude':(np.array([30.594644,25.395994,54.713718,-9.419912,-26.464188, 49.282356,4.976322,48.345077,42.012740,35.657967])),
#                                      'Longitude':(np.array([32.908213,77.747315,32.538976,-59.438476,136.822983, 7.365950,20.524435,-104.236806,104.131055,127.740093]))})
# #st.write(df_happinessAvg_2021)

# #Creating a data frame containing the Region and their respecting Average Happiness rate for 2022
# df_happinessAvg_2022 = pd.DataFrame({'Region': np.array(['MENA', 'Southern Asia', 'Central and Eastern Europe', 'Latin America and Caribbean', 'Australia and New Zealand', 'Western Europe', 'Sub-Saharan Africa', 'North America', 'Eastern Asia', 'Southeastern Asia']),
#                                      'Average Score': np.array([happiness_2022_MENA, happiness_2022_southernAsia, happiness_2022_centralandEasternEurope, happiness_2022_latinAmericaAndCaribbean, happiness_2022_australiaAndNewZealand, happiness_2022_westernEurope, happiness_2022_subSaharanAfrica, happiness_2022_northAmerica, happiness_2022_easternAsia, happiness_2022_southeasternAsia]),
#                                      'Latitude':(np.array([30.594644,25.395994,54.713718,-9.419912,-26.464188, 49.282356,4.976322,48.345077,42.012740,35.657967])),
#                                      'Longitude':(np.array([32.908213,77.747315,32.538976,-59.438476,136.822983, 7.365950,20.524435,-104.236806,104.131055,127.740093]))})
# #st.write(df_happinessAvg_2022)

# #Creating a data frame containing the Region and their respecting Average Happiness rate for 2023
# df_happinessAvg_2023 = pd.DataFrame({'Region': np.array(['MENA', 'Southern Asia', 'Central and Eastern Europe', 'Latin America and Caribbean', 'Australia and New Zealand', 'Western Europe', 'Sub-Saharan Africa', 'North America', 'Eastern Asia', 'Southeastern Asia']),
#                                      'Average Score': np.array([happiness_2023_MENA, happiness_2023_southernAsia, happiness_2023_centralandEasternEurope, happiness_2023_latinAmericaAndCaribbean, happiness_2023_australiaAndNewZealand, happiness_2023_westernEurope, happiness_2023_subSaharanAfrica, happiness_2023_northAmerica, happiness_2023_easternAsia, happiness_2023_southeasternAsia]),
#                                      'Latitude':(np.array([30.594644,25.395994,54.713718,-9.419912,-26.464188, 49.282356,4.976322,48.345077,42.012740,35.657967])),
#                                      'Longitude':(np.array([32.908213,77.747315,32.538976,-59.438476,136.822983, 7.365950,20.524435,-104.236806,104.131055,127.740093]))})
# #st.write(df_happinessAvg_2023)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#MAP of regions:

# Create a scatter map
# fig = px.scatter_geo(df_happinessAvg_2015, 
#                      lat='Latitude', 
#                      lon='Longitude', 
#                      text='Average Score',
#                      color='Average Score',
#                      color_continuous_scale='Viridis',
#                      size='Average Score',  # Adjust marker size based on value
#                      projection='natural earth',  # You can choose different projections
#                      title='Values at Specific Coordinates')

# fig.update_geos(showcoastlines=True, coastlinecolor="Black")

# # Customize the appearance
# fig.update_traces(marker=dict(size=12, opacity=0.8, line=dict(width=2, color='Black'), colorbar=dict(title='Value')))

# # Adjust the layout
# fig.update_layout(geo=dict(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white"))

# st.plotly_chart(fig)


#-------------------------------------------------------------------------------------------------------------------------------------
#Adding the average per region for each country based on the region it beongs to:


df_happiness_2015['Average Per Region'] = 0
df_happiness_2015.loc[(df_happiness_2015['Region']=='MENA'), 'Average Per Region'] = happiness_2015_MENA
df_happiness_2015.loc[(df_happiness_2015['Region']=='Southern Asia'), 'Average Per Region'] = happiness_2015_southernAsia
df_happiness_2015.loc[(df_happiness_2015['Region']=='Central and Eastern Europe'), 'Average Per Region'] = happiness_2015_centralandEasternEurope
df_happiness_2015.loc[(df_happiness_2015['Region']=='Latin America and Caribbean'), 'Average Per Region'] = happiness_2015_latinAmericaAndCaribbean
df_happiness_2015.loc[(df_happiness_2015['Region']=='Australia and New Zealand'), 'Average Per Region'] = happiness_2015_australiaAndNewZealand
df_happiness_2015.loc[(df_happiness_2015['Region']=='Western Europe'), 'Average Per Region'] = happiness_2015_westernEurope
df_happiness_2015.loc[(df_happiness_2015['Region']=='Sub-Saharan Africa'), 'Average Per Region'] = happiness_2015_subSaharanAfrica
df_happiness_2015.loc[(df_happiness_2015['Region']=='North America'), 'Average Per Region'] = happiness_2015_northAmerica
df_happiness_2015.loc[(df_happiness_2015['Region']=='Eastern Asia'), 'Average Per Region'] = happiness_2015_easternAsia
df_happiness_2015.loc[(df_happiness_2015['Region']=='Southeastern Asia'), 'Average Per Region'] = happiness_2015_southeasternAsia
#st.write(df_happiness_2015)

df_happiness_2016['Average Per Region'] = 0
df_happiness_2016.loc[(df_happiness_2016['Region'] == 'MENA'), 'Average Per Region'] = happiness_2016_MENA
df_happiness_2016.loc[(df_happiness_2016['Region'] == 'Southern Asia'), 'Average Per Region'] = happiness_2016_southernAsia
df_happiness_2016.loc[(df_happiness_2016['Region'] == 'Central and Eastern Europe'), 'Average Per Region'] = happiness_2016_centralandEasternEurope
df_happiness_2016.loc[(df_happiness_2016['Region'] == 'Latin America and Caribbean'), 'Average Per Region'] = happiness_2016_latinAmericaAndCaribbean
df_happiness_2016.loc[(df_happiness_2016['Region'] == 'Australia and New Zealand'), 'Average Per Region'] = happiness_2016_australiaAndNewZealand
df_happiness_2016.loc[(df_happiness_2016['Region'] == 'Western Europe'), 'Average Per Region'] = happiness_2016_westernEurope
df_happiness_2016.loc[(df_happiness_2016['Region'] == 'Sub-Saharan Africa'), 'Average Per Region'] = happiness_2016_subSaharanAfrica
df_happiness_2016.loc[(df_happiness_2016['Region'] == 'North America'), 'Average Per Region'] = happiness_2016_northAmerica
df_happiness_2016.loc[(df_happiness_2016['Region'] == 'Eastern Asia'), 'Average Per Region'] = happiness_2016_easternAsia
df_happiness_2016.loc[(df_happiness_2016['Region'] == 'Southeastern Asia'), 'Average Per Region'] = happiness_2016_southeasternAsia
#st.write(df_happiness_2016)

df_happiness_2017['Average Per Region'] = 0
df_happiness_2017.loc[(df_happiness_2017['Region'] == 'MENA'), 'Average Per Region'] = happiness_2017_MENA
df_happiness_2017.loc[(df_happiness_2017['Region'] == 'Southern Asia'), 'Average Per Region'] = happiness_2017_southernAsia
df_happiness_2017.loc[(df_happiness_2017['Region'] == 'Central and Eastern Europe'), 'Average Per Region'] = happiness_2017_centralandEasternEurope
df_happiness_2017.loc[(df_happiness_2017['Region'] == 'Latin America and Caribbean'), 'Average Per Region'] = happiness_2017_latinAmericaAndCaribbean
df_happiness_2017.loc[(df_happiness_2017['Region'] == 'Australia and New Zealand'), 'Average Per Region'] = happiness_2017_australiaAndNewZealand
df_happiness_2017.loc[(df_happiness_2017['Region'] == 'Western Europe'), 'Average Per Region'] = happiness_2017_westernEurope
df_happiness_2017.loc[(df_happiness_2017['Region'] == 'Sub-Saharan Africa'), 'Average Per Region'] = happiness_2017_subSaharanAfrica
df_happiness_2017.loc[(df_happiness_2017['Region'] == 'North America'), 'Average Per Region'] = happiness_2017_northAmerica
df_happiness_2017.loc[(df_happiness_2017['Region'] == 'Eastern Asia'), 'Average Per Region'] = happiness_2017_easternAsia
df_happiness_2017.loc[(df_happiness_2017['Region'] == 'Southeastern Asia'), 'Average Per Region'] = happiness_2017_southeasternAsia
#st.write(df_happiness_2017)

df_happiness_2018['Average Per Region'] = 0
df_happiness_2018.loc[(df_happiness_2018['Region'] == 'MENA'), 'Average Per Region'] = happiness_2018_MENA
df_happiness_2018.loc[(df_happiness_2018['Region'] == 'Southern Asia'), 'Average Per Region'] = happiness_2018_southernAsia
df_happiness_2018.loc[(df_happiness_2018['Region'] == 'Central and Eastern Europe'), 'Average Per Region'] = happiness_2018_centralandEasternEurope
df_happiness_2018.loc[(df_happiness_2018['Region'] == 'Latin America and Caribbean'), 'Average Per Region'] = happiness_2018_latinAmericaAndCaribbean
df_happiness_2018.loc[(df_happiness_2018['Region'] == 'Australia and New Zealand'), 'Average Per Region'] = happiness_2018_australiaAndNewZealand
df_happiness_2018.loc[(df_happiness_2018['Region'] == 'Western Europe'), 'Average Per Region'] = happiness_2018_westernEurope
df_happiness_2018.loc[(df_happiness_2018['Region'] == 'Sub-Saharan Africa'), 'Average Per Region'] = happiness_2018_subSaharanAfrica
df_happiness_2018.loc[(df_happiness_2018['Region'] == 'North America'), 'Average Per Region'] = happiness_2018_northAmerica
df_happiness_2018.loc[(df_happiness_2018['Region'] == 'Eastern Asia'), 'Average Per Region'] = happiness_2018_easternAsia
df_happiness_2018.loc[(df_happiness_2018['Region'] == 'Southeastern Asia'), 'Average Per Region'] = happiness_2018_southeasternAsia
#st.write(df_happiness_2018)

df_happiness_2019['Average Per Region'] = 0
df_happiness_2019.loc[(df_happiness_2019['Region'] == 'MENA'), 'Average Per Region'] = happiness_2019_MENA
df_happiness_2019.loc[(df_happiness_2019['Region'] == 'Southern Asia'), 'Average Per Region'] = happiness_2019_southernAsia
df_happiness_2019.loc[(df_happiness_2019['Region'] == 'Central and Eastern Europe'), 'Average Per Region'] = happiness_2019_centralandEasternEurope
df_happiness_2019.loc[(df_happiness_2019['Region'] == 'Latin America and Caribbean'), 'Average Per Region'] = happiness_2019_latinAmericaAndCaribbean
df_happiness_2019.loc[(df_happiness_2019['Region'] == 'Australia and New Zealand'), 'Average Per Region'] = happiness_2019_australiaAndNewZealand
df_happiness_2019.loc[(df_happiness_2019['Region'] == 'Western Europe'), 'Average Per Region'] = happiness_2019_westernEurope
df_happiness_2019.loc[(df_happiness_2019['Region'] == 'Sub-Saharan Africa'), 'Average Per Region'] = happiness_2019_subSaharanAfrica
df_happiness_2019.loc[(df_happiness_2019['Region'] == 'North America'), 'Average Per Region'] = happiness_2019_northAmerica
df_happiness_2019.loc[(df_happiness_2019['Region'] == 'Eastern Asia'), 'Average Per Region'] = happiness_2019_easternAsia
df_happiness_2019.loc[(df_happiness_2019['Region'] == 'Southeastern Asia'), 'Average Per Region'] = happiness_2019_southeasternAsia
#st.write(df_happiness_2019)

df_happiness_2020['Average Per Region'] = 0
df_happiness_2020.loc[(df_happiness_2020['Region'] == 'MENA'), 'Average Per Region'] = happiness_2020_MENA
df_happiness_2020.loc[(df_happiness_2020['Region'] == 'Southern Asia'), 'Average Per Region'] = happiness_2020_southernAsia
df_happiness_2020.loc[(df_happiness_2020['Region'] == 'Central and Eastern Europe'), 'Average Per Region'] = happiness_2020_centralandEasternEurope
df_happiness_2020.loc[(df_happiness_2020['Region'] == 'Latin America and Caribbean'), 'Average Per Region'] = happiness_2020_latinAmericaAndCaribbean
df_happiness_2020.loc[(df_happiness_2020['Region'] == 'Australia and New Zealand'), 'Average Per Region'] = happiness_2020_australiaAndNewZealand
df_happiness_2020.loc[(df_happiness_2020['Region'] == 'Western Europe'), 'Average Per Region'] = happiness_2020_westernEurope
df_happiness_2020.loc[(df_happiness_2020['Region'] == 'Sub-Saharan Africa'), 'Average Per Region'] = happiness_2020_subSaharanAfrica
df_happiness_2020.loc[(df_happiness_2020['Region'] == 'North America'), 'Average Per Region'] = happiness_2020_northAmerica
df_happiness_2020.loc[(df_happiness_2020['Region'] == 'Eastern Asia'), 'Average Per Region'] = happiness_2020_easternAsia
df_happiness_2020.loc[(df_happiness_2020['Region'] == 'Southeastern Asia'), 'Average Per Region'] = happiness_2020_southeasternAsia
#st.write(df_happiness_2020)

df_happiness_2021['Average Per Region'] = 0
df_happiness_2021.loc[(df_happiness_2021['Region'] == 'MENA'), 'Average Per Region'] = happiness_2021_MENA
df_happiness_2021.loc[(df_happiness_2021['Region'] == 'Southern Asia'), 'Average Per Region'] = happiness_2021_southernAsia
df_happiness_2021.loc[(df_happiness_2021['Region'] == 'Central and Eastern Europe'), 'Average Per Region'] = happiness_2021_centralandEasternEurope
df_happiness_2021.loc[(df_happiness_2021['Region'] == 'Latin America and Caribbean'), 'Average Per Region'] = happiness_2021_latinAmericaAndCaribbean
df_happiness_2021.loc[(df_happiness_2021['Region'] == 'Australia and New Zealand'), 'Average Per Region'] = happiness_2021_australiaAndNewZealand
df_happiness_2021.loc[(df_happiness_2021['Region'] == 'Western Europe'), 'Average Per Region'] = happiness_2021_westernEurope
df_happiness_2021.loc[(df_happiness_2021['Region'] == 'Sub-Saharan Africa'), 'Average Per Region'] = happiness_2021_subSaharanAfrica
df_happiness_2021.loc[(df_happiness_2021['Region'] == 'North America'), 'Average Per Region'] = happiness_2021_northAmerica
df_happiness_2021.loc[(df_happiness_2021['Region'] == 'Eastern Asia'), 'Average Per Region'] = happiness_2021_easternAsia
df_happiness_2021.loc[(df_happiness_2021['Region'] == 'Southeastern Asia'), 'Average Per Region'] = happiness_2021_southeasternAsia
#st.write(df_happiness_2021)

df_happiness_2022['Average Per Region'] = 0
df_happiness_2022.loc[(df_happiness_2022['Region'] == 'MENA'), 'Average Per Region'] = happiness_2022_MENA
df_happiness_2022.loc[(df_happiness_2022['Region'] == 'Southern Asia'), 'Average Per Region'] = happiness_2022_southernAsia
df_happiness_2022.loc[(df_happiness_2022['Region'] == 'Central and Eastern Europe'), 'Average Per Region'] = happiness_2022_centralandEasternEurope
df_happiness_2022.loc[(df_happiness_2022['Region'] == 'Latin America and Caribbean'), 'Average Per Region'] = happiness_2022_latinAmericaAndCaribbean
df_happiness_2022.loc[(df_happiness_2022['Region'] == 'Australia and New Zealand'), 'Average Per Region'] = happiness_2022_australiaAndNewZealand
df_happiness_2022.loc[(df_happiness_2022['Region'] == 'Western Europe'), 'Average Per Region'] = happiness_2022_westernEurope
df_happiness_2022.loc[(df_happiness_2022['Region'] == 'Sub-Saharan Africa'), 'Average Per Region'] = happiness_2022_subSaharanAfrica
df_happiness_2022.loc[(df_happiness_2022['Region'] == 'North America'), 'Average Per Region'] = happiness_2022_northAmerica
df_happiness_2022.loc[(df_happiness_2022['Region'] == 'Eastern Asia'), 'Average Per Region'] = happiness_2022_easternAsia
df_happiness_2022.loc[(df_happiness_2022['Region'] == 'Southeastern Asia'), 'Average Per Region'] = happiness_2022_southeasternAsia
#st.write(df_happiness_2022)

df_happiness_2023['Average Per Region'] = 0
df_happiness_2023.loc[(df_happiness_2023['Region'] == 'MENA'), 'Average Per Region'] = happiness_2023_MENA
df_happiness_2023.loc[(df_happiness_2023['Region'] == 'Southern Asia'), 'Average Per Region'] = happiness_2023_southernAsia
df_happiness_2023.loc[(df_happiness_2023['Region'] == 'Central and Eastern Europe'), 'Average Per Region'] = happiness_2023_centralandEasternEurope
df_happiness_2023.loc[(df_happiness_2023['Region'] == 'Latin America and Caribbean'), 'Average Per Region'] = happiness_2023_latinAmericaAndCaribbean
df_happiness_2023.loc[(df_happiness_2023['Region'] == 'Australia and New Zealand'), 'Average Per Region'] = happiness_2023_australiaAndNewZealand
df_happiness_2023.loc[(df_happiness_2023['Region'] == 'Western Europe'), 'Average Per Region'] = happiness_2023_westernEurope
df_happiness_2023.loc[(df_happiness_2023['Region'] == 'Sub-Saharan Africa'), 'Average Per Region'] = happiness_2023_subSaharanAfrica
df_happiness_2023.loc[(df_happiness_2023['Region'] == 'North America'), 'Average Per Region'] = happiness_2023_northAmerica
df_happiness_2023.loc[(df_happiness_2023['Region'] == 'Eastern Asia'), 'Average Per Region'] = happiness_2023_easternAsia
df_happiness_2023.loc[(df_happiness_2023['Region'] == 'Southeastern Asia'), 'Average Per Region'] = happiness_2023_southeasternAsia
#st.write(df_happiness_2023)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#AVERAGE SCORE PER REGION

st.title("Happiness in Lebanon: analyzing the decrease in Lebanon's happiness index")

st.write("The goal of this study is to provide an overview of Lebanon's current state of 'Happiness' across its population, comparing it to other countries and examining trends over the years. Following an initial exploration of Lebanon's happiness levels, a more in-depth analysis investigates the underlying factors influencing the Happiness score. This study aims to propose potential solutions and strategies based on data-driven insights to address the current state of happiness in Lebanon.")

st.title('Happiness Score Map Per Region')

# Creating a Map Plot for Happiness Scores in the MENA Region:
st.subheader('Happiness Scores Map Plot - All Regions')

st.write("To kick off the analysis, we begin by examining the overall Happiness Score across different regions. An interactive map has been created to visualise and explore this data.")

# Slider to slide over years:
selected_year = st.slider('Select Year', min_value=2015, max_value=2023)

# Filtering data based on selected year and MENA region
if selected_year == 2015:
    selected_data = df_happiness_2015
elif selected_year == 2016:
    selected_data = df_happiness_2016
elif selected_year == 2017:
    selected_data = df_happiness_2017
elif selected_year == 2018:
    selected_data = df_happiness_2018
elif selected_year == 2019:
    selected_data = df_happiness_2019
elif selected_year == 2020:
    selected_data = df_happiness_2020
elif selected_year == 2021:
    selected_data = df_happiness_2021
elif selected_year == 2022:
    selected_data = df_happiness_2022
elif selected_year == 2023:
    selected_data = df_happiness_2023

#st.write(df_happiness_2015.head())

# Creating a choropleth plot using Plotly Express
fig = px.choropleth(
    selected_data,
    locations="Country",
    locationmode="country names",
    hover_name="Country",
    color="Average Per Region",
    color_continuous_scale="reds_r",  # Adjust color scale as needed
    projection="natural earth",  # Adjust projection as needed
    range_color=[min(selected_data["Average Per Region"]), max(selected_data["Average Per Region"])]  # Corrected range_color
)
fig.update_geos(
    showcoastlines=True,
    coastlinecolor="Black",
    showland=True,
    landcolor="lightgray"
)

fig.update_layout(
    #title=f'Happiness Scores Map - MENA Region - Year {df_happiness_2015}',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular',
        center=dict(lon=25, lat=25),  # Set the center of the map
        projection_scale=1.1  # Adjust the zoom level (increase this value to zoom out)
    ))
st.plotly_chart(fig)

st.write("Subsequently, our focus shifts to the MENA (Middle East and North Africa) region, as it is of particular interest. In this phase, we compare Lebanon's Happiness score with that of other Arab countries. An interactive map illustrating the Happiness Scores of countries in the MENA region over the years is generated for a more detailed exploration. And for a clearer representation of Lebanon's ranking in Happiness within the MENA region, an interactive bar chart has been associated to the map, highlighting Lebanon in red, while all other countries are depicted in grey.")




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Score Per Country:

# Creating a Map Plot for Happiness Scores in the MENA Region:
st.subheader('Happiness Scores Map Plot - MENA Region')

st.write("Based on the insights derived from the visuals in 2022, Lebanon's current state regarding happiness can is as follows:")

# Slider to slide over years:
#selected_year = st.slider('Select Year', min_value=min(raw_data['Year']), max_value=max(raw_data['Year']))
selected_year2 = st.slider('Select Year 2', min_value=2015, max_value=2023)

# Filtering data based on selected year and MENA region:
if selected_year2 == 2015:
    selected_data2 = df_happiness_2015.query("Region == 'MENA'")
elif selected_year2 == 2016:
    selected_data2 = df_happiness_2016.query("Region == 'MENA'")
elif selected_year2 == 2017:
    selected_data2 = df_happiness_2017.query("Region == 'MENA'")
elif selected_year2 == 2018:
    selected_data2 = df_happiness_2018.query("Region == 'MENA'")
elif selected_year2 == 2019:
    selected_data2 = df_happiness_2019.query("Region == 'MENA'")
elif selected_year2 == 2020:
    selected_data2 = df_happiness_2020.query("Region == 'MENA'")
elif selected_year2 == 2021:
    selected_data2 = df_happiness_2021.query("Region == 'MENA'")
elif selected_year2 == 2022:
    selected_data2 = df_happiness_2022.query("Region == 'MENA'")
elif selected_year2 == 2023:
    selected_data2 = df_happiness_2023.query("Region == 'MENA'")

#selected_data = raw_data[(raw_data['Year'] == selected_year) & (raw_data['Region'] == 'MENA')]

# Creating a choropleth plot using Plotly Express
fig = px.choropleth(
    selected_data2,
    locations="Country",
    locationmode="country names",
    hover_name="Country",
    color="Happiness Score",
    color_continuous_scale="reds_r",  # Adjust color scale as needed
    projection="natural earth",  # Adjust projection as needed
    range_color=[max(selected_data2['Happiness Score']), min(selected_data2['Happiness Score'])] # Set the range of the color scale (adjust as needed)
)

fig.update_geos(
    showcoastlines=True,
    coastlinecolor="Black",
    showland=True,
    landcolor="lightgray"
)

fig.update_layout(
    title=f'Happiness Scores Map - MENA Region - Year {selected_year}',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular',
        center=dict(lon=25, lat=25),  # Set the center of the map
        projection_scale=4  # Adjust the zoom level (increase this value to zoom out)
    )
)

st.plotly_chart(fig)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Happiness Score in Lebanon over the years

df_happiness_lebanon_2015 = df_happiness_2015.query("Country == 'Lebanon'")
df_happiness_lebanon_2015['Year'] = str('2015')
#st.write(df_happiness_lebanon_2015)

df_happiness_lebanon_2016 = df_happiness_2016.query("Country == 'Lebanon'")
df_happiness_lebanon_2016['Year'] = str('2016')
#st.write(df_happiness_lebanon_2016)

df_happiness_lebanon_2017 = df_happiness_2017.query("Country == 'Lebanon'")
df_happiness_lebanon_2017['Year'] = str('2017')
#st.write(df_happiness_lebanon_2017)

df_happiness_lebanon_2018 = df_happiness_2018.query("Country == 'Lebanon'")
df_happiness_lebanon_2018['Year'] = str('2018')
#st.write(df_happiness_lebanon_2018)

df_happiness_lebanon_2019 = df_happiness_2019.query("Country == 'Lebanon'")
df_happiness_lebanon_2019['Year'] = str('2019')
#st.write(df_happiness_lebanon_2019)

df_happiness_lebanon_2020 = df_happiness_2020.query("Country == 'Lebanon'")
df_happiness_lebanon_2020['Year'] = str('2020')
#st.write(df_happiness_lebanon_2020)

df_happiness_lebanon_2021 = df_happiness_2021.query("Country == 'Lebanon'")
df_happiness_lebanon_2021['Year'] = str('2021')
#st.write(df_happiness_lebanon_2021)

df_happiness_lebanon_2022 = df_happiness_2022.query("Country == 'Lebanon'")
df_happiness_lebanon_2022['Year'] = str('2022')
#st.write(df_happiness_lebanon_2022)

df_happiness_lebanon_2023 = df_happiness_2023.query("Country == 'Lebanon'")
df_happiness_lebanon_2023['Year'] = str('2023')
#st.write(df_happiness_lebanon_2023)

df_happiness_lebanon = pd.concat([df_happiness_lebanon_2015, df_happiness_lebanon_2016,df_happiness_lebanon_2017,df_happiness_lebanon_2018,df_happiness_lebanon_2019,df_happiness_lebanon_2020,df_happiness_lebanon_2021,df_happiness_lebanon_2022,df_happiness_lebanon_2023], axis=0)
#st.write(df_happiness_lebanon)

fig = px.line(df_happiness_lebanon, x='Year', y='Happiness Score', title="Happiness Score Over Time in Lebanon")

# Set the y-axis range to start from 0
fig.update_yaxes(range=[0, max(df_happiness_lebanon['Happiness Score'])])

# Customize the line color to red
fig.update_traces(line=dict(color='red'))

# Remove grid lines
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)

# Set x-axis as discrete (categorical)
fig.update_xaxes(categoryorder='total ascending')

st.plotly_chart(fig)

st.write("Such a low level of happiness raises awareness towards happiness factors, what stands behind it? For that, factors that explain happiness are then studied, revealing that GDP is the main player behind happiness, thus working on GDP’s aspect is now the perspective from which our project will deal with the low happiness score issue.")




