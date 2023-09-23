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


def get_sysdate() -> datetime:
    '''
    システム日時のdatetimeを返す
    '''
    return datetime.datetime.now()


def to_str(dt: datetime, format: str) -> str:
    '''
    datetime => 文字列形式
    '''
    if (dt is None):
        logger.warn("引数が未指定. dt=None")
        return None
    return dt.strftime(format)


def to_date(str: str, format: str) -> datetime:
    '''
    文字列 => datetime
    '''
    if (str is None):
        logger.warn("引数が未指定. str=None")
        return None
    return datetime.datetime.strptime(str, format)


def get_str_yyyymm(str: str) -> str:
    '''
    文字列形式のYYYYMMを返す
    引数が未指定の場合、システム日付を返す
    '''
    if (str is None):
        logger.warn("引数が未指定. str=None")
        return to_str(datetime.datetime.now().date(), format_YYYYMM)
    return str


def get_any_month(dt: datetime, month: int) -> datetime:
    '''
    指定されたdatetimeにmonthを加算して返す
    '''
    return dt + relativedelta(months=month)


def get_first_date_str(str: str) -> datetime:
    '''
    yyyymm形式の年月の月初のdatetimeを返す
    '''
    return to_date(str + "01", format_YYYYMMDD)


def getFirstDate(dt: datetime) -> datetime:
    '''
    datetime形式の年月の月初のdatetimeを返す
    '''
    return dt.replace(day=1)


def get_last_date_str(str: str) -> datetime:
    '''
    yyyymm形式の年月の月末のdatetimeを返す
    '''
    dt: datetime = to_date(str + "01", format_YYYYMMDD)
    return get_last_date(dt)


def get_last_date(dt: datetime) -> datetime:
    '''
    datetime形式の年月の月末のdatetimeを返す
    '''
    return dt.replace(day=calendar.monthrange(dt.year, dt.month)[1])
