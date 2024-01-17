import mysql.connector

def main():
    mydb = mysql.connector.connect(
        host="db",       # 数据库主机地址
        user="root",    # 数据库用户名
        passwd="730403"   # 数据库密码
    )
    
    mycursor = mydb.cursor()

    # //创建数据库
    # mycursor.execute("CREATE DATABASE runoob_db")

    # 打印所有数据库名称
    mycursor.execute("SHOW DATABASES")
    
    for x in mycursor:
        print(x)

if __name__ == '__main__':
    main()

