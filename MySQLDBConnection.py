import pandas as pd
from sqlalchemy import create_engine

mysql_engine = create_engine('mysql+pymysql://root:sHj%406378%23jw@localhost:3306/sureshdb')
connection = mysql_engine.connect()
mysql_df = pd.read_sql("SELECT * FROM Employees", connection)
print(mysql_df)
connection.close()  # password : sHj@6378#jw

# export the data to csv
mysql_df.to_csv('MySQL_employees_data.csv', index=False)
print("Data exported as csv")
