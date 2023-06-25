import streamlit as st
import pandas as pd

@st.cache(allow_output_mutation=True)
def initialize_session_state():
    return {'page': 'Home'}

# Initialize session state
if 'page' not in st.session_state:
    st.session_state = initialize_session_state()

# # Initialize session state
# if 'page' not in st.session_state:
#     st.session_state['page'] = 'Home'
# # st.session_state['page'] = st.session_state.get('page', 'Home')

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
###-----------Zone1 Data----------###
    if st.sidebar.button("zone1"):
        st.session_state['page'] = 'zone1_data'
###-----------Zone2 Data----------###
    elif st.sidebar.button("zone2"):
        st.session_state['page'] = 'zone2_data'
###-----------Zone3 Data----------###
    elif st.sidebar.button("zone3"):
        st.session_state['page'] = 'zone3_data'
###-----------Zone4 Data----------###
    elif st.sidebar.button("zone4"):
        st.session_state['page'] = 'zone4_data'
###-----------Zone5 Data----------###
    elif st.sidebar.button("zone5"):
        st.session_state['page'] = 'zone5_data'
###-----------Zone6 Data----------###
    elif st.sidebar.button("zone6"):
        st.session_state['page'] = 'zone6_data'
###-----------Zone7 Data----------###
    elif st.sidebar.button("zone7"):
        st.session_state['page'] = 'zone7_data'
###-----------Zone8 Data----------###
    elif st.sidebar.button("zone8"):
        st.session_state['page'] = 'zone8_data'
     

###-----------Home Screen for Our EPCOR Streamlit UI-------------###
def display_Home():
    st.title("Electric vehicles power consumption in House Hold")
    st.write("""Basically, we have the Smart Meter Disaggregation data and we
                want to know how much consumption does Electric vehicles for 1 Charge
                based on the cities.We have only collected data from 4 different cities 
                and from each city we have taken 10 random houses. See the Below Plots for each of the cities""")
    



def display_plots_by_buttons():
    # Creating sessions for zone consumptions
    ###-------------Zone1 Consumption Session data---------###
    if (st.button('Zone1 EV Consumption')):
        st.session_state['page'] = 'zone1_consumption'

    ###-------------Zone2 Consumption Session data---------###
    elif (st.button('Zone2 EV Consumption')):
        st.session_state['page'] = 'zone2_consumption'  

    ###-------------Zone3 Consumption Session data---------###
    elif (st.button('Zone3 EV Consumption')):
        st.session_state['page'] = 'zone3_consumption'      
    
    ###-------------Zone4 Consumption Session data---------###
    elif (st.button('Zone4 EV Consumption')):
        st.session_state['page'] = 'zone4_consumption'      
    
    ###-------------Zone5 Consumption Session data---------###
    elif (st.button('Zone5 EV Consumption')):
        st.session_state['page'] = 'zone5_consumption'      

    ###-------------Zone6 Consumption Session data---------###
    elif (st.button('Zone6 EV Consumption')):
        st.session_state['page'] = 'zone6_consumption'      

    ###-------------Zone7 Consumption Session data---------####
    elif (st.button('Zone7 EV Consumption')):
        st.session_state['page'] = 'zone7_consumption'

    ###-------------Zone8 Consumption Session data---------####
    elif (st.button('Zone8 EV Consumption')):
        st.session_state['page'] = 'zone8_consumption'



if st.session_state['page'] == 'Home':
   display_Home()
   display_zones()
   display_plots_by_buttons()

## Zone Data Consumption View
##---------Zone1----------###
elif st.session_state['page']=='zone1_data':
    st.table(zone1)
    if (st.sidebar.button("Go Back")):
        st.session_state['page'] = 'Home'
##---------Zone2----------####
elif st.session_state['page']=='zone2_data':
    st.table(zone2)
    if (st.sidebar.button("Go Back")):
        st.session_state['page'] = 'Home'
##---------Zone3----------###
elif st.session_state['page']=='zone3_data':
    st.table(zone3)
    if (st.sidebar.button("Go Back")):
        st.session_state['page'] = 'Home'
##---------Zone4----------####
elif st.session_state['page']=='zone4_data':
    st.table(zone4)
    if (st.sidebar.button("Go Back")):
        st.session_state['page'] = 'Home'
##---------Zone5 Data View----------###
elif st.session_state['page']=='zone5_data':
    st.table(zone5)
    if (st.sidebar.button("Go Back")):
        st.session_state['page'] = 'Home'
##---------Zone6----------####
elif st.session_state['page']=='zone6_data':
    st.table(zone6)
    if (st.sidebar.button("Go Back")):
        st.session_state['page'] = 'Home'
##---------Zone7----------###
elif st.session_state['page']=='zone7_data':
    st.table(zone7)
    if (st.sidebar.button("Go Back")):
        st.session_state['page'] = 'Home'
##---------Zone8----------####
elif st.session_state['page']=='zone8_data':
    st.table(zone8)
    if (st.sidebar.button("Go Back")):
        st.session_state['page'] = 'Home'
## end of session data
# ---------------------------------
## zone Consumption Analysis----
elif (st.session_state['page']=='zone1_consumption'):
    st.write("zone1 consumption")
    if (st.sidebar.button("Go Back")):
        st.session_state['page'] = 'Home'
###-------------Zone2 Consumption Analysis-----------------###
elif (st.session_state['page']=='zone2_consumption'):
    st.write("zone2 consumption")
    if (st.sidebar.button("Go Back")):
        st.session_state['page'] = 'Home'

###-------------Zone8-----------------###
elif (st.session_state['page']=='zone3_consumption'):
    st.write("zone3 consumption")
    if (st.sidebar.button("Go Back")):
        st.session_state['page'] = 'Home'

###-------------Zone8-----------------###
elif (st.session_state['page']=='zone4_consumption'):
    st.write("zone4 consumption")
    if (st.sidebar.button("Go Back")):
        st.session_state['page'] = 'Home'

###-------------Zone8-----------------###
elif (st.session_state['page']=='zone5_consumption'):
    st.write("zone5 consumption")
    if (st.sidebar.button("Go Back")):
        st.session_state['page'] = 'Home'

###-------------Zone8-----------------###
elif (st.session_state['page']=='zone6_consumption'):
    st.write("zone6 consumption")
    if (st.sidebar.button("Go Back")):
        st.session_state['page'] = 'Home'

###-------------Zone8-----------------###
elif (st.session_state['page']=='zone7_consumption'):
    st.write("zone7 consumption")
    if (st.sidebar.button("Go Back")):
        st.session_state['page'] = 'Home'

###-------------Zone8-----------------###
elif (st.session_state['page']=='zone8_consumption'):
    st.write("zone8 consumption")
    if (st.sidebar.button("Go Back")):
        st.session_state['page'] = 'Home'
## Zone Consumption data end