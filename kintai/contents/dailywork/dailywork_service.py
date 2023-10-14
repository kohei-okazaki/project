import datetime
import decimal
from decimal import Decimal
from kintai.contents.util import date_util, ontime_mt_service
from kintai.contents.util.dto import BusinessCalendarMtDto, DailyUserWorkDataDto, DailyworkDto, OntimeMtDto, UserDataDto
from kintai.forms import DailyworkCreateForm
from kintai.models import BusinessCalendarMt, DailyUserWorkData


def get_daily_user_work_dto_list(user: UserDataDto, yyyymm: str) -> list:
    """対象ユーザと対象年月の営業日マスタリストと日別ユーザ勤怠情報リストをマージしたリストを返す

    Args:
        user (UserDataDto): ユーザ情報Dto
        yyyymm (str): 対象年月

    Returns:
        list: 営業日マスタリストと日別ユーザ勤怠情報リストをマージしたリスト
    """

    from_date: datetime = date_util.get_first_date_str(yyyymm)
    to_date: datetime = date_util.get_last_date_str(yyyymm)

    # 対象年月の営業日マスタリストを取得
    business_calendar_mt_dto_list: list = get_business_calendar_mt_dto_list(
        from_date, to_date)

    # 対象年月の日別ユーザ勤怠情報リストを取得
    daily_user_work_data_list: list = get_daily_user_work_data_dto_list(
        user, from_date, to_date)

    dto_list: list = []
    for business_calendar_mt_dto in business_calendar_mt_dto_list:
        dto: DailyworkDto = DailyworkDto()
        dto.date = business_calendar_mt_dto.date
        dto.weekday = business_calendar_mt_dto.weekday
        dto.business_flg = business_calendar_mt_dto.business_flg

        for user_work in daily_user_work_data_list:
            if date_util.to_str(business_calendar_mt_dto.date, date_util.FORMAT_YYYYMMDD) == date_util.to_str(user_work.work_start_date, date_util.FORMAT_YYYYMMDD):
                # 登録がある場合
                dto.work_start_date = user_work.work_start_date
                dto.work_end_date = user_work.work_end_date
                dto.actual_work_date = user_work.actual_work_date
                dto.rest_time = user_work.rest_time
                dto.over_time = user_work.over_time
                dto.note = user_work.note

        dto_list.append(dto)

    return dto_list


def get_business_calendar_mt_dto_list(from_date: datetime, to_date: datetime) -> list:
    """対象年月期間の営業日マスタDtoのリストを返す

    Args:
        from_date (datetime): 開始日
        to_date (datetime): 終了日

    Returns:
        list: 営業日マスタDtoのリスト
    """

    mt_list = BusinessCalendarMt.objects.filter(
        date__range=[from_date, to_date])
    dto_list: list = list(BusinessCalendarMtDto(mt) for mt in mt_list)

    return dto_list


def get_daily_user_work_data_dto_list(user: UserDataDto, from_date: datetime, to_date: datetime) -> list:
    """ユーザ情報Dtoと取得対象年月(from)と取得対象年月(to)より、日別ユーザ勤怠情報Dtoのリストを返す

    Args:
        user (UserData): ユーザ情報Dto
        from_date (datetime): 取得対象年月(from)
        to_date (datetime): 取得対象年月(to)

    Returns:
        list: _description_
    """

    user_work_list: list = DailyUserWorkData.objects.filter(
        seq_user_id=user.seq_user_id, work_start_date__range=[from_date, to_date])
    dto_list: list = list(DailyUserWorkDataDto(user_work)
                          for user_work in user_work_list)

    return dto_list


