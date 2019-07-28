import pymysql
import os
import csv

class Menu:
    def __init__(self,filename,database_name,username,password,hostname):
        self.filename = filename
        self.database_name = database_name
        self.username = username
        self.password = password
        self.hostname = hostname
    
    def insert_all_records(self,filename,hostname,username,password,database_name):
        try:
            db = pymysql.connect(host = self.hostname, user = self.username, password = self.password, database = self.database_name)
            if os.path.isfile(self.filename):
                cursor = db.cursor()
                f = open(self.filename,'r')
                reader = csv.reader(f)
                f.readline()
                tb = input("Enter the table name from your database: ")
                for val in reader: 
                    query = 'insert into {} values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",{},{})'.format(tb,val[0].strip(),val[1].strip(),val[2].strip(),val[3].strip(),val[4].strip(),val[5].strip(),val[6].strip(),val[7].strip(),val[8].strip(),val[9].strip(),val[10].strip(),val[11].strip())
                    cursor.execute(query)
                    db.commit()     
                f.close()
                print("Entries added successfully.")
            else :
                print("File does not exist.")
    
        except FileNotFoundError:
            print("File not found please check again............")
        except pymysql.err.OperationalError:
            print("Unable to connect to server due to incorrect credentials.")
        except pymysql.err.InternalError or pymysql.err.ProgrammingError:
            print("Database not found.")
        except:
            print("Something went wrong............")
            
    def display_all_records(self,hostname,username,password,database_name):
        try:
            db = pymysql.connect(host = self.hostname, user = self.username, password = self.password, database = self.database_name)
            cursor = db.cursor()
            query = 'select * from {}'.format(input("Enter the table name from your database: "))
            cursor.execute(query)
            count = 0
            for record in cursor.fetchall():
                print(record)
                count +=1
            print('Total number of records: ',count)
        except pymysql.err.OperationalError:
            print("Unable to connect to server due to incorrect credentials.")
        except pymysql.err.ProgrammingError:
            print("Database/Table not found")
        except pymysql.err.InternalError:
            print('Database/Table not found.')
    
    def insert_one_record(self,hostname,username,password,database_name):
        try:
            db = pymysql.connect(host = self.hostname, user = self.username, password = self.password, database = self.database_name)
            tb = input("Enter the table name in your database: ")
            Transaction_date = input("Please enter Transaction_date: ")
            Product = input("Please enter Product: ")
            Price = input("Please enter Product Price: ")
            Payment_Type = input("Please enter Payment Type: ")	
            Name = input("Please enter Name: ")
            City = input("Please enter City: ")
            State = input("Please enter State: ")
            Country = input("Please enter Country: ")
            Account_Created = input("Please enter Account Created Date: ")
            Last_Login = input("Please enter Last login: ")
            Latitude = input("Please enter Latitude: ")
            Longitude = input("Please enter Longitude: ")
            cursor = db.cursor()
            query = "insert into {} value('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(tb, Transaction_date
                              ,Product,Price,Payment_Type,Name,City,State,Country,Account_Created,Last_Login,Latitude,Longitude)
            cursor.execute(query)
            db.commit()     
            print("Entries added successfully.")
        
        except pymysql.err.OperationalError:
            print("Unable to connect to server due to incorrect credentials.")
        except pymysql.err.ProgrammingError:
            print("Table does not exist.")
        except pymysql.err.InternalError:
            print('Database not found.')