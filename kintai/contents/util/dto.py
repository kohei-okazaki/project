from kintai.models import BusinessCalendarMt, CompanyMt, DailyUserWorkData, DivisionMt, UserData
import datetime


class UserDataDto():
    """ユーザ情報Dto
    """

    def __init__(self, entity: UserData = None):
        """コンストラクタ

        Args:
            entity (UserData, optional): ユーザ情報. Defaults to None.
        """

        if entity is None:
            return

        self.seq_user_id = entity.seq_user_id
        self.password = entity.password
        self.company_cd = entity.company_cd
        self.division_cd = entity.division_cd
        self.del_flg = entity.del_flg
        self.reg_date = entity.reg_date
        self.update_date = entity.update_date


class CompanyMtDto():
    """企業マスタDto
    """

    def __init__(self, entity: CompanyMt = None):
        """コンストラクタ

        Args:
            entity (CompanyMt, optional): 企業マスタ. Defaults to None.
        """

        if entity is None:
            return

        self.company_cd = entity.company_cd
        self.name = entity.name
        self.del_flg = entity.del_flg
        self.reg_date = entity.reg_date
        self.update_date = entity.update_date


class DivisionMtDto():
    """部署マスタDto
    """

    def __init__(self, entity: DivisionMt = None):
        """コンストラクタ

        Args:
            entity (DivisionMt, optional): 部署マスタ. Defaults to None.
        """

        if entity is None:
            return

        self.division_cd = entity.division_cd
        self.name = entity.name
        self.del_flg = entity.del_flg
        self.reg_date = entity.reg_date
        self.update_date = entity.update_date


class DailyworkDto():
    """日次勤怠登録画面で表示する情報保持クラス
    """
    date: datetime = None
    weekday: str = None
    business_flg: bool = None
    work_start_date: datetime = None
    work_end_date: datetime = None


class BusinessCalendarMtDto():
    """営業日マスタDto
    """

    def __init__(self, entity: BusinessCalendarMt = None):
        """コンストラクタ

        Args:
            entity (BusinessCalendarMt, optional): 営業日マスタ. Defaults to None.
        """

        if entity is None:
            return

        self.seq_business_calendar_mt_id = entity.seq_business_calendar_mt_id
        self.date = entity.date
        self.weekday = entity.weekday
        self.business_flg = entity.business_flg
        self.reg_date = entity.reg_date
        self.update_date = entity.update_date


class DailyUserWorkDataDto():
    """日別ユーザ勤怠情報Dto
    """

    def __init__(self, entity: DailyUserWorkData = None):
        """コンストラクタ

        Args:
            entity (DailyUserWorkData, optional): 日別ユーザ勤怠情報. Defaults to None.
        """

        if entity is None:
            return

        self.seq_daily_user_work_data_id = entity.seq_daily_user_work_data_id
        self.seq_user_id = entity.seq_user_id
        self.company_cd = entity.company_cd
        self.division_cd = entity.division_cd
        self.work_data_reg_date = entity.work_data_reg_date
        self.work_start_date = entity.work_start_date
        self.work_end_date = entity.work_end_date
        self.actual_work_date = entity.actual_work_date
        self.approval_flg = entity.approval_flg
        self.cancel_flg = entity.cancel_flg
        self.note = entity.note
        self.reg_date = entity.reg_date
        self.update_date = entity.update_date
