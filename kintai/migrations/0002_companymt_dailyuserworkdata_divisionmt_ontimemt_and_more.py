# Generated by Django 4.1 on 2023-09-12 13:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kintai", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompanyMt",
            fields=[
                (
                    "company_cd",
                    models.CharField(
                        db_column="COMPANY_CD",
                        help_text="企業コード",
                        max_length=5,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_column="NAME", help_text="企業名", max_length=64, null=True
                    ),
                ),
                (
                    "reg_date",
                    models.DateTimeField(
                        auto_now_add=True, db_column="REG_DATE", help_text="登録日時"
                    ),
                ),
                (
                    "update_date",
                    models.DateTimeField(
                        auto_now=True, db_column="UPDATE_DATE", help_text="更新日時"
                    ),
                ),
            ],
            options={
                "db_table": "COMPANY_MT",
            },
        ),
        migrations.CreateModel(
            name="DailyUserWorkData",
            fields=[
                (
                    "seq_daily_user_work_data_id",
                    models.BigAutoField(
                        db_column="SEQ_DAILY_USER_WORK_DATA_ID",
                        help_text="日別ユーザ勤怠情報ID",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "seq_user_id",
                    models.BigIntegerField(db_column="SEQ_USER_ID", help_text="ユーザID"),
                ),
                (
                    "company_cd",
                    models.CharField(
                        db_column="COMPANY_CD", help_text="企業コード", max_length=5
                    ),
                ),
                (
                    "work_data_reg_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        db_column="WORK_DATA_REG_DATE",
                        help_text="勤怠情報登録日時",
                    ),
                ),
                (
                    "work_start_date",
                    models.CharField(
                        db_column="WORK_START_DATE", help_text="始業時刻", max_length=4
                    ),
                ),
                (
                    "work_end_date",
                    models.CharField(
                        db_column="WORK_END_DATE", help_text="終業時刻", max_length=4
                    ),
                ),
                (
                    "actual_work_date",
                    models.CharField(
                        db_column="ACTUAL_WORK_TIME", help_text="実労働時間", max_length=4
                    ),
                ),
                (
                    "reg_date",
                    models.DateTimeField(
                        auto_now_add=True, db_column="REG_DATE", help_text="登録日時"
                    ),
                ),
                (
                    "update_date",
                    models.DateTimeField(
                        auto_now=True, db_column="UPDATE_DATE", help_text="更新日時"
                    ),
                ),
            ],
            options={
                "db_table": "DAILY_USER_WORK_DATA",
            },
        ),
        migrations.CreateModel(
            name="DivisionMt",
            fields=[
                (
                    "division_cd",
                    models.CharField(
                        db_column="DIVISION_CD",
                        help_text="部署コード",
                        max_length=5,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_column="NAME", help_text="部署名", max_length=64, null=True
                    ),
                ),
                (
                    "reg_date",
                    models.DateTimeField(
                        auto_now_add=True, db_column="REG_DATE", help_text="登録日時"
                    ),
                ),
                (
                    "update_date",
                    models.DateTimeField(
                        auto_now=True, db_column="UPDATE_DATE", help_text="更新日時"
                    ),
                ),
            ],
            options={
                "db_table": "DIVISION_MT",
            },
        ),
        migrations.CreateModel(
            name="OntimeMt",
            fields=[
                (
                    "seq_ontime_mt_id",
                    models.BigAutoField(
                        db_column="SEQ_ONTIME_MT_ID",
                        help_text="日別ユーザ勤怠情報ID",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "company_cd",
                    models.CharField(
                        db_column="COMPANY_CD",
                        default="",
                        help_text="企業コード",
                        max_length=5,
                    ),
                ),
                (
                    "division_cd",
                    models.CharField(
                        db_column="DIVISION_CD",
                        default="",
                        help_text="部署マスタコード",
                        max_length=5,
                    ),
                ),
                (
                    "start_hour",
                    models.CharField(
                        db_column="START_HOUR", help_text="始業時間(時)", max_length=4
                    ),
                ),
                (
                    "start_minute",
                    models.CharField(
                        db_column="START_MINUTE", help_text="始業時間(分)", max_length=4
                    ),
                ),
                (
                    "end_hour",
                    models.CharField(
                        db_column="END_HOUR", help_text="終業時間(時)", max_length=4
                    ),
                ),
                (
                    "end_minute",
                    models.CharField(
                        db_column="END_MINUTE", help_text="終業時間(分)", max_length=4
                    ),
                ),
                (
                    "reg_date",
                    models.DateTimeField(
                        auto_now_add=True, db_column="REG_DATE", help_text="登録日時"
                    ),
                ),
                (
                    "update_date",
                    models.DateTimeField(
                        auto_now=True, db_column="UPDATE_DATE", help_text="更新日時"
                    ),
                ),
            ],
            options={
                "db_table": "ONTIME_MT",
            },
        ),
        migrations.AddConstraint(
            model_name="ontimemt",
            constraint=models.UniqueConstraint(
                fields=("company_cd", "division_cd"), name="unique_ontime_mt"
            ),
        ),
    ]
