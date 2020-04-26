from datetime import datetime, timedelta, date

import mysql.connector

cnx = mysql.connector.connect(user='sasaro', password='sasaro2020',
                              host='ec2-18-188-30-68.us-east-2.compute.amazonaws.com',
                              database='sasaro')

cursor = cnx.cursor()

tomorrow = datetime.now().date() + timedelta(days=1)

add_member = ("INSERT INTO tbl_member "
                "(member_id, name, nationality, reg_date, agreement) "
                "VALUES (%s, %s, %s, %s, %s)")

data_member = ('test@test.com', '테스트', 'vietnam', date(1977, 6, 14), 1)
emp_no = cursor.lastrowid

cursor.execute(add_member, data_member)

cnx.commit()

cursor.close()
cnx.close()
