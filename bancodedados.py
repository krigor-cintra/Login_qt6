import mysql.connector

try:

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="admin",
        database="programa1"
    )
except mysql.connector.Error as erro:
    print(erro)

mycursor = mydb.cursor()

def login_creat(email,senha):
    mycursor.execute("insert into login (email , senha0) values('%s','%s')"),email,senha
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")



def login(email,senha):
    mycursor.execute(f"SELECT email from programa1.login  where email like '{email}'")
    result=mycursor.fetchall()
    if result != []:
        mycursor.execute(f"SELECT senha0 from programa1.login  where email like '{email}'")
        result = mycursor.fetchall()
        if str(result[0]==senha):
            print("login sucess")