# Generated by Django 4.1 on 2023-09-18 22:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kintai", "0005_businesscalendarmt"),
    ]

    operations = [
        migrations.RenameField(
            model_name="businesscalendarmt",
            old_name="seqBusinessCalendarMtId",
            new_name="seq_business_calendar_mt_id",
        ),
        migrations.AlterField(
            model_name="businesscalendarmt",
            name="weekday",
            field=models.CharField(db_column="WEEKDAY", help_text="曜日", max_length=1),
        ),
    ]