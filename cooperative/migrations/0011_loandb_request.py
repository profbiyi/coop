# Generated by Django 2.0.4 on 2018-04-12 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0010_auto_20180412_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='loandb',
            name='request',
            field=models.CharField(max_length=200, null=True),
        ),
    ]