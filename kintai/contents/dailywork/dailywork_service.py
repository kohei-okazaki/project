import datetime
import decimal
from kintai.contents.util import date_util
from kintai.models import BusinessCalendarMt, DailyUserWorkData, UserData


def get_business_calendar_mt_list(from_date: datetime, to_date: datetime) -> list:
    '''
    対象年月期間の営業日マスタを取得
    '''
    return BusinessCalendarMt.objects.filter(date__range=[from_date, to_date])


def get_actual_work_date(start_hh: str, start_mi: str, end_hh: str, end_mi: str) -> decimal:
    '''
    実労働時間を取得
    '''
    start: datetime = date_util.to_date(
        start_hh + ":" + start_mi + ":00", date_util.format_HHMISS_SEP)
    end: datetime = date_util.to_date(end_hh + ":" + end_mi + ":00",
                            date_util.format_HHMISS_SEP)
    return (end - start).seconds / 60 / 60


def regist_daily_user_work_data(user: UserData, year: str, month: str, day: str, start_hh: str, start_mi: str, end_hh: str, end_mi: str) -> bool:
    '''
    DAILY_USER_WORK_DATAを登録する
    '''
    seq_user_id: int = user.seq_user_id
    company_cd: str = user.company_cd
    division_cd: str = user.division_cd
    work_start_date: datetime = datetime.datetime(int(year), int(
        month), int(day), int(start_hh), int(start_mi), 00)
    work_end_date: datetime = datetime.datetime(int(year), int(
        month), int(day), int(end_hh), int(end_mi), 00)
    actual_work_date: decimal = get_actual_work_date(
        start_hh, start_mi, end_hh, end_mi)

    work_data: DailyUserWorkData = DailyUserWorkData(
        seq_user_id=seq_user_id,
        company_cd=company_cd,
        division_cd=division_cd,
        work_start_date=work_start_date,
        work_end_date=work_end_date,
        actual_work_date=actual_work_date)

    work_data.save()

    return True
