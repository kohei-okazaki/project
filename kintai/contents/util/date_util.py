import calendar
import datetime
import logging
from dateutil.relativedelta import relativedelta

# logger
logger = logging.getLogger(__name__)

# date format
FORMAT_YYYYMM = "%Y%m"
FORMAT_YYYYMMDD = "%Y%m%d"
FORMAT_HHMISS_SEP = "%H:%M:%S"


def get_sysdate() -> datetime:
    """
    システム日時を返す

    Returns:
        datetime: システム日時
    """
    return datetime.datetime.now()


def to_str(dt: datetime, format: str) -> str:
    """
    datetime => 文字列形式

    Args:
        dt (datetime): 変換前のdatetime
        format (str): 変換フォーマット

    Returns:
        str: 変換後の文字列形式
    """
    if dt is None:
        logger.warn("引数が未指定. dt=None")
        return None
    return dt.strftime(format)


def to_date(s: str, format: str) -> datetime:
    """
    文字列 => datetime

    Args:
        s (str): 変換前の文字列形式の日付
        format (str): 変換フォーマット

    Returns:
        datetime: 変換後のdatetime
    """
    if s is None:
        logger.warn("引数が未指定. str=None")
        return None
    return datetime.datetime.strptime(s, format)


def get_str_yyyymm(s: str) -> str:
    """
    引数が未指定の場合、システム日付を返す

    Args:
        s (str): 文字列形式の日付

    Returns:
        str: 文字列形式の日付
    """
    if s is None:
        logger.warn("引数が未指定. str=None")
        return to_str(datetime.datetime.now().date(), FORMAT_YYYYMM)
    return s


def get_any_month(dt: datetime, month: int) -> datetime:
    """指定されたdatetimeにmonthを加算して返す

    Args:
        dt (datetime): 加算対象datetime
        month (int): 加算月数

    Returns:
        datetime: 加算済のdatetime
    """
    return dt + relativedelta(months=month)


def get_first_date_str(s: str) -> datetime:
    """yyyymm形式の年月の月初のdatetimeを返す

    Args:
        s (str): 対象年月

    Returns:
        datetime: 月初のdatetime
    """
    return to_date(s + "01", FORMAT_YYYYMMDD)


def get_first_date(dt: datetime) -> datetime:
    """datetime形式の年月の月初のdatetimeを返す

    Args:
        dt (datetime): 対象年月

    Returns:
        datetime: 月初のdatetime
    """
    return dt.replace(day=1)


def get_last_date_str(s: str) -> datetime:
    """yyyymm形式の年月の月末のdatetimeを返す

    Args:
        s (str): 対象年月

    Returns:
        datetime: 月末のdatetime
    """
    dt: datetime = to_date(s + "01", FORMAT_YYYYMMDD)
    return get_last_date(dt)


def get_last_date(dt: datetime) -> datetime:
    """datetime形式の年月の月末のdatetimeを返す

    Args:
        dt:

    Returns:
        datetime: 月末のdatetime
    """
    return dt.replace(day=calendar.monthrange(dt.year, dt.month)[1])
