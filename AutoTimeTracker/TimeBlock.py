from datetime import datetime

class Activity_List:
    
    def __init__(self,activities):
        self.activity_entries = activities
        
    def activity_list_to_json(self):
        print("here1")
        act_list = []
        for activity in self.activity_entries:
            act_list.append(activity.serialize())
        return act_list


    def serialize(self):
        return{
            'activities':self.activity_list_to_json()
        }

class Activity:

    def __init__(self, name, time_entries):
        self.name = name
        self.time_entries = time_entries

    def activity_to_json(self):
        time_entry_list = []
        for time_entry in self.time_entries:
            time_entry_list.append(time_entry.serialize())
        return time_entry_list

    def serialize(self):
        return{
            'name': self.name,
            'time_entries' : self.activity_to_json()
        }

class TimeBlock:

    def __init__(self, start_time, end_time, days, hours, minutes, seconds):
        self.start_time = start_time
        self.end_time = end_time
        self.total_time = end_time - start_time
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def calculate_time_attributes(self):
        self.days, self.seconds = self.total_time.days, self.total_time.seconds
        print("days = {} ; seconds = {}".format(self.days, self.seconds))
        self.hours = self.seconds//3600
        self.minutes = (self.seconds%3600)//60
        self.seconds = (self.seconds % 60 )

    def serialize(self):
        return{
            'start_time' : self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            'end_time' : self.end_time.strftime("%Y-%m-%d %H:%M:%S"),
            'days' : self.days,
            'hours' : self.hours,
            'minutes' : self.minutes,
            'seconds' : self.seconds
        }

    