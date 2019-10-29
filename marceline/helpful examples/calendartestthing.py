import os
from datetime import datetime
import calendar

megacalendar = calendar.Calendar().yeardatescalendar(datetime.now().year, width=3)

print(megacalendar)

#USE DELTA TIME THINGS!

#https://docs.python.org/3/library/datetime.html
#http://stackoverflow.com/questions/35767340/extracting-datetime-info-from-yeardatescalendar-in-python
#http://stackoverflow.com/questions/415511/how-to-get-current-time-in-python
#https://docs.python.org/3/library/calendar.html#module-calendar
