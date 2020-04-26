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

# select...
# cnx = mysql.connector.connect(user='scott', database='employees')
# cursor = cnx.cursor()
#
# query = ("SELECT first_name, last_name, hire_date FROM employees "
#          "WHERE hire_date BETWEEN %s AND %s")
#
# hire_start = datetime.date(1999, 1, 1)
# hire_end = datetime.date(1999, 12, 31)
#
# cursor.execute(query, (hire_start, hire_end))
#
# for (first_name, last_name, hire_date) in cursor:
#     print("{}, {} was hired on {:%d %b %Y}".format(
#         last_name, first_name, hire_date))


cnx.commit()

cursor.close()
cnx.close()
