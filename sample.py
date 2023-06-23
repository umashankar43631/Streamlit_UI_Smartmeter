import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cities_data.csv")

st.sidebar.markdown(" <h1> EPCOM </h1>", unsafe_allow_html=True)


inside_data = False
go_back = False
if st.sidebar.button(':blue[Toronto Data]'):
    st.title("Torento City Houses Data")
    st.table(df[df['City']=='Toronto'])
    inside_data  =True
    go_back = st.sidebar.button("Go Back")

elif (st.sidebar.button(':green[Montreal Data]')):
    st.title("Montreal City Houses Data")
    st.table(df[df['City']=='Montreal'])
    inside_data  =True
    go_back = st.sidebar.button("Go Back")


elif (st.sidebar.button(':blue[vancouver Data]')):
    st.title("vancouver City Houses Data")
    st.table(df[df['City']=='Vancouver'])
    inside_data  =True
    go_back = st.sidebar.button("Go Back")


elif (st.sidebar.button(':green[Calgary Data]')):
    st.title("Calagary City Houses Data")
    st.table(df[df['City']=='Calgary'])
    inside_data  =True
    go_back = st.sidebar.button("Go Back")


def generate_plot(city):
    fig, ax = plt.subplots()
    ax.plot(df[df['City'] == city]['EV Consumption(Watts)/day'])
    ax.set_xlabel("Houses")
    ax.set_ylabel("Consumption in watts")
    ax.set_title(f"{city} Consumption Plot")
    return fig
if (go_back == True or inside_data==False):
    st.title("Electric vehicles power consumption in House Hold")
    st.write("""Basically, we have the Smart Meter Disaggregation data and we
                want to know how much consumption does Electric vehicles for 1 Charge
                based on the cities.We have only collected data from 4 different cities 
                and from each city we have taken 10 random houses. See the Below Plots for each of the cities""")
    


    images = {
        "Toronto": "images/toronto.jpg",
        "Montreal": "images/Montreal.jpg",
        "Vancouver": "images/Vancouver.jpg",
        "Calgary": "images/calgary.jpg"
    }

    for city, image_path in images.items():
        st.image(image_path, width=400)
        if st.button(f"{city} EV Consumption Plot"):
            fig = generate_plot(city)
            st.pyplot(fig)