Podstawowa wersja programu do skanowania mocy sieci i reprezentacji graficznej otrzymanych danych. Program będzie rozbudowany o rozpoznawanie lokalizacji na podstawie nadajników BLE, tworzenie heatmapy poziomu mocy, bezprzewodowe połączenie oraz sprawdzanie innych parametrów sygnału.

Aby uruchimić program należy za pomocą wiersza poleceń dostać się do lokalizacji folderu i wpisać komendę do uruchomienia GUI (streamlit): py -m streamilt run dashboard.py

Nastepnie należy uruchomić skrypt bridge.py, który połączy się z naszym ESP32 (wczesniej upewnić się czy skrypt ESP_scan.ino został wgrany na płytkę)
