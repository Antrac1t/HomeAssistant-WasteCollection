# Waste collection - Home Assistant Sensor

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

Application use json file to parse weeks for waste collection and showed active status of each bin over week.

## Installation

### Step 1: Download files

#### Option 1: Via HACS

Make sure you have HACS installed. If you don't, run `curl -sfSL https://hacs.xyz/install | bash -` in HA.
Then choose Components under HACS. Choose the menu in the upper right, and select Custom repositories. Then add this repo's URL. You should be able to choose to Install now.

#### Option 2: Manual
Clone this repository or download the source code as a zip file and add/merge the `custom_components/` folder with its contents in your configuration directory.

### Step 2: Create JSON file
In repository is save example of json file called svoz_odpadu.json. Define all weeks in year and assign them yours type of waste collection 
```yaml
{
    "week": 1,
    "Types": [{
            "Typ": "komunal",
            "Status": 1
        }, {
            "Typ": "plast",
            "Status": 0
        }, {
            "Typ": "papir",
            "Status": 0
        }, {
            "Typ": "bio",
            "Status": 0
        }
    ]
}
```
### Step 3: Configure
Add the following to your `configuration.yaml` file:

```yaml
# Example od binary sensors  
binary_sensor:
  - platform: wastecollection
    name: Komunál
    day: "1"
    hour: "8"
    type: "komunal"
  - platform: wastecollection
    name: Plast
    day: "1"
    hour: "8"
    type: "plast"
  - platform: wastecollection
    name: Papír
    day: "1"
    hour: "8"
    type: "papir"
  - platform: wastecollection
    name: Bio
    day: "1"
    hour: "8"
    type: "bio"
```
