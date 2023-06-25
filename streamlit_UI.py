import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
city = ['toronto']
lat = ['44.0310471005316']
long = ['-78.949678']
df = pd.DataFrame({'city': city, 'lat': long, 'long': long})
map = folium.Map(location=[44.0310471005316, -78.949678], zoom_start=4, control_scale=True)

import folium
import streamlit as st

from streamlit_folium import st_folium

# center on Liberty Bell, add marker
# m = folium.Map(location=[44.0310471005316, -78.949678], zoom_start=16)
# folium.Marker(
#     [44.0310471005316, -78.949678], popup="Liberty Bell", tooltip="Liberty Bell"
# ).add_to(m)
# # call to render Folium map in Streamlit
# st_data = st_folium(m, width=725)

# The logic will be if one value is greater than 80% of the values present in list then we consider there is an EV Spike
# we find the second max value
# Interquartile Range (IQR) method:

# Arrange the dataset in ascending order.
# Calculate the first quartile (Q1) and third quartile (Q3) of the dataset.
# Calculate the IQR as the difference between Q3 and Q1: IQR = Q3 - Q1.
# Determine the lower and upper bounds for outliers using the formulas:
# Lower bound: Q1 - 1.5 * IQR
# Upper bound: Q3 + 1.5 * IQR
# Any data point below the lower bound or above the upper bound can be considered an outlier.







