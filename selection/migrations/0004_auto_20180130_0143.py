# Generated by Django 2.0 on 2018-01-30 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0003_auto_20180130_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classdata',
            name='isgn',
            field=models.CharField(choices=[('1234', '1234')], max_length=30),
        ),
    ]
