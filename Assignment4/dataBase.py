'''
Filename: Assignment 4.
Author: tejveer Singh
Course Name: Programming Language Research Project
Course Number: CST8333
Lab	Sec #: 351
Exercise Number: 3
Professors Name: Stanley Pieda.
'''
import csv
import pymysql

firstLine = True
mydb = pymysql.connect("localhost","root","abcd","testDB")
cursor = mydb.cursor()
class dataBaseClass:
    def createTableWithDataInDataBase():#function responsible for creating table in database and entering data
        global firstLine
        cursor.execute("DROP TABLE if exists Dataset")
        cursor.execute("""
            CREATE TABLE Dataset (
            ID int NOT NULL AUTO_INCREMENT,
            REF_DATE varchar(255),
            GEO varchar(255),
            DGUID varchar(255),
            Food_categories varchar(255),
            Commodity varchar(255),
            UOM varchar(255),
            UOM_ID varchar(255),
            SCALAR_FACTOR varchar(255),
            SCALAR_ID varchar(255),
            VECTOR varchar(255),
            COORDINATE varchar(255),
            VALUE varchar(255),
            STATUS varchar(255),
            SYMBOL varchar(255),
            TERMI_NATED varchar(255),
            DECIMALS varchar(255),
            PRIMARY KEY (ID) 
        );
        """)
        with open("32100054.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if firstLine:
                    firstLine = False
                else:
                    cursor.execute('INSERT INTO Dataset(REF_DATE,GEO,DGUID,Food_categories,Commodity,UOM,UOM_ID,SCALAR_FACTOR,SCALAR_ID,VECTOR,COORDINATE,VALUE,STATUS,SYMBOL,TERMI_NATED,DECIMALS) VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")',
                          row)
        firstLine = True
        #close the connection to the database.
        mydb.commit()
        print("Database Created")
        return 5




    def selctRowFromMysql(rowNumber):#returns a particular row
        try:
            cursor.execute("""
            select * from dataset where ID = {};
            """.format(rowNumber))

            rows = cursor.fetchall()
            return rows
        except:
            print("error occured")


    def deleteRowInDb(rowNumber):#delete selected row
        cursor.execute("""
                DELETE FROM dataset WHERE ID='{}';
                """.format(rowNumber))
        mydb.commit()
        return 5

    #update selected row
    def updateRowInDb(rowNumber,REF_DATE,GEO,DGUID,Food_categories,Commodity,UOM,UOM_ID,SCALAR_FACTOR,SCALAR_ID,VECTOR,COORDINATE,VALUE,STATUS,SYMBOL,TERMI_NATED,DECIMALS):
        cursor.execute("""
                UPDATE dataset SET REF_DATE = "{}",GEO = "{}",DGUID = "{}",Food_categories = "{}",Commodity = "{}",UOM = "{}",UOM_ID = "{}",SCALAR_FACTOR = "{}",SCALAR_ID = "{}",VECTOR = "{}",COORDINATE = "{}",VALUE = "{}",STATUS = "{}",SYMBOL = "{}",TERMI_NATED = "{}",DECIMALS = "{}" WHERE ID = {};
                """.format(REF_DATE, GEO,DGUID, Food_categories, Commodity, UOM, UOM_ID, SCALAR_FACTOR, SCALAR_ID, VECTOR, COORDINATE, VALUE, STATUS, SYMBOL, TERMI_NATED, DECIMALS, rowNumber))
        mydb.commit()
        return 5
    #insert New Record into database
    def insertTheNewData(REF_DATE, GEO, DGUID, Food_categories, Commodity, UOM, UOM_ID, SCALAR_FACTOR,
                                   SCALAR_ID, VECTOR, COORDINATE, VALUE, STATUS, SYMBOL, TERMI_NATED, DECIMALS):
        cursor.execute("""
                        INSERT INTO Dataset(REF_DATE,GEO,DGUID,Food_categories,Commodity,UOM,UOM_ID,SCALAR_FACTOR,SCALAR_ID,VECTOR,COORDINATE,VALUE,STATUS,SYMBOL,TERMI_NATED,DECIMALS) 
                        values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")
                        """.format(REF_DATE, GEO, DGUID, Food_categories, Commodity, UOM, UOM_ID, SCALAR_FACTOR,
                                   SCALAR_ID, VECTOR, COORDINATE, VALUE, STATUS, SYMBOL, TERMI_NATED, DECIMALS))
        mydb.commit()
        return 5



    def closeCursor():
        cursor.close()
        print("Done")
        return 5
