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
    data = pd.read_sql_query("SELECT * FROM dbo.Products", connection)
    print(data)


def getProductByName(name):
    pass

def setOrderItem(customer_id,order_id):
    pass

getProductList()