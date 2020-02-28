# Prometheus exporter for FRITZ!Dect devices

Prometheus Endpoint, written in Python to read FRITZ!Dect devices and export values as prometheus metrics. [![Build Status](https://ci.devopoly.de/api/badges/lukibahr/raspbi-temperature-exporter/status.svg)](https://ci.devopoly.de/lukibahr/raspbi-temperature-exporter)

## Prerequisites - Creating the FRITZ!Box User

t.b.d.


## Implementation

Have a look at the sourcecode for details. Generally, you'll have to download and import the required python libraries.
Refer to the official documentation on how to implement a prometheus exporter: https://github.com/prometheus/client_python.

### Development

You'll need to install python (I recommend python3) to prepare your local environment: 

```bash
$ sudo apt-get update
$ sudo apt-get install python3-pip
$ sudo python3 -m pip install --upgrade pip setuptools wheel
$ sudo pip3 install prometheus_client fritzconnection
$ python3 exporter.py --< args[] >
```

### Sample fritzconnection query

```json
{'NewDeviceId': 16,
 'NewFunctionBitMask': 2944, 
 'NewFirmwareVersion': '04.16', 
 'NewManufacturer': 'AVM', 
 'NewProductName': 'FRITZ!DECT', 
 'NewDeviceName': 'FRITZ!DECT',
 'NewPresent': 'CONNECTED',
 'NewMultimeterIsEnabled': 'ENABLED', 
 'NewMultimeterIsValid': 'VALID', 
 'NewMultimeterPower': 0, //current power in watts  Power value [1/100 W] 
 'NewMultimeterEnergy': , //Total consumption over the last year in kWh
 'NewTemperatureIsEnabled': 'ENABLED', 
 'NewTemperatureIsValid': 'VALID', 
 'NewTemperatureCelsius': 200, 
 'NewTemperatureOffset': 0, 
 'NewSwitchIsEnabled': 'ENABLED', 
 'NewSwitchIsValid': 'VALID', 
 'NewSwitchState': 'OFF', //switch state
 'NewSwitchMode': 'MANUAL', 
 'NewSwitchLock': False, 
 'NewHkrIsEnabled': 'DISABLED', 
 'NewHkrIsValid': 'INVALID', 
 'NewHkrIsTemperature': 0, 
 'NewHkrSetVentilStatus': 'CLOSED', 
 'NewHkrSetTemperature': 0, 
 'NewHkrReduceVentilStatus': 'CLOSED', 
 'NewHkrReduceTemperature': 0, 
 'NewHkrComfortVentilStatus': 'CLOSED', 
 'NewHkrComfortTemperature': 0
 }
```

## Running in docker

I've used hypriot os with a RaspberryPi 3B+. It works on a Raspberry Pi 2 too, although docker builds might take some time, so be calm to your Pi.

```bash
usage: exporter.py [-h] [-n NODE] [-p PORT] [-i INTERVAL] [-a AIN]
                   [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-w PASSWORD]
                   [-f ADDRESS] [-u USER]

Prometheus Fritz!DECT exporter

optional arguments:
  -h, --help            show this help message and exit
  -n NODE, --node NODE  The node, the exporter runs on
  -p PORT, --port PORT  The port, the exporter runs on
  -i INTERVAL, --interval INTERVAL
                        The sleep interval of the exporter
  -a AIN, --ain AIN     The Aktor Identifikationsnummer (AIN) which identifies
                        the device
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --loglevel {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set the logging level
  -w PASSWORD, --password PASSWORD
                        The password to authenticate the FRITZ!Box
  -f ADDRESS, --address ADDRESS
                        The address of the FRITZ!Box
  -u USER, --user USER  The user to authenticate the FRITZ!Box
```

## Building and running

You can run the exporter either via python itself or in a docker container. The required commands for running it via python are 
also in the supplied Makefile. For docker use:

```bash
t.b.d
```

or refer to the supplied Makefile.

You can also download it from docker hub via `docker pull lukasbahr/...`

## Open ToDo's

- :heavy_check_mark: Add CI/CD Support
- :x: Add unit tests
- :x: use buildx to create the proper image
- :x: Add health metric, error metric, scrape interval, general information about exporter etc.

## Further reading

- https://avm.de/fileadmin/user_upload/Global/Service/Schnittstellen/x_homeauto.pdf