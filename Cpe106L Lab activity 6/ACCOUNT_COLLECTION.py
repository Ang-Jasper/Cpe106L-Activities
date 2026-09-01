import psycopg2

from Lab_activity6 import  profit, suckers_account, bet

print(f"\nADMIN PANEL")
conn = psycopg2.connect(
    dbname="gambling_addicts",
    user="postgres",
    password="SCAMMING69!",
    host="127.0.0.1",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS user_records (suckers_account VARCHAR(100) NOT NULL, bet NUMERIC(10,2) NOT NULL, profit NUMERIC(10,2) NOT NULL);")
cursor.execute("INSERT INTO user_records (suckers_account, bet, profit) VALUES (%s, %s, %s);",(suckers_account, bet, profit))
conn.commit()
cursor.execute("SELECT suckers_account, bet, profit FROM user_records;")
records = cursor.fetchall()

print("\n ---------------------- GATHERED ACCOUNT LOG -----------------------")
print("\n -------------------------------- ONLY SERVER OWNER CAN SEE HEHE  --------------------------------")
print(f"{'ACOUNT NAME':<30} | {'THEIR BET  ':<20} | {'THEIR PROFIT':<20} | {'OUR PROFITS:':<30}")
print("----------------------------------------------------------------------------------------------------")
for record in records:
    print(f"{record[0]:<30} | {float(record[1]):<20.2f} | {float(record[2]):<20.2f} | {float(record[1] - record[2]):<20.2f}")
print("-----------------------------------------------------------------------------------------------------\n")

cursor.close()
conn.close()
print("\n-connection closed. Account collected HEHEHE-")