
#import library
import requests
import json

#Well... it seems that adding 'headers' solve the issue of 'Mod Security'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

# 1) Getting All Employee Data
def getEmployees():
    #routing
    employees_src = 'https://dummy.restapiexample.com/api/v1/employees'
    #Get response and converting data into json
    return json.loads(requests.get(employees_src, headers=headers).text)


# 2) Getting a Single Employees
def getEmployee(id):
    #routing
    employee_src = 'https://dummy.restapiexample.com/api/v1/employee/' + str(id)
    #Get response and converting data into json
    return json.loads(requests.get(employee_src, headers=headers).text)


#3) Adding a record
def createRecord(name,salary,age):
    symbol= '"'
    #routing
    record_src = 'https://dummy.restapiexample.com/api/v1/create'
    record_Json = {"name": symbol+str(name)+symbol,"salary":symbol+str(salary)+symbol,"age":symbol+str(age)+symbol}
    action = requests.post(record_src,json=record_Json, headers=headers)
    print(action.status_code)
    print(action.text)

#Testing Area
print(getEmployees())
#print(getEmployee(1))
#createRecord('carlosLeon',5000,100)