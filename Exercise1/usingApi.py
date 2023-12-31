
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
    print(action.status_code) #code: 200 means 'success'
    print(action.text)
    print(f'Your user id is: {json.loads(action.text)["data"]["id"]}')

# 4) How many employees earn more than ___ ? 
def queryEmployeesBySalary(salary):
   #creating a counter of those employees who satisfy the specification
    count_employees = 0
    for i in getEmployees()['data']:
        if(int(i['employee_salary']) > int(salary)):
           count_employees+=1
    print(f'No. Employees earning more than {salary} is: {count_employees}')

#Testing Area
#print(getEmployees())
#print(getEmployee(1))
#createRecord('carlosLeon',5000,100)
#queryEmployeesBySalary(300000) #Ans: 11

if __name__ == '__main__':
    #Answering Questions: 
    status = False
    while(not status):
        option = int(input('What would you like to know (input number)? \n 1. How many employees earn more than $300,000.00? \n 2. Create a record with your name and know its id \n 3.exit \n'))
        if(option >2):
            status = True
            break
        else:
            if (option == 1 ):
                queryEmployeesBySalary(300000) #Ans: 11
            if (option == 2):
                createRecord('carlosLeon',5000,100)

