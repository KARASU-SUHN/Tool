#To convert a date in string to different formats.
import datetime,time

def createDateObject(str_date,strFormat="%Y-%m-%d"):    
    timeStamp = time.mktime(time.strptime(str_date,strFormat))
    return datetime.datetime.fromtimestamp(timeStamp)

def FormatDate(objectDate,strFormat="%Y-%m-%d"):
    return objectDate.strftime(strFormat)
  

c=createDateObject('2013-03-03')
f=FormatDate(c,'%d-%m-%Y')
# _____
# f
# output: '03-03-2013'


#### covert unix timestamp to date  ## way1: use pd
import pandas
time=pd.read_csv('*Pathtime.csv',names=["unix"])
unix=time['unix']
result_s=pandas.to_datetime(unix,unit='s')
# str(result_s)
print(result_s) #output dtype:datetime64

#convert datetime to string  #make sure import datetime module
date = result_s.apply(lambda x: x.strftime('%Y'))
# df['DATE'] = df['Date'].apply(lambda x: x.strftime('%Y-%m-%d')) 

#way2: use datetime package 
from datetime import datetime
ts = int('1284101485')

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

#Convert unix timestamp in Python to datetime and make 2 Hours behind
from datetime import datetime, timedelta

unix_ts = 1507126064
dt = (datetime.fromtimestamp(unix_ts) - timedelta(hours=2)).strftime('%Y-%m-%d %H:%M:%S')
print(dt)
