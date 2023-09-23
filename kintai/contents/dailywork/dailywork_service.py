import datetime
from kintai.contents.util import date_util
from kintai.models import BusinessCalendarMt, DailyUserWorkData

# 対象年月期間の営業日マスタを取得
def get_business_calendar_mt_list(from_date, to_date):
    return BusinessCalendarMt.objects.filter(date__range=[from_date, to_date])

# 実労働時間を取得
def get_actual_work_date(start_hh, start_mi, end_hh, end_mi):
    start = date_util.toDate(start_hh + ":" + start_mi + ":00", date_util.format_HHMISS_SEP)
    end = date_util.toDate(end_hh + ":" + end_mi + ":00", date_util.format_HHMISS_SEP)
    return (end - start).seconds / 60 / 60

# DAILY_USER_WORK_DATAを登録する
def regist_daily_user_work_data(user, year, month, day, start_hh, start_mi, end_hh, end_mi):

    seq_user_id = user.seq_user_id
    company_cd = user.company_cd
    division_cd = user.division_cd
    work_start_date = datetime.datetime(int(year), int(month), int(day), int(start_hh), int(start_mi), 00)
    work_end_date = datetime.datetime(int(year), int(month), int(day), int(end_hh), int(end_mi), 00)
    actual_work_date = get_actual_work_date(start_hh, start_mi, end_hh, end_mi)

    work_data = DailyUserWorkData(\
        seq_user_id = seq_user_id, \
        company_cd = company_cd, \
        division_cd = division_cd, \
        work_start_date = work_start_date,\
        work_end_date = work_end_date, \
        actual_work_date = actual_work_date)

    work_data.save()

    return True