from django.db import models


class UserData(models.Model):
    seq_user_id = models.BigAutoField(primary_key=True, help_text='ユーザID')
    password = models.CharField(max_length=64, help_text='パスワード')
    company_code = models.CharField(max_length=5, help_text='企業コード')
    reg_date = models.DateTimeField(auto_now_add=True, help_text='登録日時')
    update_date = models.DateTimeField(auto_now=True, help_text='更新日時')

    def __str__(self):
        return "USER_DATA"\
            "SEQ_USER_ID=" + str(self.seq_user_id) + \
            ",PASSWORD=" + str(self.password) + \
            ",COMPANY_CODE=" + str(self.company_code) + \
            ",REG_DATE=" + str(self.reg_date) + \
            ",UPDATE_DATE=" + str(self.update_date)


class DailyUserWorkData(models.Model):
    daily_user_work_data_id = models.BigAutoField(
        primary_key=True, help_text='日別ユーザ勤怠情報ID')
    seq_user_id = models.BigIntegerField(help_text='ユーザID')
    company_code = models.CharField(max_length=5, help_text='企業コード')
    work_data_reg_date = models.DateTimeField(
        auto_now_add=True, help_text='勤怠情報登録日時')
    work_start_date = models.CharField(max_length=4, help_text='始業時刻')
    work_end_date = models.CharField(max_length=4, help_text='終業時刻')
    actual_work_date = models.CharField(max_length=4, help_text='実労働時間')
    reg_date = models.DateTimeField(auto_now_add=True, help_text='登録日時')
    update_date = models.DateTimeField(auto_now=True, help_text='更新日時')

    def __str__(self):
        return "DAILY_USER_WORK_DATA"\
            "AILY_USER_WORK_DATA_ID=" + str(self.daily_user_work_data_id) + \
            ",SEQ_USER_ID=" + str(self.seq_user_id) + \
            ",COMPANY_CODE=" + str(self.company_code) + \
            ",WORK_DATA_REG_DATE=" + str(self.work_data_reg_date) + \
            ",WORK_START_DATE=" + str(self.work_start_date) + \
            ",WORK_END_DATE=" + str(self.work_end_date) + \
            ",ACTUAL_WORK_TIME=" + str(self.actual_work_date) + \
            ",REG_DATE=" + str(self.reg_date) + \
            ",UPDATE_DATE=" + str(self.update_date)
