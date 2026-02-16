import serial
import sqlite3
from datetime import datetime
import time

#funkcja do tworzenia/zapisu bazy
def to_db():
    conn = sqlite3.connect('wifi_data.db')
    c = conn.cursor()
    #tworzymy dwie tabele - dane i komendy
    c.execute('''CREATE TABLE IF NOT EXISTS scans
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              ssid TEXT,
              rssi INTEGER,
              timestamp DATETIME)''')
    c.execute('''CREATE TABLE IF NOT EXISTS commands 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, cmd TEXT)''')
    conn.commit()
    return conn

#polaczenie z ESP
def esp_connection():
   
    conn = to_db()
    cursor = conn.cursor()

    print("Proba polaczenia z ESP32")
    try:
        COM_ADR = 'COM9'
        ser = serial.Serial(COM_ADR, 115200) #ustawić nasze parametry
        print(f'Polaczone z ESP na {COM_ADR}')
    except Exception as e:
        print(f'Nieudana próba: {e}')
    while True:
        try:
            #sprawdzamy liczbe bajtow w buforze
            if ser.in_waiting > 0:
                #odbieranie danych od ESP
                line = ser.readline().decode('utf-8').strip()
                
                #szukamy seperatora
                if "|" in line:
                    ssid, rssi = line.split("|")
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    cursor.execute('INSERT INTO scans (ssid,rssi,timestamp) VALUES (?,?,?)', (ssid, int(rssi), now))

                    conn.commit()
                    print("ZAPISANO POMIAR")
    
            #wysylanie danych do ESP
            cursor.execute("SELECT id, cmd FROM commands LIMIT 1")
            row = cursor.fetchone()
            if row:
                cmd_id, cmd_text = row
                cursor.execute("DELETE FROM scans") #czyscimy dotychczasowe pomiary
                ser.write(f"{cmd_text}\n".encode('utf-8')) # Wysyła "SCAN\n"
                cursor.execute("DELETE FROM commands WHERE id = ?", (cmd_id,))
                conn.commit()
                print(f"Wysłano do ESP: {cmd_text}")
        except Exception as e:
            print(f'WYSTAPIL BLAD W PETLI PRZESYLU! {e}')
        time.sleep(0.05)

if __name__ == "__main__":
    esp_connection()