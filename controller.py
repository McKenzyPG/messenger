def ftp_send():

    host = "your_host"
    ftp_user = "login"
    ftp_password = "password"
    filename = "image.jpg"

    con = ftplib.FTP(host, ftp_user, ftp_password)
    file = open(filename, "rb")
    send = con.storbinary("STOR " + filename, file)
    con.close()
    file.close()


def sql_save():

     host = "your_host"
    mysql_db = "db_name"
    mysql_user = "login"
    mysql_password = "password"



    try:
        conn = MySQLdb.connect(host, mysql_user, mysql_password, mysql_db)

    except MySQLdb.Error as err:
        print("Connection error: {}".format(err))
        conn.close()

    sql = "INSERT INTO image(file) VALUES('" + filename + "');"

    # conn.autocommit(True)

    try:
        cur = conn.cursor()
        cur.execute(sql)

    except MySQLdb.Error as err:
        print("Query error: {}".format(err))

    conn.commit()

    conn.close()
