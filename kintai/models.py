import datetime
import decimal
from django.db import models
from django.db.models import Model


class UserData(Model):
    seq_user_id: decimal = models.BigAutoField(db_column="SEQ_USER_ID", primary_key=True, null=False, help_text="ユーザID")
    password: str = models.CharField(db_column="PASSWORD", max_length=64, null=False, help_text="パスワード")
    company_cd: str = models.CharField(db_column="COMPANY_CD", max_length=5, null=False, help_text="企業コード")
    division_cd: str = models.CharField(db_column="DIVISION_CD", default="", max_length=5, null=False, help_text="部署コード")
    del_flg: bool = models.BooleanField(db_column="DEL_FLG", default=False, max_length=5, null=False, help_text="削除フラグ")
    reg_date: datetime = models.DateTimeField(db_column="REG_DATE", auto_now_add=True, null=False, help_text="登録日時")
    update_date: datetime = models.DateTimeField(db_column="UPDATE_DATE", auto_now=True, null=False, help_text="更新日時")

    def __str__(self):
        return "USER_DATA=>"\
            "SEQ_USER_ID=" + str(self.seq_user_id) + \
            ",PASSWORD=" + str(self.password) + \
            ",COMPANY_CD=" + str(self.company_cd) + \
            ",DIVISION_CD=" + str(self.division_cd) + \
            ",DEL_FLG=" + str(self.del_flg) + \
            ",REG_DATE=" + self.reg_date.strftime("%Y/%m/%d %H:%M:%S") + \
            ",UPDATE_DATE=" + self.update_date.strftime("%Y/%m/%d %H:%M:%S")

    class Meta:
        db_table = "USER_DATA"

class UserDataHist(Model):
    seq_user_data_hist_id: decimal = models.BigAutoField(db_column="SEQ_USER_DATA_HIST_ID", primary_key=True, null=False, help_text="ユーザID情報履歴ID")
    seq_user_id: decimal = models.BigIntegerField(db_column="SEQ_USER_ID", null=False, help_text="ユーザID")
    password: str = models.CharField(db_column="PASSWORD", max_length=64, null=False, help_text="パスワード")
    company_cd: str = models.CharField(db_column="COMPANY_CD", max_length=5, null=False, help_text="企業コード")
    division_cd: str = models.CharField(db_column="DIVISION_CD", default="", max_length=5, null=False, help_text="部署コード")
    del_flg: bool = models.BooleanField(db_column="DEL_FLG", default=False, max_length=5, null=False, help_text="削除フラグ")
    reg_date: datetime = models.DateTimeField(db_column="REG_DATE", auto_now_add=True, null=False, help_text="登録日時")
    update_date: datetime = models.DateTimeField(db_column="UPDATE_DATE", auto_now=True, null=False, help_text="更新日時")

    def __str__(self):
        return "USER_DATA_HIST=>"\
            "SEQ_USER_DATA_HIST_ID=" + str(self.seq_user_data_hist_id) + \
            ",SEQ_USER_ID=" + str(self.seq_user_id) + \
            ",PASSWORD=" + str(self.password) + \
            ",COMPANY_CD=" + str(self.company_cd) + \
            ",DIVISION_CD=" + str(self.division_cd) + \
            ",DEL_FLG=" + str(self.del_flg) + \
            ",REG_DATE=" + self.reg_date.strftime("%Y/%m/%d %H:%M:%S") + \
            ",UPDATE_DATE=" + self.update_date.strftime("%Y/%m/%d %H:%M:%S")

    class Meta:
        db_table = "USER_DATA_HIST"

