import smbus2
import bme280

# Använd rätt bussnummer – byt vid behov
bus = smbus2.SMBus(2)
address = 0x76

# Läs in kalibreringsdata
calibration_params = bme280.load_calibration_params(bus, address)

# Ta ett prov och skriv ut
data = bme280.sample(bus, address, calibration_params)
print(f"Temperatur: {data.temperature:.1f} °C")
print(f"Luftfuktighet: {data.humidity:.1f} %")
print(f"Lufttryck: {data.pressure:.1f} hPa")
