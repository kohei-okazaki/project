from kintai.models import BusinessCalendarMt, CompanyMt, DailyUserWorkData, DivisionMt, UserData
import datetime


class UserDataDto(UserData):
    """ユーザ情報Dto
    """


class CompanyMtDto(CompanyMt):
    """企業マスタDto
    """


class DivisionMtDto(DivisionMt):
    """部署マスタDto
    """


class DailyworkDto(BusinessCalendarMt):
    """日次勤怠登録画面で表示する情報保持クラス
    """
    work_start_date: datetime = None
    work_end_date: datetime = None


class BusinessCalendarMtDto(BusinessCalendarMt):
    """営業日マスタDto
    """


class DailyUserWorkDataDto(DailyUserWorkData):
    """日別ユーザ勤怠情報Dto
    """