class DailyUserWorkData(Model):
    seq_daily_user_work_data_id: decimal = models.BigAutoField(db_column="SEQ_DAILY_USER_WORK_DATA_ID", primary_key=True, null=False, help_text="日別ユーザ勤怠情報ID")
    seq_user_id: decimal = models.BigIntegerField(db_column="SEQ_USER_ID", null=False, help_text="ユーザID")
    company_cd: str = models.CharField(db_column="COMPANY_CD", max_length=5, null=False, help_text="企業コード")
    division_cd: str = models.CharField(db_column="DIVISION_CD", default="", max_length=5, null=False, help_text="部署コード")
    work_data_reg_date: datetime = models.DateTimeField(db_column="WORK_DATA_REG_DATE", auto_now_add=True, null=False, help_text="勤怠情報登録日時")
    work_start_date: datetime = models.DateTimeField(db_column="WORK_START_DATE", null=False, help_text="始業時刻")
    work_end_date: datetime = models.DateTimeField(db_column="WORK_END_DATE", null=False, help_text="終業時刻")
    actual_work_date: decimal = models.DecimalField(db_column="ACTUAL_WORK_TIME", max_digits=4, decimal_places=2, null=False, help_text="実労働時間")
    rest_time: decimal = models.DecimalField(db_column="REST_TIME", max_digits=4, decimal_places=2, default=0.00, null=False, help_text="休憩時間")
    over_time: decimal = models.DecimalField(db_column="OVER_TIME", max_digits=4, decimal_places=2, null=True, help_text="残業時間")
    approval_flg: bool = models.BooleanField(db_column="APPROVAL_FLG", default=False, null=False, help_text="承認フラグ")
    cancel_flg: bool = models.BooleanField(db_column="CANCEL_FLG", default=False, null=False, help_text="取消申請フラグ")
    note: str = models.CharField(db_column="NOTE", null=True, max_length=128, help_text="備考")
    reg_date: datetime = models.DateTimeField(db_column="REG_DATE", auto_now_add=True, null=False, help_text="登録日時")
    update_date: datetime = models.DateTimeField(db_column="UPDATE_DATE", auto_now=True, null=False, help_text="更新日時")

    def __str__(self):
        return "DAILY_USER_WORK_DATA=>"\
            "SEQ_DAILY_USER_WORK_DATA_ID=" + str(self.seq_daily_user_work_data_id) + \
            ",SEQ_USER_ID=" + str(self.seq_user_id) + \
            ",COMPANY_CD=" + str(self.company_cd) + \
            ",DIVISION_CD=" + str(self.division_cd) + \
            ",WORK_DATA_REG_DATE=" + str(self.work_data_reg_date) + \
            ",WORK_START_DATE=" + str(self.work_start_date) + \
            ",WORK_END_DATE=" + str(self.work_end_date) + \
            ",ACTUAL_WORK_TIME=" + str(self.actual_work_date) + \
            ",REST_TIME=" + str(self.rest_time) + \
            ",OVER_TIME=" + str(self.over_time) + \
            ",APPROVAL_FLG=" + str(self.approval_flg) + \
            ",CANCEL_FLG=" + str(self.cancel_flg) + \
            ",NOTE=" + str(self.note) + \
            ",REG_DATE=" + self.reg_date.strftime("%Y/%m/%d %H:%M:%S") + \
            ",UPDATE_DATE=" + self.update_date.strftime("%Y/%m/%d %H:%M:%S")

    class Meta:
        db_table = "DAILY_USER_WORK_DATA"


class OntimeMt(Model):
    seq_ontime_mt_id: decimal = models.BigAutoField(db_column="SEQ_ONTIME_MT_ID", primary_key=True, null=False, help_text="定時マスタID")
    company_cd: str = models.CharField(db_column="COMPANY_CD", default="", max_length=5, null=False, help_text="企業コード")
    division_cd: str = models.CharField(db_column="DIVISION_CD", default="", max_length=5, null=False, help_text="部署コード")
    start_hour: str = models.CharField(db_column="START_HOUR", max_length=4, null=False, help_text="始業時間(時)")
    start_minute: str = models.CharField(db_column="START_MINUTE", max_length=4, null=False, help_text="始業時間(分)")
    end_hour: str = models.CharField(db_column="END_HOUR", max_length=4, null=False, help_text="終業時間(時)")
    end_minute: str = models.CharField(db_column="END_MINUTE", max_length=4, null=False, help_text="終業時間(分)")
    del_flg: bool = models.BooleanField(db_column="DEL_FLG", default=False, null=False, help_text="削除フラグ")
    reg_date: datetime = models.DateTimeField(db_column="REG_DATE", auto_now_add=True, null=False, help_text="登録日時")
    update_date: datetime = models.DateTimeField(db_column="UPDATE_DATE", auto_now=True, null=False, help_text="更新日時")

    def __str__(self):
        return "ONTIME_MT=>"\
            ",SEQ_ONTIME_MT_ID=" + str(self.seq_ontime_mt_id) + \
            ",COMPANY_CD=" + str(self.company_cd) + \
            ",DIVISION_CD=" + str(self.division_cd) + \
            ",START_HOUR=" + str(self.start_hour) + \
            ",START_MINUTE=" + str(self.start_minute) + \
            ",END_HOUR=" + str(self.end_hour) + \
            ",END_MINUTE=" + str(self.end_minute) + \
            ",DEL_FLG=" + str(self.del_flg) + \
            ",REG_DATE=" + self.reg_date.strftime("%Y/%m/%d %H:%M:%S") + \
            ",UPDATE_DATE=" + self.update_date.strftime("%Y/%m/%d %H:%M:%S")

    class Meta:
        db_table = "ONTIME_MT"
        constraints = [
            # 企業コードと部署コードでuniqueとする
            models.UniqueConstraint(fields=["company_cd", "division_cd"], name="unique_ontime_mt")
        ]


