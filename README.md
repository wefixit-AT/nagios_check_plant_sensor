nagios_check_plant_sensor
=========================

More informations see https://blog.wefixit.at/plant-monitoring-v0-1

Example: NRPE
-------------

command[check_plant1_moisture]=/opt/nagios_check_plant_sensor.git/check_plant_sensor.py --mac C4:7C:8D:6B:7C:3D --sensor moisture -w 32 -c 25
command[check_plant1_battery]=/opt/nagios_check_plant_sensor.git/check_plant_sensor.py --mac C4:7C:8D:6B:7C:3D --sensor battery -w 90 -c 80
command[check_plant1_temperature]=/opt/nagios_check_plant_sensor.git/check_plant_sensor.py --mac C4:7C:8D:6B:7C:3D --sensor temperature -w 25 -c 20
