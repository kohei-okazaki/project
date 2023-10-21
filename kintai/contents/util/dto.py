import datetime
import decimal
from kintai.models import BusinessCalendarMt, CompanyMt, DailyUserWorkData, DivisionMt, OntimeMt, UserData


class UserDataDto:
    """ユーザ情報Dto
    """

    def __init__(self, entity: UserData = None):
        """コンストラクタ

        Args:
            entity (UserData, optional): ユーザ情報. Defaults to None.
        """

        if entity is None:
            return

        self.seq_user_id: decimal = entity.seq_user_id
        self.password: str = entity.password
        self.company_cd: str = entity.company_cd
        self.division_cd: str = entity.division_cd
        self.del_flg: bool = entity.del_flg
        self.reg_date: datetime = entity.reg_date
        self.update_date: datetime = entity.update_date


class CompanyMtDto:
    """企業マスタDto
    """

    def __init__(self, entity: CompanyMt = None):
        """コンストラクタ

        Args:
            entity (CompanyMt, optional): 企業マスタ. Defaults to None.
        """

        if entity is None:
            return

        self.company_cd: str = entity.company_cd
        self.name: str = entity.name
        self.del_flg: bool = entity.del_flg
        self.reg_date: datetime = entity.reg_date
        self.update_date: datetime = entity.update_date


class DivisionMtDto:
    """部署マスタDto
    """

    def __init__(self, entity: DivisionMt = None):
        """コンストラクタ

        Args:
            entity (DivisionMt, optional): 部署マスタ. Defaults to None.
        """

        if entity is None:
            return

        self.division_cd: str = entity.division_cd
        self.name: str = entity.name
        self.del_flg: bool = entity.del_flg
        self.reg_date: datetime = entity.reg_date
        self.update_date: datetime = entity.update_date


class DailyworkDto:
    """日次勤怠登録画面で表示する情報保持クラス
    """
    date: datetime = None
    weekday: str = None
    business_flg: bool = None
    work_start_date: datetime = None
    work_end_date: datetime = None
    actual_work_date: datetime = None
    rest_time: decimal = None
    over_time: decimal = None
    note: str = ""


class BusinessCalendarMtDto:
    """営業日マスタDto
    """

    def __init__(self, entity: BusinessCalendarMt = None):
        """コンストラクタ

        Args:
            entity (BusinessCalendarMt, optional): 営業日マスタ. Defaults to None.
        """

        if entity is None:
            return

        self.seq_business_calendar_mt_id: decimal = entity.seq_business_calendar_mt_id
        self.date: datetime.date = entity.date
        self.weekday: str = entity.weekday
        self.business_flg: bool = entity.business_flg
        self.reg_date: datetime = entity.reg_date
        self.update_date: datetime = entity.update_date


class DailyUserWorkDataDto:
    """日別ユーザ勤怠情報Dto
    """

    def __init__(self, entity: DailyUserWorkData = None):
        """コンストラクタ

        Args:
            entity (DailyUserWorkData, optional): 日別ユーザ勤怠情報. Defaults to None.
        """

        if entity is None:
            return

        self.seq_daily_user_work_data_id: decimal = entity.seq_daily_user_work_data_id
        self.seq_user_id: decimal = entity.seq_user_id
        self.company_cd: str = entity.company_cd
        self.division_cd: str = entity.division_cd
        self.work_data_reg_date: datetime = entity.work_data_reg_date
        self.work_start_date: datetime = entity.work_start_date
        self.work_end_date: datetime = entity.work_end_date
        self.actual_work_date: decimal = entity.actual_work_date
        self.rest_time: decimal = entity.rest_time
        self.over_time: decimal = entity.over_time
        self.approval_flg: bool = entity.approval_flg
        self.cancel_flg: bool = entity.cancel_flg
        self.note: str = entity.note
        self.reg_date: datetime = entity.reg_date
        self.update_date: datetime = entity.update_date


class OntimeMtDto:
    """定時マスタDto
    """

    def __init__(self, entity: OntimeMt = None):
        """コンストラクタ

        Args:
            entity (OntimeMt, optional): 定時マスタ. Defaults to None.
        """

        if entity is None:
            return

        self.seq_ontime_mt_id: decimal = entity.seq_ontime_mt_id
        self.company_cd: str = entity.company_cd
        self.division_cd: str = entity.division_cd
        self.start_hour: str = entity.start_hour
        self.start_minute: str = entity.start_minute
        self.end_hour: str = entity.end_hour
        self.end_minute: str = entity.end_minute
        self.del_flg: bool = entity.del_flg
        self.reg_date: datetime = entity.reg_date
        self.update_date: datetime = entity.update_date
