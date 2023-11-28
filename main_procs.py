from io import BytesIO
import time
import datetime
from matplotlib import pyplot as plt
import streamlit as st
import getapi as api
import noti
def click_button(cls,b):
    if (b==1):
        cls.lightOnOff(cls,1)
    if (b==2):
        cls.lightOnOff(cls,2)
    if (b==3):
        cls.lightOnOff(cls,3)
    api.BlynkAPI.setByID(cls.token,ID='1',v=str(cls.l1))
    api.BlynkAPI.setByID(cls.token,ID='2',v=str(cls.l2))
    api.BlynkAPI.setByID(cls.token,ID='3',v=str(cls.l3))
class doWit():
    l1=l2=l3=tem=hum=0
    token=''
    tem_values = []
    hum_values = []
    def __init__(cls,token): 
        cls.token=token
        cls.l1=int(api.BlynkAPI.getByID(token,ID='1'))
        cls.l2=int(api.BlynkAPI.getByID(token,ID='2'))
        cls.l3=int(api.BlynkAPI.getByID(token,ID='3'))
        cls.tem=float(api.BlynkAPI.getByID(token,ID='5'))
        cls.hum=float(api.BlynkAPI.getByID(token,ID='6'))
        st.markdown("<h2 style='background-color: #f0f0f0; padding: 10px; border-radius: 5px", unsafe_allow_html=True)
        cls.b1=st.button('Light 1',key='b1',on_click=click_button,args=(doWit,1))
        cls.b2=st.button('Light 2',key='b2',on_click=click_button,args=(doWit,2))
        cls.b3=st.button('Light 3',key='b3',on_click=click_button,args=(doWit,3))
            
    @classmethod
    def display_values(cls, token):
        cls.token = token
        cls.l1=int(api.BlynkAPI.getByID(cls.token,ID='1'))
        cls.l2=int(api.BlynkAPI.getByID(cls.token,ID='2'))
        cls.l3=int(api.BlynkAPI.getByID(cls.token,ID='3'))
        st.markdown("<h2 style='background-color: #f0f0f0; padding: 10px; border-radius: 5px", unsafe_allow_html=True)
        if cls.l1 == 0:
            st.write('Light 1: Off 🔴')
        else:
            st.write('Light 1: On 🟢')

        if cls.l2 == 0:
            st.write('Light 2: Off 🔴')
        else:
            st.write('Light 2: On 🟢')

        if cls.l3 == 0:
            st.write('Light 3: Off 🔴')
        else:
            st.write('Light 3: On 🟢')
    def lightOnOff(cls,l):
        if l==1:
            cls.l1= -cls.l1+1
        elif(l==2):
            cls.l2= -cls.l2+1
        elif(l==3):
            cls.l3= -cls.l3+1
    
    def get_temperature(cls):
        return cls.tem

    def get_humidity(cls):
        return cls.hum
    
    def update_data(cls,output,output_img):
        while True:
            cls.tem=float(api.BlynkAPI.getByID(cls.token,ID='5'))
            cls.hum=float(api.BlynkAPI.getByID(cls.token,ID='6'))

            html = f'''
            <div id='sensor-data'>
                <p>Temperature: {cls.tem}°C</p>
                <p>Humidity: {cls.hum}%</p>
                <p>Time: {datetime.datetime.now().strftime('%H:%M:%S')}</p>
            </div>
            <script>
                // Xóa nội dung cũ sau khi cập nhật dữ liệu mới
                var element = document.getElementById('sensor-data');
                if (element) {{
                    element.parentNode.removeChild(element);
                }}
            </script>
            '''

            # Ghi HTML vào Streamlit
            output.write(html, unsafe_allow_html=True)
            cls.chart_update(output_img)
            time.sleep(30)
            
    def chart_update(cls, output):
        max_data_points = 50
        
        cls.tem_values.append(cls.tem)
        cls.hum_values.append(cls.hum)
        cls.tem_values = cls.tem_values[-max_data_points:]
        cls.hum_values = cls.hum_values[-max_data_points:]

        # Hiển thị biểu đồ
        cls.display_chart(output)

    def display_chart(cls,output):
        plt.figure(figsize=(8, 6))
        plt.subplot(2, 1, 1)
        plt.plot(cls.tem_values, 'r', label='Temperature')
        plt.ylabel('Temperature (°C)')
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.plot(cls.hum_values, 'b', label='Humidity')
        plt.ylabel('Humidity (%)')
        plt.xlabel('Time')
        plt.legend()

        # Lưu biểu đồ vào buffer hình ảnh
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.close()

        # Hiển thị biểu đồ sử dụng st.image()
        output.image(buffer.getvalue())
    def send_noti(cls,gmail):
        noti.send(gmail,cls.l1,cls.l2,cls.l3,cls.tem,cls.hum)
    def send_sdl(cls,gmail,interval):
        noti.timewinders(gmail,interval,cls.l1,cls.l2,cls.l3,cls.tem,cls.hum)