def regist_daily_user_work_data(user: UserDataDto, form: DailyworkCreateForm) -> bool:
    """DAILY_USER_WORK_DATAを登録する

    Args:
        user (UserDataDto): ユーザ情報Dto
        year (str): 年
        month (str): 月
        day (str): 日
        start_hh (str): 開始時間(時)
        start_mi (str): 開始時間(分)
        end_hh (str): 終了時間(時)
        end_mi (str): 終了時間(分)
        rest_time (str): 休憩時間
        note (str): 備考

    Returns:
        bool: 登録処理成功の場合True、それ以外の場合False
    """

    seq_user_id: int = user.seq_user_id
    company_cd: str = user.company_cd
    division_cd: str = user.division_cd

    year: int = int(form.cleaned_data["year"])
    month: int = int(form.cleaned_data["month"])
    day: int = int(form.cleaned_data["day"])
    start_hh: int = int(form.cleaned_data["start_hh"])
    start_mi: int = int(form.cleaned_data["start_mi"])
    end_hh: int = int(form.cleaned_data["end_hh"])
    end_mi: int = int(form.cleaned_data["end_mi"])
    rest_time: decimal = Decimal(form.cleaned_data["rest_time"])
    note: str = form.cleaned_data["note"]

    work_start_date: datetime = datetime.datetime(
        year, month, day, start_hh, start_mi, 00)
    work_end_date: datetime = datetime.datetime(
        year, month, day, end_hh, end_mi, 00)
    actual_work_date: decimal = get_actual_work_date(
        start_hh, start_mi, end_hh, end_mi, rest_time)
    over_time: decimal = get_over_time(
        company_cd, division_cd, actual_work_date, rest_time)

    # 日別ユーザ勤怠情報を検索
    from_date: datetime = datetime.datetime(year, month, day)
    to_date: datetime = datetime.datetime(year, month, day + 1)
    daily_user_work_data_list = DailyUserWorkData.objects.filter(
        seq_user_id=user.seq_user_id, work_start_date__range=[from_date, to_date]).order_by("work_start_date")

    if daily_user_work_data_list.count() > 0:
        # 既に勤怠情報が登録されている場合
        work_data: DailyUserWorkData = daily_user_work_data_list.first()
        work_data.work_start_date = work_start_date
        work_data.work_end_date = work_end_date
        work_data.actual_work_date = actual_work_date
        work_data.rest_time = rest_time
        work_data.over_time = over_time
        work_data.note = note
        work_data.save()

    else:
        work_data: DailyUserWorkData = DailyUserWorkData(
            seq_user_id=seq_user_id,
            company_cd=company_cd,
            division_cd=division_cd,
            work_start_date=work_start_date,
            work_end_date=work_end_date,
            actual_work_date=actual_work_date,
            rest_time=rest_time,
            over_time=over_time,
            note=note)

        work_data.save()

    return True


def get_actual_work_date(start_hh: int, start_mi: int, end_hh: int, end_mi: int, rest_time: decimal) -> decimal:
    """実労働時間を取得

    Args:
        start_hh (int): 開始時間(時)
        start_mi (int): 開始時間(分)
        end_hh (int): 終了時間(時)
        end_mi (int): 終了時間(分)
        rest_time (decimal): 休憩時間

    Returns:
        decimal: 実労働時間(n.n)形式
    """

    start: datetime = date_util.to_date(
        str(start_hh) + ":" + str(start_mi) + ":00", date_util.FORMAT_HHMISS_SEP)
    end: datetime = date_util.to_date(
        str(end_hh) + ":" + str(end_mi) + ":00", date_util.FORMAT_HHMISS_SEP)
    return Decimal(str((end - start).seconds / 60 / 60)) - rest_time


def get_over_time(company_cd: str, division_cd: str, actual_work_date: decimal, rest_time: decimal) -> decimal:
    """残業時間を返す

    Args:
        company_cd (str): 企業コード
        division_cd (str): 部署コード
        actual_work_date (decimal): 実労働時間

    Returns:
        decimal: 残業時間(n.n)形式
    """

    # 定時マスタを取得
    ontime_mt_dto: OntimeMtDto = ontime_mt_service.get_dto(
        company_cd, division_cd)
    if ontime_mt_dto is None:
        return Decimal(0.00)

    start: datetime = date_util.to_date(
        ontime_mt_dto.start_hour + ":" + ontime_mt_dto.start_minute + ":00", date_util.FORMAT_HHMISS_SEP)

    end: datetime = date_util.to_date(
        ontime_mt_dto.end_hour + ":" + ontime_mt_dto.end_minute + ":00", date_util.FORMAT_HHMISS_SEP)

    ontime_diff: decimal = Decimal(
        str((end - start).seconds / 60 / 60)) - rest_time
    over_time: decimal = actual_work_date - ontime_diff

    return over_time if over_time > 0 else 0
