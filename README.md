# Waste collection - Home Assistant Sensor

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

Application use json file to parse weeks for waste collection. 

# Example od binary sensors  
binary_sensor:
  - platform: wastecollection
    name: Komunál
    type: "komunal"
  - platform: wastecollection
    name: Plast
    type: "plast"
  - platform: wastecollection
    name: Papír
    type: "papir"
  - platform: wastecollection
    name: Bio
    type: "bio"
