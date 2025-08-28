# Bme280
Otto version
Hej!

Före du kör koden så kör först
sudo apt update
sudo apt install python3-smbus python3-pip python3-bme280 i2c-tools
pip install smbus2 RPi.bme280

Kolla också om sensorn hittas av Beagle boarden med
sudo i2cdetect -y 2
eller om inget syns i 0x76 så
sudo i2cdetect -y -r 2


import smbus2
import bme280
import time

Sensoradress (från i2cdetect)
address borde vara = 0x76

#Initiera I2C-buss 2 
bus = smbus2.SMBus(2)

Initiera BME280
calibration_params = bme280.load_calibration_params(bus, address)

# här kommer koden (Rå kod som går att klistra in finns i en annan fil)
import smbus2    # Bibliotek för att kommunicera via I2C-protokollet
import bme280    # Bibliotek för att läsa data från BME280-sensor
import time      # Bibliotek för att kunna pausa programmet

address = 0x76   # Sensoradress från i2cdetect (hex-format)

bus = smbus2.SMBus(2) # Initierar I2C-buss nummer 2 (byt till 1 om du använder /dev/i2c-1)

calibration_params = bme280.load_calibration_params(bus, address)  # Läser kalibreringsdata från sensorn

try:
    while True:  # Loopar för att läsa data kontinuerligt
        data = bme280.sample(bus, address, calibration_params)  # Hämtar mätdata från sensorn
        print(f"Temperatur: {data.temperature:.1f} °C")         # Skriver ut temperatur med 1 decimal
        print(f"Luftfuktighet: {data.humidity:.1f} %")          # Skriver ut luftfuktighet med 1 decimal
        print(f"Lufttryck: {data.pressure:.1f} hPa")            # Skriver ut lufttryck med 1 decimal
        print("-------------------------------")               # Avskiljare för tydlighet
        time.sleep(0.5)  # Väntar 0,5 sekunder innan nästa mätning
except KeyboardInterrupt:  # Om användaren trycker Ctrl+C
    print("Avslutar...")   # Skriver ut avslutningsmeddelande
finally:
    bus.close()


<img width="1207" height="1296" alt="image" src="https://github.com/user-attachments/assets/9326a83c-2ecb-4cb6-b5e4-7edbbde552de" />
