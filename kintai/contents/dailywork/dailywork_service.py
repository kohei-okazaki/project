import datetime
import decimal
from kintai.contents.dailywork.dailywork_dto import DailyworkDto
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
        start_hh + ":" + start_mi + ":00", date_util.FORMAT_HHMISS_SEP)
    end: datetime = date_util.to_date(
        end_hh + ":" + end_mi + ":00", date_util.FORMAT_HHMISS_SEP)
    return (end - start).seconds / 60 / 60


def regist_daily_user_work_data(user: UserData, year: str, month: str, day: str, start_hh: str, start_mi: str, end_hh: str, end_mi: str) -> bool:
    '''
    DAILY_USER_WORK_DATAを登録する
    '''
    seq_user_id: int = user.seq_user_id
    company_cd: str = user.company_cd
    division_cd: str = user.division_cd
    work_start_date: datetime = datetime.datetime(
        int(year), int(month), int(day), int(start_hh), int(start_mi), 00)
    work_end_date: datetime = datetime.datetime(
        int(year), int(month), int(day), int(end_hh), int(end_mi), 00)
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


def get_daily_user_work_data_list(user: UserData, from_date: datetime, to_date: datetime) -> list:
    '''
    ユーザIDと取得対象年月(from)と取得対象年月(to)より、DAILY_USER_WORK_DATAのリストを取得する
    '''
    return DailyUserWorkData.objects.filter(seq_user_id=user.seq_user_id, work_start_date__range=[from_date, to_date])


def get_daily_user_work_dto_list(user: UserData, yyyymm: str) -> list:
    '''
    対象ユーザと対象年月の営業日マスタリストと日別ユーザ勤怠情報リストをマージしたリストを返す
    '''

    from_date: datetime = date_util.get_first_date_str(yyyymm)
    to_date: datetime = date_util.get_last_date_str(yyyymm)

    # 対象年月の営業日マスタリストを取得
    mt_list: list = get_business_calendar_mt_list(from_date, to_date)

    # 対象年月の日別ユーザ勤怠情報リストを取得
    daily_user_work_data_list: list = get_daily_user_work_data_list(
        user, from_date, to_date)

    dto_list: list = []
    for mt in mt_list:
        dto: DailyworkDto = DailyworkDto()
        dto.date = mt.date
        dto.weekday = mt.weekday
        dto.business_flg = mt.business_flg

        for user_work in daily_user_work_data_list:
            if date_util.to_str(mt.date, date_util.FORMAT_YYYYMMDD) == date_util.to_str(user_work.work_start_date, date_util.FORMAT_YYYYMMDD):
                # 登録がある場合
                dto.work_start_date = user_work.work_start_date
                dto.work_end_date = user_work.work_end_date

        dto_list.append(dto)

    return dto_list
