import psycopg2
import psycopg2.extras
import csv
import os

database_ = psycopg2.connect(host=os.environ["HOST_IP"], dbname=os.environ["DB_NAME"],
                             user=os.environ["USERNAME"], password=os.environ["PASSWORD"])
cursor = database_.cursor()

cursor.execute("SELECT * FROM {}".format(os.environ["TABLE_NAME"]))
data = cursor.fetchmany(1000)

#print(data[39])

with open("lalouiga.csv", "w") as lalouiga:
    csv_writer = csv.writer(lalouiga)
    csv_writer.writerow([i[0] for i in cursor.description])

with open("lalouiga.csv", "a") as lalouiga:
    csv_writer.writerows(data)

#print(cursor.description)

database_.close()
cursor.close()