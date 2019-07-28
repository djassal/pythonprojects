import urllib.request as req
import pymysql
from Menu import *

def download_file():
    link = "http://samplecsvs.s3.amazonaws.com/SalesJan2009.csv"
    filename = link.split("/")[-1]
    req.urlretrieve(link,filename)
    print( filename,"is downloaded in",os.getcwd())

def database_creation(hostname,username,password):
        try:
            db = pymysql.connect(host = hostname, user = username, password = password)
            cursor = db.cursor()
            db_name = input("Enter the database name: ")
            query = 'create database {}'.format(db_name)
            cursor.execute(query)
            tb = input('Enter table name: ')
            db = pymysql.connect(host = hostname, user = username, password = password,database = db_name)
            cursor = db.cursor()
            query2 = 'create table {} (Transaction_date varchar(50),Product varchar(50),Price varchar(50),Payment_Type varchar(50),Name varchar(50),City varchar(50),State varchar(50),Country varchar(50),Account_Created varchar(50),Last_Login varchar(50),Latitude varchar(50),Longitude varchar(50))'.format(tb)
            cursor.execute(query2)
            print('Database created successfully with table',tb,'.')
        except pymysql.err.OperationalError:
            print("Unable to connect to server due to incorrect credentials.")
        except pymysql.err.ProgrammingError or pymysql.err.InternalError:
            print("Database already exists.")
        except:
            print('Something went wrong.')

if __name__ == '__main__':
    print('****************created by Dhimanshu(dhimanshu1508@gmail.com)*********************')
    print('Welcome to the menu based object oriented program.')
    print('Enter 1 to insert all records from file to database.')
    print('Enter 2 to display all records and total number of records from your database.')
    print('Enter 3 to insert custom record in database.')
    print('Enter 4 to exit the program now.')
    print('Enter 5 to download the csv file/create new database.')
    try: 
        choice = int(input('Please enter your choice: '))
        if choice == 1:
            hostname = input('Please enter your hostname: ')
            username = input('Please enter your username: ')
            password = input('Please enter your password: ')
            db_name = input('Please enter your database name: ')
            filename = input('Please enter the filename: ' )
            action1 = Menu(filename,db_name,username,password,hostname)
            action1.insert_all_records(filename,hostname,username,password,db_name)
        elif choice == 2:
            hostname = input('Please enter your hostname: ')
            username = input('Please enter your username: ')
            password = input('Please enter your password: ')
            db_name = input('Please enter your database name: ')
            action2 = Menu('filename',db_name,username,password,hostname)
            action2.display_all_records(hostname,username,password,db_name)
        elif choice == 3:
            hostname = input('Please enter your hostname: ')
            username = input('Please enter your username: ')
            password = input('Please enter your password: ')
            db_name = input('Please enter your database name: ')
            action2 = Menu('filename',db_name,username,password,hostname)
            action2.insert_one_record(hostname,username,password,db_name)
        elif choice == 4:
            exit
        elif choice == 5:
            choice2 = int(input('Enter 1 for csv file download and 2 for database creation: '))
            if choice2 == 1:
                download_file()
            elif choice2 == 2:
                hostname = input('Please enter your hostname: ')
                username = input('Please enter your username: ')
                password = input('Please enter your password: ')
                database_creation(hostname,username,password)
            else:
                print('Invalid choice.')
        else:
            print("Invalid choice. Please check again.")
    except TypeError :
        print("Please check your input again..........")
    except ValueError :
        print("Please check your input again..........")
    except :
        print("Something went wrong...............")