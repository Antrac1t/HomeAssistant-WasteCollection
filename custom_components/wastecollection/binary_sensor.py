__version__ = "0.1"

import logging
from . import downloader
import voluptuous as vol
from datetime import timedelta, datetime, date
from homeassistant.components.sensor import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.util import Throttle

import requests
from lxml import html, etree

MIN_TIME_BETWEEN_SCANS = timedelta(seconds=300)
_LOGGER = logging.getLogger(__name__)

DOMAIN = "wastecollection"
CONF_DAY = "day"
CONF_HOUR = "hour"
CONF_TYPE = "type"
CONF_NAME = "name"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_DAY): cv.string,
        vol.Required(CONF_HOUR): cv.string,
        vol.Required(CONF_TYPE): cv.string,
        vol.Required(CONF_NAME): cv.string,
    }
)

def setup_platform(hass, config, add_entities, discovery_info=None):
    name = config.get(CONF_NAME)
    day = config.get(CONF_DAY)
    hour = config.get(CONF_HOUR)
    type = config.get(CONF_TYPE)

    ents = []
    ents.append(WasteCollection(name,day,hour,type))
    add_entities(ents)

class WasteCollection(BinarySensorEntity):
    def __init__(self, name,day,hour,type):
        """Initialize the sensor."""
        self._name = name
        self.day = day
        self.hour = hour
        self.type = type
        self.responseCalendarJson = "[]"
        self.status= False
        self.update()

    @property
    def name(self):
        return self._name

    @property
    def icon(self):
        return "mdi:trash-can-outline"

    @property
    def should_poll(self):
        return True

    @property
    def available(self):
        return self.last_update_success

    @property
    def device_class(self):
        return ''

    @property
    def is_on(self):
        self.status  = downloader.parseCalendar(self.responseCalendarJson,self.type,self.day,self.hour)
        return self.status

    @property
    def device_state_attributes(self):
        attributes = {}
        attributes['Svoz odpadu'] = downloader.test(self.responseCalendarJson,self.type,self.day,self.hour)
        return attributes

    @Throttle(MIN_TIME_BETWEEN_SCANS)
    def update(self):
        responseCalendar = requests.get(downloader.getCalendar())
        if responseCalendar.status_code == 200:
            self.responseCalendarJson = responseCalendar.json() 
            self.last_update_success = True
        else:
            self.last_update_success = False
