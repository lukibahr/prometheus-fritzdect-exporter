# Prometheus exporter for FRITZ!Dect devices

Prometheus Endpoint, written in Python to read FRITZ!Dect devices and export values as prometheus metrics. [![Build Status](https://ci.devopoly.de/api/badges/lukibahr/raspbi-temperature-exporter/status.svg)](https://ci.devopoly.de/lukibahr/raspbi-temperature-exporter)

## Prerequisites - Creating the FRITZ!Box User

### 1. Creating a user account with the right to configure FRITZ!Box settings  
Create at least one user account that you can access the FRITZ!Box settings with:  
1. Click "System" in the FRITZ!Box user interface. 
2. Click "FRITZ!Box Users" in the "System" menu. 
3. Click the "Add User" button. 
4. Enable the option "User account enabled". 
5. Enter a user name, a valid email address, and a password for the user. 
6. Enable the option "Access from the internet allowed" if the user may also access the FRITZ!Box over the internet. 
7. Enable the option "FRITZ!Box settings" under "Rights". You can assign additional rights according to your individual needs. 
8. Click "OK" to save the settings. 

### 2. Setting up users with restricted authorization
1. Click "System" in the FRITZ!Box user interface. 
2. Click "FRITZ!Box Users" in the "System" menu. 
3. Click the "Add User" button. 
4. Enable the option "User account enabled". 
5. Enter a user name, a valid email address, and a password for the user. 
6. Enable the option "Access from the internet allowed" if the user may also use the FRITZ!Box services for which he is authorized over the internet. 
7. Disable the option "FRITZ!Box settings" under "Rights" because otherwise the user can access all of the settings. 
8. Assign additional rights according to the individual needs of the user. 
9. Click "OK" to save the settings.

### 3. Enabling login to the home network with user name and password
After you have created the users with the desired rights, enable login to the home network with the user accounts:  
1. Click "System" in the FRITZ!Box user interface 
2. Click "FRITZ!Box Users" in the "System" menu. 
3. Click on the "Login to the Home Network" tab. 
4. Enable the option "Login with FRITZ!Box user name and password". 
5. Click "Apply" to save the settings. 

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