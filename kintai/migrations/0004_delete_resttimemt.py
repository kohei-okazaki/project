# Generated by Django 4.1 on 2023-10-14 01:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("kintai", "0003_resttimemt_alter_ontimemt_seq_ontime_mt_id_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="RestTimeMt",
        ),
    ]