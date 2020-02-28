#!/usr/bin/env python
"""
Prometheus running in kubernetes will automatically scrape this service.
"""

import time
import argparse
import logging
import socket
from fritzconnection.lib.fritzhomeauto import FritzHomeAutomation
from prometheus_client.core import GaugeMetricFamily, REGISTRY
from prometheus_client import start_http_server

LOGFORMAT = "%(asctime)s - %(levelname)s [%(name)s] %(threadName)s %(message)s"

class CustomCollector():
    """
    Class CustomCollector implements the collect function
    """
    def __init__(self, node=None, address=None, user=None, password=None, device_ain=None):
        self.address = address
        self.user = user
        self.password = password
        self.device_ain = device_ain
        self.node = node
        self.fha = FritzHomeAutomation(address=self.address, user=self.user, password=self.password)

    def collect(self):
        """collect collects the metrics"""
        device_name = self.fha.get_device_information_by_identifier(self.device_ain)\
            ['NewDeviceName']
        temperature = self.fha.get_device_information_by_identifier(self.device_ain)\
            ['NewTemperatureCelsius'] * 0.1
        powerconsumption = self.fha.get_device_information_by_identifier(self.device_ain)\
            ['NewMultimeterEnergy']
        power = self.fha.get_device_information_by_identifier(self.device_ain)\
            ['NewMultimeterPower'] / 100
        switchstate = self.fha.get_device_information_by_identifier(self.device_ain)\
            ['NewSwitchState']

        logging.debug(self.fha.get_device_information_by_identifier(self.device_ain))
        t = GaugeMetricFamily('fritzdect_temperature', 'Temperature measured in celcuis',
                              labels=['node', 'device_name', 'ain'])
        w = GaugeMetricFamily("fritzdect_current_powerconsumption",
                              "Current power consumption in watts",
                              labels=['node', 'device_name', 'ain'])
        p = GaugeMetricFamily("fritzdect_total_powerconsumption",
                              "Total power consumption in watts per year",
                              labels=['node', 'device_name', 'ain'])
        s = GaugeMetricFamily("fritzdect_switch_state", "The current state of the switch",
                              labels=['node', 'device_name', 'ain', 'value'])

        t.add_metric([self.node, device_name, self.device_ain], temperature)
        p.add_metric([self.node, device_name, self.device_ain], powerconsumption)
        w.add_metric([self.node, device_name, self.device_ain], power)
        s.add_metric([self.node, device_name, self.device_ain, switchstate], 0)
        return p, w, t, s

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Prometheus Fritz!DECT exporter')
    parser.add_argument('-n', '--node', type=str,
                        help='The node, the exporter runs on', default=socket.gethostname())
    parser.add_argument('-p', '--port', type=int,
                        help='The port, the exporter runs on', default=9123)
    parser.add_argument('-i', '--interval', type=int,
                        help='The sleep interval of the exporter', default=120)
    parser.add_argument('-a', '--ain', type=str,
                        help='The Aktor Identifikationsnummer (AIN) which identifies the device',
                        default='00000 0000000')
    parser.add_argument('-l', '--loglevel',
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help='Set the logging level')
    parser.add_argument('-w', '--password', type=str,
                        help='The password to authenticate the FRITZ!Box', default='password')
    parser.add_argument('-f', '--address', type=str,
                        help='The address of the FRITZ!Box', default='192.168.178.1')
    parser.add_argument('-u', '--user', type=str,
                        help='The user to authenticate the FRITZ!Box', default='user')
    args = parser.parse_args()
    if args.loglevel:
        logging.basicConfig(level=getattr(logging, args.loglevel), format=LOGFORMAT)
    logging.debug("Parsing command line arguments: %s", args)
    logging.info("Running exporter on port %s", args.port)
    start_http_server(args.port)
    REGISTRY.register(CustomCollector(args.node, args.address, args.user, args.password, args.ain))
    while True:
        logging.debug("Sleeping for %s seconds", args.interval)
        time.sleep(args.interval)
