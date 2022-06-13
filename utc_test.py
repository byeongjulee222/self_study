import logging
import pymysql
import sys
import datetime
from django.utils import timezone


host = "localhost"
port = 3306
database = "test"
username = "root"
password = "1234"

def main():
    try:
        conn = pymysql.connect(host=host, user=username, passwd=password, db=database, port=port, use_unicode=True, charset='utf8', unix_socket='/tmp/mysql.sock')
        cursor = conn.cursor()
    except:
        logging.error("connection error")
        sys.exit(1)

    default_time = datetime.datetime.now()
    # print(default_time.date())
    # query = f"INSERT INTO new_table (time_zone) VALUE ('{default_time}')"
    query = f"SELECT time_zone FROM new_table"
    cursor.execute(query)
    data = cursor.fetchall()[0][0]
    print(data)
    print(type(data))
    print(datetime.datetime.utcnow())
    print(type(datetime.datetime.utcnow()))

    date = datetime.datetime.now(timezone.utc)
    print(date.strftime('%Y-%m-%d %H:%M:%S %Z %z'))
    print(date.astimezone().strftime('%Y-%m-%d %H:%M:%S %Z %z'))

    conn.commit()

    conn.close()

if __name__=='__main__':
    main()