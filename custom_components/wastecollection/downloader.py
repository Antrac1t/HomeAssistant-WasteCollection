import json
import datetime
from urllib.request import urlopen

def getCalendar():
    return "http://192.168.192.25:8123/local/svoz_odpadu.json"


def parseCalendar(CalendarJson,type,dayValue,hourValue):
    #input_region_dict = json.load(regionFile )
    dateNow = datetime.datetime.now()
    dayHour = dateNow.hour
    dayWeek = dateNow.isoweekday()
    next_week = dateNow + datetime.timedelta(days=7)
    # hour & week > dateNow -> show this week
    # hour & week < dateNow -> show next week
    if int(dayWeek) < int(dayValue):
        week_number = dateNow.isocalendar()[1]
    elif int(dayWeek) == int(dayValue):
        if int(dayHour)<=int(hourValue):
            week_number = dateNow.isocalendar()[1]
        else:
            week_number = next_week.isocalendar()[1]
    else:
        week_number = next_week.isocalendar()[1]

    output_calendar_dict = [x for x in CalendarJson if x['week'] == week_number]
    for itemData in output_calendar_dict:
        for itemTypes in itemData['Types']:
            if itemTypes['Typ'] == type:
                if itemTypes['Status'] == 1:
                    StatusOfWaste = True
                else:
                    StatusOfWaste = False
    return StatusOfWaste


def test(CalendarJson,type,dayValue,hourValue):
    #input_region_dict = json.load(regionFile )
    dateNow = datetime.datetime.now()
    week_number = dateNow.isocalendar()[1]

    output_calendar_dict = [x for x in CalendarJson if x['week'] == week_number]
    for itemData in output_calendar_dict:
        for itemTypes in itemData['Types']:
            if itemTypes['Typ'] == type:
                if itemTypes['Status'] == 1:
                    StatusOfWaste = True
                else:
                    StatusOfWaste = False
    return StatusOfWaste
