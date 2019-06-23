import numpy as np

# creating a date
today = np.datetime64('2017-02-12')
print 'Date is: ', today
print 'Year is: ', np.datetime64(today, 'Y')

# creation of array of dates in a month
dates = np.arange('2017-02', '2017-03', dtype = 'datetime64[D]')
print "Dates in February, 2017:\n", dates
print 'Today is February:', today in dates

# arithmetic operation on dates
dur = np.datetime64('2017-05-22') - np.datetime64('2016-05-22')
print 'No. of days: ', dur
print 'No. of weeks: ', np.timedelta64(dur, 'W')

# Sorting dates
a = np.array(['2017-02-12','2016-10-13','2019-05-22'], dtype = 'datetime64')
print 'Dates in sorted order: ', np.sort(a)
