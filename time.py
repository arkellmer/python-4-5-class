#andrew kellmer 9/21/18
#world clock


import time
import calendar


##def clock(total_time):
##    
##    time_left = total_time
##
##    #days = time_left // 86400
##    #time_left = time_left % 86400
##    time_left = time_left - 21600
##    total_hours = time_left // 3600
##    hours = total_hours % 24
##    time_left = time_left % 3600
##    minutes = time_left // 60
##    time_left = time_left % 60
##    seconds = time_left
##
##    return hours, minutes, seconds
##    
##
##
##total_time = calendar.timegm (time.gmtime())
##
##hours, minutes, seconds = clock(total_time)
##
##print ("Total Seconds:",total_time)
##print ("Days:", days)
##print ("Hours:", hours)
##print ("Minutes:", minutes)
##print ("Seconds:", seconds)
##print ("Current Time: ",hours,":",minutes,":",seconds)
##
##clock()


while True:
    total_time = calendar.timegm (time.gmtime())

    time_left = total_time
     
    time_left = time_left - 21600
    total_hours = time_left // 3600
    hours = total_hours % 24
    time_left = time_left % 3600
    minutes = time_left // 60
    time_left = time_left % 60
    seconds = time_left

    time.sleep (1)

    print ("Current Time: ",hours,":",minutes,":",seconds)



