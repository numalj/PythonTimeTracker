#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 21:26:50 2019

@author: numalj
"""
from AppKit import NSWorkspace
from Foundation import *
import time
from datetime import datetime
import json
from TimeBlock import *
import os 

print("test")

dir_path = os.path.dirname(os.path.realpath(__file__))
JSON_FILE_PATH = dir_path+'/'+'activities.json'
last_activity_name = ''
start_time = datetime.now()
first_time = True
activity_list = Activity_List([])

def get_chrome_url():
    textOfMyScript = """tell app "google chrome" to get the url of the active tab of window 1"""
    s = NSAppleScript.initWithSource_(NSAppleScript.alloc(), textOfMyScript)
    results, err = s.executeAndReturnError_(None)
    return results.stringValue()

def url_to_name(url):
    string_list = url.split('/')
    return string_list[2]

while True:
    active_window_name = (NSWorkspace.sharedWorkspace()
                               .activeApplication()['NSApplicationName'])
    
    if active_window_name == "Google Chrome":
                active_window_name = url_to_name(get_chrome_url())

    if active_window_name != last_activity_name:
        print("New Activity: {} ; Previous Activity: {}".format(active_window_name,last_activity_name))
        #print("Active Window: %s" % active_window_name)
        if first_time:
            #print("First Time")
            #print("Active Window: %s, Current Activity: %s" % (active_window_name,last_activity_name))
            first_time = False
            last_activity_name = active_window_name
        
        else:
            end_time = datetime.now()

            print(last_activity_name)
            
            #Look for activity in list
            found=False
            curr_activity = Activity(last_activity_name, [])
            for activity in activity_list.activity_entries:
                if activity.name == last_activity_name:
                    curr_activity = activity
                    print("Found Activity: {}",last_activity_name)
                    found = True
                    break
                
            if not found:
                #Create Activity
                activity_list.activity_entries.append(curr_activity)
                
                 
            #Create time block
            timeEntry = TimeBlock(start_time, end_time, 0, 0,0, 0)
            timeEntry.calculate_time_attributes()
            #print(json.dumps(timeEntry.serialize()))

            curr_activity.time_entries.append(timeEntry)

            #print(json.dumps(activity_list.serialize()))
            #Write JSON to file
            with open(JSON_FILE_PATH, 'w') as outfile:
                json.dump(activity_list.serialize(), outfile)
            
            start_time=datetime.now()
            last_activity_name = active_window_name

    time.sleep(1)