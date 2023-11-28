import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading
import streamlit as st
import time
def convert_status(value):
    return "On" if value == 1 else "Off"

def send(gmail,l1,l2,l3,t1,h1):
# creates SMTP session
    l1 = convert_status(l1)
    l2= convert_status(l2)
    l3 = convert_status(l3)
    message = MIMEMultipart()
    message["From"] = "mail4c0d3@gmail.com"
    message["To"] = gmail
    message["Subject"] = "Arduino Information"
    print(l1,l2,l3)
    # message to be sent
    email_content = f"""
    Light 1: {l1}
    Light 2: {l2}
    Light 3: {l3}
    Temperature: {t1} (°C)
    Humidity: {h1} (%)
    """

    # Thêm nội dung email vào thông điệp
    message.attach(MIMEText(email_content, "plain"))
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("mail4c0d3@gmail.com", "kqfu oxxl uxvh noec")
        server.send_message(message)
def send_email_periodically(interval,gmail,l1,l2,l3,t1,h1):
    while True:
        send(gmail,l1,l2,l3,t1,h1)
        time.sleep(interval)
def timewinders(gmail,interval,l1,l2,l3,t1,h1):
    # Giao diện Streamlit
    st.write("Scheduled Email Sender")
    start_button = st.button("Start Scheduled Emails")

    if start_button:
        thread = threading.Thread(target=send_email_periodically, args=(interval,gmail,l1,l2,l3,t1,h1))
        thread.daemon = True
        thread.start()
        