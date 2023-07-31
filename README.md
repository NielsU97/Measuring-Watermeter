<br>
  <h1 align="center">NPN Sensor Water Consumption Integration with Home Assistant</h1>
  <br>
 <h2 align="center">
<img src="https://github.com/NielsU97/Measuring-Watermeter/blob/main/www/Images/watermeter_example.jpg" width="300">
  </br>
</br>  
<h2>	                                                                                                                                     
<h2> Connecting sensor to Raspberry Pi </h2> 
Hardware needed:
<ol>
  - LJ12A3-4-Z/Bx Inductieve Proximity (NPN) Sensor <br>
  - Logic Level Converter 5V to 3.3V <br>
  - 10k resistor <br>
</ol>
</br>
</br>
<img src=https://github.com/NielsU97/Measuring-Watermeter/blob/main/www/Images/connecting_sensor.png width="300"> 
</br>
<br>

<h2> Reading sensor data</h2> 
The python script "watermeter.py" reads the sensor and write the number of rotations to a txt file. If the red pointer has made a full lap it equals one litre and has passed the sensor once.
</br>
<br>

<h2> Integration with Home Assistant</h2> 

`configuration.yaml` - Add the following lines in your configuration.yaml
<br>

```
sensor:    
  - platform: file
    name: Water Meterstand
    file_path: /config/www/meterstand_water.txt
    value_template: '{{ value }}'
    unit_of_measurement: "L"

template:
  - sensor:
    - name: "Water Consumption"
      unique_id: "water_consumption_total"
      device_class: water
      state_class: total_increasing
      state: >-
         {% set value = states('sensor.water_meterstand') | int %}
         {{value}}
      unit_of_measurement: "L"
```
<br>
The entity "Water Consumption" can be used to add it to your Energy Dashboard.
<br>
<br>
<img src=https://github.com/NielsU97/Measuring-Watermeter/blob/main/www/Images/hass_water_meterstand.png width="300"> 
<br>
<br>
<img src=https://github.com/NielsU97/Measuring-Watermeter/blob/main/www/Images/hass_energy_dashboard.png width="300"> 