class CompanyMt(Model):
    company_cd: str = models.CharField(db_column="COMPANY_CD", primary_key=True, max_length=5, null=False, help_text="企業コード")
    name: str = models.CharField(db_column="NAME", max_length=64, null=True, help_text="企業名")
    del_flg: bool = models.BooleanField(db_column="DEL_FLG", default=False, null=False, help_text="削除フラグ")
    reg_date: datetime = models.DateTimeField(db_column="REG_DATE", auto_now_add=True, null=False, help_text="登録日時")
    update_date: datetime = models.DateTimeField(db_column="UPDATE_DATE", auto_now=True, null=False, help_text="更新日時")

    def __str__(self):
        return "COMPANY_MT=>"\
            "COMPANY_CD=" + str(self.company_cd) + \
            ",NAME=" + str(self.name) + \
            ",DEL_FLG=" + str(self.del_flg) + \
            ",REG_DATE=" + self.reg_date.strftime("%Y/%m/%d %H:%M:%S") + \
            ",UPDATE_DATE=" + self.update_date.strftime("%Y/%m/%d %H:%M:%S")

    class Meta:
        db_table = "COMPANY_MT"


class DivisionMt(Model):
    division_cd: str = models.CharField(db_column="DIVISION_CD", primary_key=True, max_length=5, null=False, help_text="部署コード")
    name: str = models.CharField(db_column="NAME", max_length=64, null=True, help_text="部署名")
    del_flg: bool = models.BooleanField(db_column="DEL_FLG", default=False, null=False, help_text="削除フラグ")
    reg_date: datetime = models.DateTimeField(db_column="REG_DATE", auto_now_add=True, null=False, help_text="登録日時")
    update_date: datetime = models.DateTimeField(db_column="UPDATE_DATE", auto_now=True, null=False, help_text="更新日時")

    def __str__(self):
        return "DIVISION_MT=>"\
            "DIVISION_CD=" + str(self.division_cd) + \
            ",NAME=" + str(self.name) + \
            ",DEL_FLG=" + str(self.del_flg) + \
            ",REG_DATE=" + self.reg_date.strftime("%Y/%m/%d %H:%M:%S") + \
            ",UPDATE_DATE=" + self.update_date.strftime("%Y/%m/%d %H:%M:%S")

    class Meta:
        db_table = "DIVISION_MT"


class BusinessCalendarMt(Model):
    seq_business_calendar_mt_id: decimal = models.BigAutoField(db_column="SEQ_BUSINESS_CALENDAR_MT_ID", primary_key=True, null=False, help_text="営業日マスタID")
    date: datetime.date = models.DateField(db_column="DATE", null=False, help_text="日付")
    weekday: str = models.CharField(db_column="WEEKDAY", max_length=1, null=False, help_text="曜日")
    business_flg: bool = models.BooleanField(db_column="BUSINESS_FLG", default=True, null=False, help_text="営業日フラグ")
    reg_date: datetime = models.DateTimeField(db_column="REG_DATE", auto_now_add=True, null=False, help_text="登録日時")
    update_date: datetime = models.DateTimeField(db_column="UPDATE_DATE", auto_now=True, null=False, help_text="更新日時")

    def __str__(self):
        return "BUSINESS_CALENDAR_MT=>"\
            "SEQ_BUSINESS_CALENDAR_MT_ID=" + str(self.seq_business_calendar_mt_id) + \
            ",DATE=" + str(self.date) + \
            ",WEEKDAY=" + str(self.weekday) + \
            ",BUSINESS_FLG=" + str(self.business_flg) + \
            ",REG_DATE=" + self.reg_date.strftime("%Y/%m/%d %H:%M:%S") + \
            ",UPDATE_DATE=" + self.update_date.strftime("%Y/%m/%d %H:%M:%S")

    class Meta:
        db_table = "BUSINESS_CALENDAR_MT"
