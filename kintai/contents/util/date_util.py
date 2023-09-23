import calendar
import datetime
import logging
from dateutil.relativedelta import relativedelta

# logger
logger = logging.getLogger(__name__)

# date format
format_YYYYMM = "%Y%m"
format_YYYYMMDD = "%Y%m%d"
format_HHMISS_SEP = "%H:%M:%S"

# システム日時のdatetimeを返す
def get_sysdate():
    return datetime.datetime.now()

# datetime => 文字列形式
def to_str(dt, format):
    if (dt is None):
        logger.warn("引数が未指定. dt=None")
        return None
    return dt.strftime(format)

# 文字列 => datetime
def to_date(str, format):
    if (str is None):
        logger.warn("引数が未指定. str=None")
        return None
    return datetime.datetime.strptime(str, format)

# 文字列形式のYYYYMMを返す
# 引数が未指定の場合、システム日付を返す
def get_str_yyyymm(str):
    if (str is None):
        logger.warn("引数が未指定. str=None")
        return to_str(datetime.datetime.now().date(), format_YYYYMM)
    return str

# 指定されたdatetimeにmonthを加算して返す
def get_any_month(dt, month):
    return dt + relativedelta(months=month)

# yyyymm形式の年月の月初のdatetimeを返す
def get_first_date_str(str):
    return to_date(str + "01", format_YYYYMMDD)

# datetime形式の年月の月初のdatetimeを返す
def getFirstDate(dt):
    return dt.replace(day=1)

# yyyymm形式の年月の月末のdatetimeを返す
def get_last_date_str(str):
    dt = to_date(str + "01", format_YYYYMMDD)
    return get_last_date(dt)

# datetime形式の年月の月末のdatetimeを返す
def get_last_date(dt):
    return dt.replace(day=calendar.monthrange(dt.year, dt.month)[1])