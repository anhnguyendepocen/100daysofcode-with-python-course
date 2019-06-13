from datetime import datetime, timedelta
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    extract_date = re.search('\d{4}-\d{2}-\d{2}.\d{2}:\d{2}:\d{2}', line).group()
    date = datetime.strptime(extract_date, '%Y-%m-%dT%H:%M:%S')
    return date


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdowns = []
    for line in loglines:
        event = re.findall('Shutdown initiated', line)
        if event:
            date = convert_to_datetime(line)
            shutdowns.append(date)

    diff = shutdowns[-1] - shutdowns[0]
    return diff


line1 = 'ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file'
line2 = 'INFO 2015-10-03T10:12:51 supybot Shutdown initiated.'
line3 = 'INFO 2016-09-03T02:11:22 supybot Shutdown complete.'
convert_to_datetime(line1) == datetime(2014, 7, 3, 23, 24, 31)
convert_to_datetime(line2) == datetime(2015, 10, 3, 10, 12, 51)
convert_to_datetime(line3) == datetime(2016, 9, 3, 2, 11, 22)

diff = time_between_shutdowns(loglines)
type(diff) == timedelta
str(diff) == '0:03:31'
