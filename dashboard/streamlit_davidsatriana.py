# -*- coding: utf-8 -*-
"""streamlit_davidsatriana

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/141Aaf1yTYyNdxFZIHZ2xyfyyYp34LCCn
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit page config
st.title('Air Quality Analysis')

# Load data
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Nongzhanguan_20130301-20170228.csv")
    return df

df = load_data()

# Display the first few rows of the dataset
st.write("First few rows of the dataset:")
st.write(df.head())

# Display data overview
st.write(f"Number of rows: {df.shape[0]}")
st.write(f"Number of columns: {df.shape[1]}")
st.write("Summary Statistics:")
st.write(df.describe())

# Check for missing values
missing_values = df.isnull().sum()
st.write("Missing Values:")
st.write(missing_values)

# Drop rows with missing values
df.dropna(inplace=True)

# Overview of the cleaned dataset
def data_overview(df, message):
  overview = f"{message}: \n" + \
  "Rows: " + str(df.shape[0]) + \
  "\nNumber of features: " + str(df.shape[1]) + \
  "\n\nFeatures:\n" + str(df.columns.tolist()) + \
  "\n\nMissing Values: " + str(df.isna().sum().values.sum()) + \
  "\n\nUnique values:\n" + str(df.nunique().to_string())
  return overview

st.write(data_overview(df, 'Overview of the Cleaned Dataset'))

# Analysis of most common pollutants
pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
most_common_pollutants = {pollutant: df[pollutant].mode().values[0] for pollutant in pollutants}
st.write("Most Common Air Pollutants:")
st.write(most_common_pollutants)

# Display the most common pollutant
most_common_pollutant = max(most_common_pollutants, key=most_common_pollutants.get)
st.write(f"Most Common Air Pollutant in Dataset is: {most_common_pollutant}")

# Frequency of occurrence of pollutants
pollutant_counts = df[pollutants].mode().iloc[0]

# Plot for most common pollutants
st.write("Frequency of Most Common Pollutants:")
fig, ax = plt.subplots()
pollutant_counts.plot(kind='bar', color='skyblue', ax=ax)
plt.title('Most Common Air Pollutants in Dataset')
plt.xlabel('Air Pollutant')
plt.ylabel('Frequency of Occurrence')
plt.xticks(rotation=45)
st.pyplot(fig)

# Annual aggregation of data
annual_data = df.groupby('year').agg({'PM2.5': 'mean', 'PM10': 'mean', 'SO2': 'mean', 'NO2': 'mean', 'CO': 'mean', 'O3': 'mean'})

# Visualization of annual data
st.write("Annual Variation in Air Quality:")
fig, ax = plt.subplots(figsize=(12, 6))
for column in annual_data.columns:
  ax.plot(annual_data.index, annual_data[column], label=column)
plt.title('Annual Variation in Air Quality')
plt.xlabel('Year')
plt.ylabel('Average Value')
plt.legend()
st.pyplot(fig)

