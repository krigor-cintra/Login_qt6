import mysql.connector

try:

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="admin",
        database="programa1"
    )

    mycursor = mydb.cursor()

except mysql.connector.Error as erro:
    print(erro)




def login_creat(email,senha):
    try:
        mycursor.execute(f"insert into login (email , senha0) values('{email}','{senha}')")
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    except mysql.connector.Error as erro:
        print(erro)



def login(email,senha):
    try:
        mycursor.execute(f"SELECT email from programa1.login  where email like '{email}'")
        result=mycursor.fetchall()
        if result != []:
            mycursor.execute(f"SELECT senha0 from programa1.login  where email like '{email}'")
            result = mycursor.fetchall()
            if str(result[0]==senha):
                print("login sucess")
    except mysql.connector.Error as erro:
        print(erro)


