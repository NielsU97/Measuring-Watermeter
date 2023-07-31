<br>
  <h1 align="center">NPN Water Level Sensor Integration with Home Assistant</h1>
  <br>
 <h2 align="center">
<img src="https://github.com/NielsU97/Measuring-Watermeter/blob/main/www/Images/watermeter_example.jpg" width="300">
  </br>
</br>  
<h2>	                                                                                                                                     
<h2> Connecting sensor to Raspberry Pi </h2> 
<br>Text
</br>
</br>
<img src=https://github.com/NielsU97/Measuring-Watermeter/blob/main/www/Images/connecting_sensor.png width="300"> 
</br>
<br>

<h2> Reading sensor data</h2> 
<br>Text
</br>
<br>

<h2> Integration with Home Assistant</h2> 

`configuration.yaml`
<br>

```
sensor:    
    - platform: file
      name: water_meterstand
      file_path: /config/www/meterstand_water.txt
      value_template: '{{ value }}'
      unit_of_measurement: "L"
    - platform: template
      sensors:  
        water_total:
          device_class: water
          value_template: >-
            {% set water = states('sensor.water_meterstand') | int %}
            {{water / 1000}}
          unit_of_measurement: "m3"
```
<br>
<br>
<img src=https://github.com/NielsU97/Measuring-Watermeter/blob/main/www/Images/hass_water_graph.png width="300"> 

