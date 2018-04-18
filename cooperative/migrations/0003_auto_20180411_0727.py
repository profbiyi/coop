# Generated by Django 2.0.4 on 2018-04-11 07:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cooperative', '0002_auto_20180411_0643'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_approved', models.BooleanField(default=False)),
                ('guarantor_name', models.ForeignKey(on_delete='CASSCADE', related_name='guarantee', to=settings.AUTH_USER_MODEL)),
                ('own', models.ForeignKey(on_delete='CASSCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='loan',
            name='admin_declined',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='fulfilled',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='guaranted',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='guarantor',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='guarantor_declined',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='start_date',
        ),
        migrations.AddField(
            model_name='loan',
            name='tenure',
            field=models.CharField(max_length=244, null=True),
        ),
    ]