import pandas as pd
import requests
import json

class BlynkAPI():
    def get(token):
        url='https://blynk.cloud/external/api/getAll?token='+token
        try:
            data = json.loads(requests.get(url).text)
        except:
            data = None
        return data
    def getByID(token,ID):
        url='https://blynk.cloud/external/api/get?token='+token+'&dataStreamId='+ID
        try:
            data = requests.get(url).text
        except:
            data = None
        return data
    def setByID(token,ID,v):
        url='https://blynk.cloud/external/api/update?token='+token+'&dataStreamId='+ID+'&value='+v
        try:
            requests.get(url)
        except:
            None
            
        