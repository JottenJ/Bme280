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

# Sensoradress (från i2cdetect)
address = 0x76

# Initiera I2C-buss 2 (byt till 1 om det är /dev/i2c-1)
bus = smbus2.SMBus(2)

# Initiera BME280
calibration_params = bme280.load_calibration_params(bus, address)


