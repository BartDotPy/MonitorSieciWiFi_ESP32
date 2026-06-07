# Monitor Sieci WiFi (ESP32)

Podstawowa wersja programu do skanowania mocy sieci i reprezentacji graficznej otrzymanych danych. Program będzie rozbudowany o rozpoznawanie lokalizacji na podstawie nadajników BLE, tworzenie heatmapy poziomu mocy, bezprzewodowe połączenie oraz sprawdzanie innych parametrów sygnału.

## Wymagania
* Płytka mikrokontrolera **ESP32**.
* Środowisko (np. Arduino IDE) do wgrania skryptu `.ino`.
* Środowisko Python z zainstalowaną biblioteką Streamlit (oraz ewentualnie inne, np. pyserial).

## Jak uruchomić

**1. Konfiguracja sprzętu:**
Upewnij się, że skrypt `ESP_scan.ino` (z folderu `ESP_scan`) został wgrany na Twoją płytkę ESP32.

**2. Połączenie z płytką:**
Uruchom skrypt pośredniczący, który nawiąże połączenie z ESP32:
`bash
python bridge.py
`

**3. Uruchomienie interfejsu graficznego:**
Otwórz wiersz poleceń w lokalizacji folderu i wpisz poniższą komendę, aby uruchomić GUI (Streamlit):
`bash
python -m streamlit run dashboard.py
`)

<img width="1858" height="716" alt="image" src="https://github.com/user-attachments/assets/4ea1ace9-9430-4d67-a951-ba588a03c1cc" />


## Plany rozwoju (To-Do)
* Wdrożenie rozpoznawania lokalizacji na podstawie nadajników BLE (zrealizowane w innym projekcie - dokładność lokalizacji na poziomie +- 3m).
* Generowanie heatmapy poziomu mocy sygnału.
* Obsługa połączenia bezprzewodowego.
* Sprawdzanie i wizualizacja dodatkowych parametrów sygnału.
