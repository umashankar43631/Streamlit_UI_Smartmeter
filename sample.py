import streamlit as st
import pandas as pd

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
st.sidebar.markdown("<h1>EPCOR</h1>")
go_back = False
home = True
inside_data = False

def display_zones(go_back):
    if st.sidebar.button("zone1"):
        inside_data  =True
        go_back = st.sidebar.button("Go Back")
        st.table(zone1)
    elif st.sidebar.button("zone2"):
        inside_data  =True
        go_back = st.sidebar.button("Go Back")
        st.table(zone2)
    elif st.sidebar.button("zone3"):
        inside_data  =True
        go_back = st.sidebar.button("Go Back")
        st.table(zone3)
    elif st.sidebar.button("zone4"):
        inside_data  =True
        go_back = st.sidebar.button("Go Back")
        st.table(zone3)
    elif st.sidebar.button("zone5"):
        inside_data  =True
        go_back = st.sidebar.button("Go Back")
        st.table(zone5)
    elif st.sidebar.button("zone6"):
        inside_data  =True
        go_back = st.sidebar.button("Go Back")
        st.table(zone6)
    elif st.sidebar.button("zone7"):
        inside_data  =True
        go_back = st.sidebar.button("Go Back")
        st.table(zone7)
    elif st.sidebar.button("zone8"):
        inside_data  =True
        go_back = st.sidebar.button("Go Back")
        st.table(zone8)

def display_home():
    st.title("Electric vehicles power consumption in House Hold")
    st.write("""Basically, we have the Smart Meter Disaggregation data and we
                want to know how much consumption does Electric vehicles for 1 Charge
                based on the cities.We have only collected data from 4 different cities 
                and from each city we have taken 10 random houses. See the Below Plots for each of the cities""")
    

if (home):
   display_home()
   display_zones(go_back)
   if (go_back==True):
        go_back==False
        display_home
    if(go_back== True):
        
    if (st.button('Zone1 EV Consumption')):
        st.write("Hello")
        if (st.sidebar.button("Go back")):
            continue
        # zone1['EV Spike'] = 0
        # for i in zone1[times_list[6:]]
        # pass
    elif (st.button('Zone2 EV Consumption')):
        st.write("Hello Zone2")
        if (st.sidebar.button("Go back")):
            continue
        # print(times_list[6:])
        
    elif (st.button('Zone3 EV Consumption')):
        st.write("Hello Zone3")
        if (st.sidebar.button("Go back")):
            continue
        
    elif (st.button('Zone4 EV Consumption')):
        st.write("Hello zone 4")
        if (st.sidebar.button("Go back")):
            continue

    elif (st.button('Zone5 EV Consumption')):
        st.write("Hello zone 5")
        if (st.sidebar.button("Go back")):
            continue

    elif (st.button('Zone6 EV Consumption')):
        st.write("Hello zone 6")
        if (st.sidebar.button("Go back")):
            continue

    elif (st.button('Zone7 EV Consumption')):
        st.write("Hello zone7")
        if (st.sidebar.button("Go back")):
            continue

    elif (st.button('Zone8 EV Consumption')):
        st.write("Hello zone8")
        if (st.sidebar.button("Go back")):
            continue


    

