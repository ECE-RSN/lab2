#!/usr/bin/env python3

import serial
import sys
import time

def convertGPGGA2latlon(nmea_list):
    nmea_header = nmea_list[0]
    utc = float(nmea_list[1])
    lat = float(nmea_list[2])
    northDirection = nmea_list[3]
    lon = float(nmea_list[4])
    eastDirection = nmea_list[5]
    num_sats = nmea_list[7]
    HDOP = nmea_list[8]
    altitude = float(nmea_list[9])
    alt_unit = nmea_list[10]

    gnss_info = [lat, lon, altitude, utc, HDOP]
    return gnss_info
    
def publish():
    gnss_port = serial.Serial("/dev/pts/2", baudrate=4800, bytesize=8, timeout=1, stopbits=1)
    
    while True:
        nmea_bytes = gnss_port.readline()
        nmea_string = nmea_bytes.decode('utf-8')
        nmea_list = nmea_string.split(",")

        if "GNGGA" in nmea_list[0]:
            print(nmea_string)
            gnss_info = convertGPGGA2latlon(nmea_list)  
        time.sleep(1/13)
        
if __name__ == '__main__':

    try:
        publish()
    except:
        pass

