import datetime

# print(datetime.datetime.now())

from datetime import datetime
from zoneinfo import ZoneInfo

# print(datetime.now())
UTC_TZ = ZoneInfo("UTC")
IST_TZ = ZoneInfo("Asia/Kolkata")
print(datetime.now(UTC_TZ))
print(datetime.now(IST_TZ))
