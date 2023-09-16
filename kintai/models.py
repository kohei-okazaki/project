from django.db import models
from django.db.models import Model


class UserData(Model):
    seq_user_id = models.BigAutoField(db_column="SEQ_USER_ID", primary_key=True, null=False, help_text='ユーザID')
    password = models.CharField(db_column="PASSWORD", max_length=64, null=False, help_text='パスワード')
    company_cd = models.CharField(db_column="COMPANY_CD", max_length=5, null=False, help_text='企業コード')
    division_cd = models.CharField(db_column="DIVISION_CD", default="", max_length=5, null=False, help_text='部署コード')
    reg_date = models.DateTimeField(db_column="REG_DATE", auto_now_add=True, null=False, help_text='登録日時')
    update_date = models.DateTimeField(db_column="UPDATE_DATE", auto_now=True, null=False, help_text='更新日時')

    def __str__(self):
        return "USER_DATA=>"\
            "SEQ_USER_ID=" + str(self.seq_user_id) + \
            ",PASSWORD=" + str(self.password) + \
            ",COMPANY_CD=" + str(self.company_cd) + \
            ",DIVISION_CD=" + str(self.division_cd) + \
            ",REG_DATE=" + self.reg_date.strftime('%Y/%m/%d %H:%M:%S') + \
            ",UPDATE_DATE=" + self.update_date.strftime('%Y/%m/%d %H:%M:%S')

    class Meta:
        db_table = "USER_DATA"


class DailyUserWorkData(Model):
    seq_daily_user_work_data_id = models.BigAutoField(db_column="SEQ_DAILY_USER_WORK_DATA_ID", primary_key=True, null=False, help_text='日別ユーザ勤怠情報ID')
    seq_user_id = models.BigIntegerField(db_column="SEQ_USER_ID", null=False, help_text='ユーザID')
    company_cd = models.CharField(db_column="COMPANY_CD", max_length=5, null=False, help_text='企業コード')
    division_cd = models.CharField(db_column="DIVISION_CD", default="", max_length=5, null=False, help_text='部署コード')
    work_data_reg_date = models.DateTimeField(db_column="WORK_DATA_REG_DATE", auto_now_add=True, null=False, help_text='勤怠情報登録日時')
    work_start_date = models.CharField(db_column="WORK_START_DATE", max_length=4, null=False, help_text='始業時刻')
    work_end_date = models.CharField(db_column="WORK_END_DATE", max_length=4, null=False, help_text='終業時刻')
    actual_work_date = models.CharField(db_column="ACTUAL_WORK_TIME", max_length=4, null=False, help_text='実労働時間')
    reg_date = models.DateTimeField(db_column="REG_DATE", auto_now_add=True, null=False, help_text='登録日時')
    update_date = models.DateTimeField(db_column="UPDATE_DATE", auto_now=True, null=False, help_text='更新日時')

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
            ",REG_DATE=" + self.reg_date.strftime('%Y/%m/%d %H:%M:%S') + \
            ",UPDATE_DATE=" + self.update_date.strftime('%Y/%m/%d %H:%M:%S')

    class Meta:
        db_table = "DAILY_USER_WORK_DATA"


class OntimeMt(Model):
    seq_ontime_mt_id = models.BigAutoField(db_column="SEQ_ONTIME_MT_ID", primary_key=True, null=False, help_text='日別ユーザ勤怠情報ID')
    company_cd = models.CharField(db_column="COMPANY_CD", default="", max_length=5, null=False, help_text='企業コード')
    division_cd = models.CharField(db_column="DIVISION_CD", default="", max_length=5, null=False, help_text='部署コード')
    start_hour = models.CharField(db_column="START_HOUR", max_length=4, null=False, help_text='始業時間(時)')
    start_minute = models.CharField(db_column="START_MINUTE", max_length=4, null=False, help_text='始業時間(分)')
    end_hour = models.CharField(db_column="END_HOUR", max_length=4, null=False, help_text='終業時間(時)')
    end_minute = models.CharField(db_column="END_MINUTE", max_length=4, null=False, help_text='終業時間(分)')
    reg_date = models.DateTimeField(db_column="REG_DATE", auto_now_add=True, null=False, help_text='登録日時')
    update_date = models.DateTimeField(db_column="UPDATE_DATE", auto_now=True, null=False, help_text='更新日時')

    def __str__(self):
        return "ONTIME_MT=>"\
            ",SEQ_ONTIME_MT_ID=" + str(self.seq_ontime_mt_id) + \
            ",COMPANY_CD=" + str(self.company_cd) + \
            ",DIVISION_CD=" + str(self.division_cd) + \
            ",START_HOUR=" + str(self.start_hour) + \
            ",START_MINUTE=" + str(self.start_minute) + \
            ",END_HOUR=" + str(self.end_hour) + \
            ",END_MINUTE=" + str(self.end_minute) + \
            ",REG_DATE=" + self.reg_date.strftime('%Y/%m/%d %H:%M:%S') + \
            ",UPDATE_DATE=" + self.update_date.strftime('%Y/%m/%d %H:%M:%S')

    class Meta:
        db_table = "ONTIME_MT"
        constraints = [
            # 企業コードと部署コードでuniqueとする
            models.UniqueConstraint(fields=["company_cd", "division_cd"], name="unique_ontime_mt")
        ]


class CompanyMt(Model):
    company_cd = models.CharField(db_column="COMPANY_CD", primary_key=True, max_length=5, null=False, help_text='企業コード')
    name = models.CharField(db_column="NAME", max_length=64, null=True, help_text='企業名')
    reg_date = models.DateTimeField(db_column="REG_DATE", auto_now_add=True, null=False, help_text='登録日時')
    update_date = models.DateTimeField(db_column="UPDATE_DATE", auto_now=True, null=False, help_text='更新日時')

    def __str__(self):
        return "COMPANY_MT=>"\
            "COMPANY_CD=" + str(self.company_cd) + \
            ",NAME=" + str(self.name) + \
            ",REG_DATE=" + self.reg_date.strftime('%Y/%m/%d %H:%M:%S') + \
            ",UPDATE_DATE=" + self.update_date.strftime('%Y/%m/%d %H:%M:%S')

    class Meta:
        db_table = "COMPANY_MT"


class DivisionMt(Model):
    division_cd = models.CharField(db_column="DIVISION_CD", primary_key=True, max_length=5, null=False, help_text='部署コード')
    name = models.CharField(db_column="NAME", max_length=64, null=True, help_text='部署名')
    reg_date = models.DateTimeField(db_column="REG_DATE", auto_now_add=True, null=False, help_text='登録日時')
    update_date = models.DateTimeField(db_column="UPDATE_DATE", auto_now=True, null=False, help_text='更新日時')

    def __str__(self):
        return "DIVISION_MT=>"\
            "DIVISION_CD=" + str(self.division_cd) + \
            ",NAME=" + str(self.name) + \
            ",REG_DATE=" + self.reg_date.strftime('%Y/%m/%d %H:%M:%S') + \
            ",UPDATE_DATE=" + self.update_date.strftime('%Y/%m/%d %H:%M:%S')

    class Meta:
        db_table = "DIVISION_MT"
