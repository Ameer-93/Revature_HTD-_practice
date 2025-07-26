import mysql.connector

# Establishing the connection
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="employee"
)

# Creating a cursor object
cursor = conn.cursor()

# Executing the SQL query
cursor.execute("SELECT * FROM employee.ameer")

# Fetching and printing the results
for row in cursor:
    print(row)
cursor.execute("insert into employee.ameer values(1, 'John', 'HR',55),(2, 'Ameer', 'Finance',26)")  
for row in cursor:
    print(row)

# Closing the connection
conn.close()
