# Generated by Django 3.0.3 on 2020-03-20 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200320_1837'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vinfo',
        ),
        migrations.RemoveField(
            model_name='cinfo',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='cinfo',
            name='Code',
        ),
        migrations.RemoveField(
            model_name='cinfo',
            name='PhoneNo',
        ),
    ]
