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
    #data = pd.read_sql_query("SELECT * FROM dbo.Orders", connection)
    statement = "INSERT INTO dbo.Orders VALUES ("+ str(len(data)+2) + ","+str(customer_id)+","+"'"+str(date.today())+"')"
    ##pd.read_sql_query wouldn't work with inserting values, so we need to use a cursor (something simmilar to a pointer)
    connection.cursor().execute(statement)
    data = pd.read_sql_query("SELECT * FROM dbo.Orders", connection)
    #print(data)

#getProductList()
#getProductByName('Jelly')
setOrder(3)