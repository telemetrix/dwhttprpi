import time
import os

import psutil
import serial
from TR50 import TR50http


serial_port = '/dev/tty.usbserial-AL01HX2M'
ser = serial.Serial(
    port=serial_port,
    baudrate=19200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    timeout=5.0
)

dw_config = {
        'endpoint': 'http://api-de.devicewise.com/api',
        'app_id': '0000001', # it has to be locked ID value for each logic device. (generating from serial numbers?)
        'app_token': 'hzFldHm60s4vaYzW',
        'thing_key': 'wmbus169_concentrator_01'
    }

tr50http = TR50http.TR50http(dw_config)

pid = os.getpid()
ps = psutil.Process(pid)

while 1:
    rcv = ser.read(128).decode('utf-8')
    if rcv.__len__() > 0:
        memoryUse = ps.memory_info()[0]
        result = tr50http.execute('property.publish', {'key': 'rss', 'value': memoryUse})
        print(tr50http.get_response())
        result = tr50http.execute('log.publish', {'msg': rcv})
        print(tr50http.get_response())
        print(rcv)

