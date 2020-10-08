#!/usr/bin/env python3

import argparse
import sys

from btlewrap.gatttool import GatttoolBackend
from miflora.miflora_poller import (
    MI_BATTERY,
    MI_CONDUCTIVITY,
    MI_LIGHT,
    MI_MOISTURE,
    MI_TEMPERATURE,
    MiFloraPoller,
)

def main():
    parser = argparse.ArgumentParser(description='Check values against a plant sensor')
    parser.add_argument('--mac', required=True,
        help='mac of the sensor. Run "hcitool lescan" and search for "Flower care"')
    parser.add_argument('--sensor', required=True,
        help='Available sensors: battery, conductivity, moisture, temperature, light')
    parser.add_argument('-w', required=True, type=float,
        help='Warning value')
    parser.add_argument('-c', required=True, type=float,
        help='Critical value')

    args = parser.parse_args()
    
    poller = MiFloraPoller(args.mac, GatttoolBackend)
    value = -1
    text = "OK"
    return_value = 0
    
    if args.sensor == "battery":
        value = poller.parameter_value(MI_BATTERY);
    if args.sensor == "conductivity":
        value = poller.parameter_value(MI_CONDUCTIVITY);
    if args.sensor == "moisture":
        value = poller.parameter_value(MI_MOISTURE);
    if args.sensor == "temperature":
        value = poller.parameter_value(MI_TEMPERATURE);
    if args.sensor == "light":
        value = poller.parameter_value(MI_LIGHT);

    if value < args.w:
        text = "WARNING"
        return_value = 1
    
    if value < args.c:
        text = "CRITICAL"
        return_value = 2


    print(text + " - " + args.sensor + " = " + str(value) + " |" + args.sensor + "=" + str(value) + ";" + str(args.w) + ";" + str(args.c) + ";0")
    sys.exit(return_value)
    
if __name__ == "__main__":
    main()
