# FLASKTEST DRONE POC
A basic flask application with drone integration in Swatchgroup infrastructure.
Some configuration should be respected to work with PaloaAlto Firewall and transparent proxy configuration.


.drone.yaml configuration must integrate Swatchgroup DNS as google dns are avoid in Firewall rules
```
custom_dns: ['10.139.3.10','10.139.3.11']
```


