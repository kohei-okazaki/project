import calendar
import datetime
import logging

# logger
logger = logging.getLogger(__name__)

# date format
format_YYYYMM = "%Y%m"
format_YYYYMMDD = "%Y%m%d"

# 文字列形式のYYYYMMを返す
# 引数が未指定の場合、システム日付を返す
def getStrYYYYMM(val):
    sysdate = datetime.datetime.now()
    return val if val else sysdate.date().strftime(format_YYYYMM)

# YYYYMMDD形式の文字列をdatetimeで返す
def convertDate(strDate):
    if not strDate:
        logger.warn("引数が未指定. strDate=" + strDate)
        return datetime.datetime.now()

    return datetime.datetime.strptime(strDate, format_YYYYMMDD)

# yyyymm形式の年月の月初のdatetimeを返す
def getFirstDateForStr(val):
    return convertDate(val + "01")

# datetime形式の年月の月初のdatetimeを返す
def getFirstDate(val):
    return val.replace(day=1)

# yyyymm形式の年月の月末のdatetimeを返す
def getLastDateForStr(val):
    dt = convertDate(val + "01")
    return getLastDate(dt)

# datetime形式の年月の月末のdatetimeを返す
def getLastDate(val):
    return val.replace(day=calendar.monthrange(val.year, val.month)[1])