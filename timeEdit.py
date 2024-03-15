import datetime

def timefunc1():
    testtime=datetime.datetime.now()
    t=testtime.strftime("%Y.%m.%d %H:%M")
    t1=testtime.strftime("%m.%d %H:%M")
    year=t[2:4]
    return_time=year+"."+t1

    return return_time

