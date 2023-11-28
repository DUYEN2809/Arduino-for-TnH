import streamlit as st
import main_procs
import login
import pandas as pd
import noti
tokenn=''
st.set_page_config(
page_title="Arduino App",
page_icon="🧊",
initial_sidebar_state="expanded",
menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
token=None
if (token==None):
    token=login.mainn()
st.markdown("""
    # 🧊 Arduino Web-Application
        """)
tokenn=token
              
light_controller = st.container()
light_controller.markdown("<h2 style='background-color: #f0f0f0; padding: 10px; border-radius: 5px;'>Light controller</h2>", unsafe_allow_html=True)
with light_controller:
    col1,col2=st.columns(2)
    st.markdown("<h2 style='background-color: #f0f0f0; padding: 10px; border-radius: 5px", unsafe_allow_html=True)
    with col1:
        User = main_procs.doWit("84NFK0f7n6y24Je00XyseSXVyvmQuJKY")
    with col2:
        User.display_values("84NFK0f7n6y24Je00XyseSXVyvmQuJKY")
   
    ight_controller = st.container()
    ight_controller.markdown("<h2 style='background-color: #f0f0f0; padding: 10px; border-radius: 5px;'>Send me a noti</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='background-color: #f0f0f0; padding: 10px; border-radius: 5px", unsafe_allow_html=True)
    col11,col22=st.columns(2)
    with col11:
        if st.button("Send me an instant email"):
                if (open('gmail_current.txt','r').read() !=""):
                    gmail=open('gmail_current.txt','r').read()
                    User.send_noti(gmail)
    with col22:
        time_options = {
            "5 minutes": 300,
            "10 minutes": 600,
            "30 minutes": 1800,
            "1 hour": 3600
        }

        selected_time = st.selectbox("Select time interval to send email:", list(time_options.keys()))
        interval = time_options[selected_time]
        if st.button("Send me scheduled emails"):
                if (open('gmail_current.txt','r').read() !=""):
                    gmail=open('gmail_current.txt','r').read()
                    User.send_sdl(gmail,interval)  
                    st.success(f"Scheduled emails started at {selected_time} interval!")
                        
    Tem_hum = st.container()
    Tem_hum.markdown("<h2 style='background-color: #f0f0f0; padding: 10px; border-radius: 5px;'>TnH reporter</h2>", unsafe_allow_html=True)
    output = st.empty()
    output_img = st.empty()
    User.update_data(output, output_img)
    
