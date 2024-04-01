import time
import pandas as pd
import streamlit as st
import numpy as np



def main():
    st.title("   HIL Test Automation   ")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Test Automation", "Trends"])
    if page == "Home":
        Home()


#This function will be called when the user selects the Home page
def Home():
    #Init Protocol
    Protocol= None
    # Divide the page into columns
    col1 , col2, col3 =st.columns(3) # 2 columns
    data_frame=pd.DataFrame({"Time": [pd.Timestamp.now()], "Value": [np.random.rand() * 100]})
    chart=st.line_chart(data_frame)
    # Add a title to the first column
    with col3:
        col3.info("Select Communication Protocol")
        Protocol=st.radio(label="Protocol", options=["ModBus", "Serial"], index=None,label_visibility="hidden")
        if Protocol == "ModBus":
            col1.info("ModBus Protocol Selected")
        elif Protocol == "Serial":
            col1.info("Serial Protocol Selected")
        else:
            col1.info("Please select the Communication protocol")

    with col1:
        while (Protocol == "ModBus"):
            timestamp=pd.Timestamp.now()
        
            #At this stage get the data from your device
            from backend import Dummy
            data=Dummy.generate_dummy_stream()
            #Plot the data
            data_frame.loc[len(data_frame)]=[timestamp, data]
            chart=chart.line_chart(data_frame,x="Time",y="Value")
            time.sleep(1)

        while(Protocol == "Serial"):
            return
            #TODO: Handle Streamlit session state




main()
