#importing libraries
import pyodbc
import pandas as pd

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

def setOrderItem(customer_id,order_id):
    pass

#getProductList()
getProductByName('Jelly')