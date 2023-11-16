import mysql.connector
from pathlib import Path

# create connection string to database
try:
    data_folder = Path("../../")
    file_to_open = data_folder / "database_connect.txt"

    # read connect data in file
    with open(file_to_open) as f:
        con_str = f.read().splitlines()
    def constr():
        mydb = mysql.connector.connect(
            host=con_str[0],
            user=con_str[1],
            password=con_str[2],
            database=con_str[3]
        )
        return mydb
except:
  print("Something went wrong..."
        "is in databaseconnect data")
else:
  print("Everything is alright...")
