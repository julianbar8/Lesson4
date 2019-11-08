import pyodbc

#variables to connect to db

server = 'localhost, 1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'



docker_northwind = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

#what is cursor

cursor = docker_northwind.cursor()
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
print(row)


#we can also fetch all rows
all_customers = cursor.execute("SELECT * FROM Customers;").fetchall()
#Fetch all is dangerous and can block our cpu with huge amount of data

print(all_customers)
print(type(all_customers))

for row in all_customers:
    #do operations with data
    print(row.ContactName,row.Fax)

#because this is dangerous we can use while loop to fetchone()
#until record / row is none --> break.

all_products = cursor.execute("SELECT * FROM Products;")

#this is more efficient than fetchall().

while True:
    row_record = all_products.fetchone()
    if row_record is None:
        break
    print(row_record.UnitPrice)

