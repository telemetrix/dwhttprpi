import time

import serial
import pynmea2
from geopy.distance import geodesic

serial_port = '/dev/tty.usbserial-AL01HX1H'
ser = serial.Serial(
    port=serial_port,
    baudrate=19200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
)

def get_position(sentence='$GNRMC'):
    with serial.Serial('/dev/tty.usbserial-A702G71L', baudrate=9600, timeout=1) as ser:
        try:
            while 1:
                nmea = ''
                while 1:
                    line = ser.readline().decode('ascii', errors='replace')
                    if line.find(sentence) != -1:
                        nmea = line
                        break

                nmea_obj = pynmea2.parse(nmea)
                return (1, nmea_obj.is_valid, nmea_obj.status, nmea_obj.latitude, nmea_obj.lat_dir,
                        nmea_obj.longitude, nmea_obj.lon_dir, nmea_obj.spd_over_grnd, nmea_obj.true_course,
                        nmea_obj.datestamp, nmea_obj.timestamp, nmea_obj.mag_variation, nmea_obj.mag_var_dir)

        except Exception as e:
            return (0, e)

gw_position = (50.023756, 20.908174)

while 1:
    nmea = get_position()
    print(nmea)

    pos = (float(nmea[3]), float(nmea[5]))
    print(geodesic(gw_position, pos).kilometers)

    time.sleep(5)