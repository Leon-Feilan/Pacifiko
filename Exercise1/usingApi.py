
#import library
import requests
import json

# 1) Getting Employee Data
def getEmployee():
    #Well... it seems that adding 'headers' solve the issue of 'Mod Security'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    #routing
    employee_src = 'https://dummy.restapiexample.com/api/v1/employees'
    #Get response and converting data into json
    return json.loads(requests.get(employee_src, headers=headers).text)








#Testing Area
#print(getEmployee())