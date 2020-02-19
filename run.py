import psycopg2
import psycopg2.extras
import csv
import os

database_ = psycopg2.connect(host=os.environ["HOST_IP"], dbname=os.environ["DB_NAME"],
                             user=os.environ["USERNAME"], password=os.environ["PASSWORD"])
cursor = database_.cursor()

cursor.execute("SELECT * FROM {}".format(os.environ["TABLE_NAME"]))
data = cursor.fetchmany(1000)

file_name = str("csv/" + os.environ["CSV_NAME"] + ".csv")
print(file_name)

with open(file_name, "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description])

while (data):
    with open(file_name, "a") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(data)
    data = cursor.fetchmany(1000)

database_.close()
cursor.close()