import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="WiFi Scanner Dashboard", layout="wide")

st.title("Monitor Sieci WiFi (ESP32)")


def request_scan():
    conn = sqlite3.connect('wifi_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO commands (cmd) VALUES ('SCAN')")
    conn.commit()
    conn.close()
    return df

def get_data():
    conn = sqlite3.connect('wifi_data.db')
    df = pd.read_sql_query("SELECT * FROM scans ORDER BY timestamp DESC", conn)
    conn.close()
    return df

def clear_scan():
    conn = sqlite3.connect('wifi_data.db')
    c = conn.cursor()
    c.execute('DELETE FROM scans')
    conn.commit()
    conn.close()
    return df

# Wyświetlanie danych
df = get_data()

with st.sidebar:
    st.header("Opcje")
    if st.button('Uruchom Skanowanie', use_container_width=True):
        request_scan() #wysylanie prosby do esp
        st.toast("Zlecono skanowanie...")
    if st.button('Wyczyść baze', use_container_width=True):
        clear_scan()
        st.toast('Zlecono czyszczenie')
    



if not df.empty:
    # Statystyki
    c1, c2 = st.columns(2)
    c1.metric("Znalezione sieci", len(df['ssid'].unique()))
    c2.metric("Najlepszy sygnał", f"{df['rssi'].max()} dBm")

    # Wykres i Tabela
    tab1, tab2 = st.tabs(["Wykres sygnału", "Surowe dane"])
    with tab1:
        st.bar_chart(df.set_index('ssid')['rssi'])
    with tab2:
        st.dataframe(df, use_container_width=True)
else:
    st.info("Baza danych jest pusta. Kliknij 'Uruchom Skanowanie' w panelu bocznym.")

if st.button('Odśwież dane'):
    st.rerun()