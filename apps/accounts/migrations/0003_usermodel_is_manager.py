# Generated by Django 4.2.6 on 2023-11-04 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_groupmodel_table_alter_usermodel_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
    ]
