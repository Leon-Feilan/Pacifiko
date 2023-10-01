#importing libraries
import pyodbc
import pandas as pd
from datetime import date #importing date

#querying drivers
#print(pyodbc.drivers())

#Connection's details
connection = pyodbc.connect(
    Driver= '{ODBC Driver 17 for SQL Server}',
    Trusted_Connection = 'Yes',
    Server = "LAPTOP-PUOK99KF",
    Database = "e-commerce"
)



def getProductList():
    data = pd.read_sql_query("SELECT Product_name, Stock_quantity FROM dbo.Products", connection)
    print(data)


def getProductByName(name):
    statement = "SELECT * From dbo.Products WHERE Product_name ="+"'"+name+"'"
    data = pd.read_sql_query(statement, connection)
    print('\n The product is: \n')
    print(data)

def setOrder(customer_id):
    data = pd.read_sql_query("SELECT * FROM dbo.Orders", connection)
    statement = "INSERT INTO dbo.Orders VALUES ("+ str(len(data)+2) + ","+str(customer_id)+","+"'"+str(date.today())+"')"
    ##pd.read_sql_query wouldn't work with inserting values, so we need to use a cursor (something simmilar to a pointer)
    connection.cursor().execute(statement)
    data = pd.read_sql_query("SELECT * FROM dbo.Orders", connection)
    print(data)

def orderUI():
    #print a message
    data = pd.read_sql_query("SELECT * FROM dbo.Customers", connection)
    print('Hey! These are our costumers, please remember their id for creating an order\n')
    print(data)
    id = int(input('\n Please Insert CostumerID: '))
    setOrder(id)
    print('\n Done!')

def mainUI():
    exit=False
    print("\t Welcome!\n")
    while(not exit):
        option = int(input('Please select an action (insert number): \n 1.Display Products and Stock \n 2.Search Products By Name \n 3.Place an Order\n 4.Exit \n : '))
        if(option > 3):
            exit=True
            break
        else:
            if(option==1):
                getProductList()
            elif(option==2):
                getProductByName(str(input('What is the name of the product?: ')))
            else:
                orderUI()

if __name__ == "__main__":
    mainUI()


#Testing Area
#getProductList()
#getProductByName('Jelly')
#setOrder(3)