from django.db import models
from django.db.models import Model


class UserData(Model):
    seq_user_id = models.BigAutoField(
        primary_key=True, null=False, help_text='ユーザID')
    password = models.CharField(max_length=64, null=False, help_text='パスワード')
    company_cd = models.CharField(max_length=5, null=False, help_text='企業コード')
    reg_date = models.DateTimeField(
        auto_now_add=True, null=False, help_text='登録日時')
    update_date = models.DateTimeField(
        auto_now=True, null=False, help_text='更新日時')

    def __str__(self):
        return "USER_DATA=>"\
            "SEQ_USER_ID=" + str(self.seq_user_id) + \
            ",PASSWORD=" + str(self.password) + \
            ",COMPANY_CD=" + str(self.company_cd) + \
            ",REG_DATE=" + str(self.reg_date) + \
            ",UPDATE_DATE=" + str(self.update_date)

    class Meta:
        db_table = "USER_DATA"


class DailyUserWorkData(Model):
    daily_user_work_data_id = models.BigAutoField(
        primary_key=True, null=False, help_text='日別ユーザ勤怠情報ID')
    seq_user_id = models.BigIntegerField(null=False, help_text='ユーザID')
    company_cd = models.CharField(max_length=5, null=False, help_text='企業コード')
    work_data_reg_date = models.DateTimeField(
        auto_now_add=True, null=False, help_text='勤怠情報登録日時')
    work_start_date = models.CharField(
        max_length=4, null=False, help_text='始業時刻')
    work_end_date = models.CharField(
        max_length=4, null=False, help_text='終業時刻')
    actual_work_date = models.CharField(
        max_length=4, null=False, help_text='実労働時間')
    reg_date = models.DateTimeField(
        auto_now_add=True, null=False, help_text='登録日時')
    update_date = models.DateTimeField(
        auto_now=True, null=False, help_text='更新日時')

    def __str__(self):
        return "DAILY_USER_WORK_DATA=>"\
            "DAILY_USER_WORK_DATA_ID=" + str(self.daily_user_work_data_id) + \
            ",SEQ_USER_ID=" + str(self.seq_user_id) + \
            ",COMPANY_CD=" + str(self.company_cd) + \
            ",WORK_DATA_REG_DATE=" + str(self.work_data_reg_date) + \
            ",WORK_START_DATE=" + str(self.work_start_date) + \
            ",WORK_END_DATE=" + str(self.work_end_date) + \
            ",ACTUAL_WORK_TIME=" + str(self.actual_work_date) + \
            ",REG_DATE=" + str(self.reg_date) + \
            ",UPDATE_DATE=" + str(self.update_date)

    class Meta:
        db_table = "DAILY_USER_WORK_DATA"


class OntimeMt(Model):
    company_cd = models.CharField(
        primary_key=True, max_length=5, null=False, help_text='企業コード')
    start_hour = models.CharField(
        max_length=4, null=False, help_text='始業時間(時)')
    start_minute = models.CharField(
        max_length=4, null=False, help_text='始業時間(分)')
    end_hour = models.CharField(max_length=4, null=False, help_text='終業時間(時)')
    end_minute = models.CharField(
        max_length=4, null=False, help_text='終業時間(分)')
    reg_date = models.DateTimeField(
        auto_now_add=True, null=False, help_text='登録日時')
    update_date = models.DateTimeField(
        auto_now=True, null=False, help_text='更新日時')

    def __str__(self):
        return "ONTIME_MT=>"\
            "COMPANY_CD=" + str(self.company_cd) + \
            ",START_HOUR=" + str(self.start_hour) + \
            ",START_MINUTE=" + str(self.start_minute) + \
            ",END_HOUR=" + str(self.end_hour) + \
            ",END_MINUTE=" + str(self.end_minute) + \
            ",REG_DATE=" + str(self.reg_date) + \
            ",UPDATE_DATE=" + str(self.update_date)

    class Meta:
        db_table = "ONTIME_MT"


class CompanyMt(Model):
    company_cd = models.CharField(
        primary_key=True, max_length=5, null=False, help_text='企業コード')
    name = models.CharField(max_length=64, null=False, help_text='企業名')
    reg_date = models.DateTimeField(
        auto_now_add=True, null=False, help_text='登録日時')
    update_date = models.DateTimeField(
        auto_now=True, null=False, help_text='更新日時')

    def __str__(self):
        return "COMPANY_MT=>"\
            "COMPANY_CD=" + str(self.company_cd) + \
            ",NAME=" + str(self.name) + \
            ",REG_DATE=" + str(self.reg_date) + \
            ",UPDATE_DATE=" + str(self.update_date)

    class Meta:
        db_table = "COMPANY_MT"
