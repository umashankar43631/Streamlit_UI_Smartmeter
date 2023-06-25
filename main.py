import streamlit as st
import pandas as pd

@st.cache_data
def initialize_session_state():
    return {'page': 'Home'}

# Initialize session state
if 'page' not in st.session_state:
    st.session_state = initialize_session_state()

# Zones csv files
zone1 = pd.read_csv('smart_meter_data/zone1_data.csv')
zone2 = pd.read_csv('smart_meter_data/zone2_data.csv')
zone3 = pd.read_csv('smart_meter_data/zone3_data.csv')
zone4 = pd.read_csv('smart_meter_data/zone4_data.csv')
zone5 = pd.read_csv('smart_meter_data/zone5_data.csv')
zone6 = pd.read_csv('smart_meter_data/zone6_data.csv')
zone7 = pd.read_csv('smart_meter_data/zone7_data.csv')
zone8 = pd.read_csv('smart_meter_data/zone8_data.csv')

times_list = zone1.columns[6:]

def display_zones():
    if st.sidebar.button("zone1"):
        st.session_state['page'] = 'zone1_data'
    elif st.sidebar.button("zone2"):
        st.session_state['page'] = 'zone2_data'
    elif st.sidebar.button("zone3"):
        st.session_state['page'] = 'zone3_data'
    elif st.sidebar.button("zone4"):
        st.session_state['page'] = 'zone4_data'
    elif st.sidebar.button("zone5"):
        st.session_state['page'] = 'zone5_data'
    elif st.sidebar.button("zone6"):
        st.session_state['page'] = 'zone6_data'
    elif st.sidebar.button("zone7"):
        st.session_state['page'] = 'zone7_data'
    elif st.sidebar.button("zone8"):
        st.session_state['page'] = 'zone8_data'

def display_home():
    st.title("Electric vehicles power consumption in Household")
    st.write("""Basically, we have the Smart Meter Disaggregation data and we
                want to know how much consumption does Electric vehicles for 1 Charge
                based on the cities. We have only collected data from 4 different cities 
                and from each city, we have taken 10 random houses. See the Below Plots for each of the cities""")

def display_plots_by_buttons():
    if st.button('Zone1 EV Consumption'):
        st.session_state['page'] = 'zone1_consumption'
    elif st.button('Zone2 EV Consumption'):
        st.session_state['page'] = 'zone2_consumption'
    elif st.button('Zone3 EV Consumption'):
        st.session_state['page'] = 'zone3_consumption'
    elif st.button('Zone4 EV Consumption'):
        st.session_state['page'] = 'zone4_consumption'
    elif st.button('Zone5 EV Consumption'):
        st.session_state['page'] = 'zone5_consumption'
    elif st.button('Zone6 EV Consumption'):
        st.session_state['page'] = 'zone6_consumption'
    elif st.button('Zone7 EV Consumption'):
        st.session_state['page'] = 'zone7_consumption'
    elif st.button('Zone8 EV Consumption'):
        st.session_state['page'] = 'zone8_consumption'

if st.session_state['page'] == 'Home':
    display_home()
    display_zones()
    display_plots_by_buttons()

elif st.session_state['page'] == 'zone1_data':
    st.table(zone1)
    if st.sidebar.button("Go Back"):
        st.session_state['page'] = 'Home'

elif st.session_state['page'] == 'zone2_data':
    st.table(zone2)
    if st.sidebar.button("Go Back"):
        st.session_state['page'] = 'Home'

elif st.session_state['page'] == 'zone3_data':
    st.table(zone3)
    if st.sidebar.button("Go Back"):
        st.session_state['page'] = 'Home'

elif st.session_state['page'] == 'zone4_data':
    st.table(zone4)
    if st.sidebar.button("Go Back"):
        st.session_state['page'] = 'Home'

elif st.session_state['page'] == 'zone5_data':
    st.table(zone5)
    if st.sidebar.button("Go Back"):
        st.session_state['page'] = 'Home'

elif st.session_state['page'] == 'zone6_data':
    st.table(zone6)
    if st.sidebar.button("Go Back"):
        st.session_state['page'] = 'Home'

elif st.session_state['page'] == 'zone7_data':
    st.table(zone7)
    if st.sidebar.button("Go Back"):
        st.session_state['page'] = 'Home'

elif st.session_state['page'] == 'zone8_data':
    st.table(zone8)
    if st.sidebar.button("Go Back"):
        st.session_state['page'] = 'Home'

elif st.session_state['page'] == 'zone1_consumption':
    st.write("zone1 consumption")
    if st.sidebar.button("Go Back"):
        st.session_state['page'] = 'Home'

elif st.session_state['page'] == 'zone2_consumption':
    st.write("zone2 consumption")
    if st.sidebar.button("Go Back"):
        st.session_state['page'] = 'Home'

elif st.session_state['page'] == 'zone3_consumption':
    st.write("zone3 consumption")
    if st.sidebar.button("Go Back"):
        st.session_state['page'] = 'Home'

elif st.session_state['page'] == 'zone4_consumption':
    st.write("zone4 consumption")
    if st.sidebar.button("Go Back"):
        st.session_state['page'] = 'Home'

elif st.session_state['page'] == 'zone5_consumption':
    st.write("zone5 consumption")
    if st.sidebar.button("Go Back"):
        st.session_state['page'] = 'Home'

elif st.session_state['page'] == 'zone6_consumption':
    st.write("zone6 consumption")
    if st.sidebar.button("Go Back"):
        st.session_state['page'] = 'Home'

elif st.session_state['page'] == 'zone7_consumption':
    st.write("zone7 consumption")
    if st.sidebar.button("Go Back"):
        st.session_state['page'] = 'Home'

elif st.session_state['page'] == 'zone8_consumption':
    st.write("zone8 consumption")
    if st.sidebar.button("Go Back"):
        st.session_state['page'] = 'Home'





# city = ['toronto']
# lat = ['44.0310471005316']
# long = ['-78.949678']
# df = pd.DataFrame({'city': city, 'lat': long, 'long': long})
# map = folium.Map(location=[44.0310471005316, -78.949678], zoom_start=4, control_scale=True)

# import folium
# import streamlit as st

# from streamlit_folium import st_folium

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
