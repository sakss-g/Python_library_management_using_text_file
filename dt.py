
#creating functions for current date and time

def get_date():
    import datetime
    now = datetime.datetime.now
    return str(now().date())

def get_time():
    import datetime
    now = datetime.datetime.now
    return str(now().time())
