import sqlite3

DATABASE = "wifistatus.sql"

def init_db():
    conn = sqlite3.connect(DATABASE)
    conn.execute("CREATE TABLE IF NOT EXISTS WIFISESSIONS (device_number INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL,connection_status TEXT CHECK(connection_status IN ('CONNECTED', 'QUEUING', 'DISCONNECTED')) NOT NULL DEFAULT 'QUEUING');")
    conn.commit()
    conn.close()


def connected_user():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM WIFISESSIONS WHERE connection_status = 'CONNECTED';")
    count = cursor.fetchone()[0]
    conn.close()
    return count

def add_user(username, active_status = 'CONNECTED'):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    if active_status == 'CONNECTED':
        if connected_user() >= 3:
            cursor.execute("UPDATE WIFISESSIONS SET connection_status = 'DISCONNECTED' WHERE device_number = (SELECT device_number FROM WIFISESSIONS  WHERE connection_status = 'CONNECTED' ORDER BY device_number ASC LIMIT 1);")
        FINAL_STATUS = 'CONNECTED'
    else:
        FINAL_STATUS = 'QUEUING'
    cursor.execute("INSERT INTO WIFISESSIONS (username, connection_status) VALUES (?, ?);", (username, FINAL_STATUS))
    conn.commit()
    conn.close()

def ALL_user():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT device_number, username, connection_status FROM WIFISESSIONS ORDER BY device_number ASC;")
    rows = cursor.fetchall()
    conn.close()
    return rows


def display_queue():
    all_connection = ALL_user()
    connected_count = connected_user()
    print("\n ---------------------- CURRENT CONNECTION STATUS LOG -----------------------")
    print("\n ----------------- Only 3 people can be connected at a time  ----------------")
    print(f"{'DEVICE NUMBER':<30} | {'DEVICE NAME':<30} | {'STATUS':<15}")
    for row in all_connection:
        print(f"(imagine personal data)-{row[0]:<6} | {row[1]:<30} | {row[2]:<15}")
    print("-----------------------------------------------------------------------------\n")


init_db()
print("FREE 5G WIFI, DEFINETLY NO CONSEQUENCES. CONNECT NOW!")
name = input("Enter your name/Device name: ")

confirm = input(f"Would you like to connect (y/n) [invalid input are not allowed]: ").strip()

if confirm == "y":
    add_user(name, 'CONNECTED')
else:
    add_user(name, 'QUEUING')

display_queue()
