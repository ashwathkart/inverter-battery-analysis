from django.shortcuts import render
from django.http import HttpResponse
# from .models import Battery
import mysql.connector

def battery(request):
    import mysql.connector
    from datetime import datetime as dt
    from datetime import timedelta as delta

    mydb = mysql.connector.connect(host = 'localhost', user = "username", passwd = 'password', database = 'mydb', auth_plugin='mysql_native_password')

    #battery table
    battery_cursor = mydb.cursor()
    battery_cursor.execute("SELECT * FROM battery WHERE product = 1 ORDER BY id DESC")
    battery_cursor = list(battery_cursor)

    #user table
    user_cursor = mydb.cursor()
    user_cursor.execute("SELECT * FROM users WHERE product = 1")
    user_cursor = list(user_cursor)
    
    name = user_cursor[0][1]
    date = user_cursor[0][3]

    #initialize column lists
    id = []
    timestamp = []
    voltage = []

    #assign column lists
    for i in battery_cursor:
        id.append(i[0])
        timestamp.append(i[2])
        voltage.append(i[3])

    #check voltage and assign range
    def find_range(volts):
        if volts >= 12.6:
            range = 100
        elif (volts < 12.6) & (volts >= 12.5):
            range = 90
        elif (volts < 12.5) & (volts >= 12.42):
            range = 80
        elif (volts < 12.42) & (volts >= 12.32):
            range = 70
        elif (volts < 12.32) & (volts >= 12.2):
            range = 60
        elif (volts < 12.2) & (volts >= 12.06):
            range = 50
        elif (volts < 12.06) & (volts >= 11.90):
            range = 40
        elif (volts < 11.90) & (volts >= 11.75):
            range = 30
        elif (volts < 11.75) & (volts >= 11.58):
            range = 20
        elif (volts < 11.58) & (volts >= 11.31):
            range = 10
        else:
            range = 0

        return range

    #check online or offline
    def online():
        if dt.now() - timestamp[0] > delta(minutes = 20):
            comment = "offline"
        else:
            comment = "online"
        return comment

    #check status
    def check_status():
        j = 0
        
        #find timestamp of 15 mins ago
        fifteen = dt.now() - delta(minutes = 15)
        
        #find the record closest to 15 mins ago
        while j < len(timestamp):
            if timestamp[j] - fifteen <= delta(minutes = 2):
                closest_to = timestamp[j]
                break
            j +=1
        
        #find voltage of that record
        reqd_volts = voltage[j-1]

        #find slope
        volts_diff = float(voltage[0]-reqd_volts)
        time_diff = timestamp[0]-timestamp[j]
        time_diff = time_diff.total_seconds()/60

        slope = volts_diff/time_diff
        
        if slope > 1:
            status = "Charging"
        elif (slope <= 1) & (slope > 0):
            status = "Stable"
        elif (slope <= 0) & (slope > -1):
            status = "Discharging"
        else:
            status = "Discharging heavily, your attention is required."
        
        return status

    #body of code
    percentage = find_range(voltage[0])
    status = check_status()
    online = online()

    return render(request, 'final-battery.html', {'name':str(name), 'date':str(date), 'percentage':str(percentage), 'status':str(status), 'online':str(online)})
