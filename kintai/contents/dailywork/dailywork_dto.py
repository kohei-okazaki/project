
import datetime
from kintai.models import BusinessCalendarMt


class DailyworkDto(BusinessCalendarMt):
    '''
    日次勤怠登録画面で表示する情報保持クラス
    '''
    work_start_date: datetime = None
    work_end_date: datetime = None
