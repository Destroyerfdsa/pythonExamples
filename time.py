import calendar
import time
yes = True

def clock():
    totalMilliseconds = calendar.timegm(time.gmtime())
    totalMilliseconds =totalMilliseconds *1000
    totalSeconds = totalMilliseconds / 1000
    currentSecond = int(totalSeconds % 60)

    totalMinutes = totalSeconds / 60
    currentMinute = int(totalMinutes % 60)

    totalHours = totalMinutes / 60
    currentHour = int(totalHours % 24)
    currentHour -= 6


##    print("Total ms: ",totalMilliseconds)
##    print("Total Seconds: ",totalSeconds)
##    print("Total Minutes",totalMinutes)
##    print("Total Hours",totalHours)
##    print("Actual time(hopefully)")
    return currentHour,currentMinute,currentSecond
        

##currentHour,currentMinute,currentSecond = clock()

while yes == True:
    currentHour,currentMinute,currentSecond = clock()
    #print(currentHour,":",currentMinute,":",currentSecond)
    print("%s:%s:%s" % (currentHour,currentMinute,currentSecond))
