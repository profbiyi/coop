# Generated by Django 2.0.4 on 2018-04-17 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0019_loanstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loandb',
            name='admin_approved',
        ),
        migrations.RemoveField(
            model_name='loandb',
            name='gurantor_status',
        ),
    ]
