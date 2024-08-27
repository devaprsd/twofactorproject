import mysql.connector 
def pusher(name,username,email,imagepath,password):
    mydb = mysql.connector.connect( host="localhost",user="facey",password="aki!@#123",database="facey")
    print (mydb)
    mycursor=mydb.cursor()
    sql = "INSERT INTO userbase (name, username , email , imagepath , password) VALUES (%s, %s,%s,%s,%s)"
    val = (name,username,email,imagepath,password)  
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()
def checker(username):
    mydb = mysql.connector.connect( host="localhost",user="facey",password="aki!@#123",database="facey")
    print (mydb)
    mycursor=mydb.cursor()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM userbase")
    myresult = mycursor.fetchall()
    for x in myresult:
        if x[1]==username:
            return True
    return False
    mydb.close()
def password(username):
    mydb = mysql.connector.connect( host="localhost",user="facey",password="aki!@#123",database="facey")
    print (mydb)
    mycursor=mydb.cursor()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM userbase")
    myresult = mycursor.fetchall()
    for x in myresult:
        if x[1]==username:
            return x[4]
        else:
            None
    mydb.close()
def imagepath(username):
    mydb = mysql.connector.connect( host="localhost",user="facey",password="aki!@#123",database="facey")
    mycursor=mydb.cursor()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM userbase")
    myresult = mycursor.fetchall()
    for x in myresult:
        if x[1]==username:
            return x[3]
        else:
            None
    mydb.close()
def usermail(username):
    mydb = mysql.connector.connect( host="localhost",user="facey",password="aki!@#123",database="facey")
    mycursor=mydb.cursor()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM userbase")
    myresult = mycursor.fetchall()
    for x in myresult:
        if x[1]==username:
            return x[2]
        else:
            None
    mydb.close()
