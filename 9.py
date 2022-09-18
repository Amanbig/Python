from datetime import datetime
def times():
    date=datetime.now()
    times=datetime.time(datetime.now())
    print(date.strftime("%D"))
    print(times.strftime("%H %M"))

times()