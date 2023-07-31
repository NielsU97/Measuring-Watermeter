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
      name: meterstand_water
      file_path: /config/www/meterstand_water.txt
      value_template: '{{ value }}'
      unit_of_measurement: "m3"
```

