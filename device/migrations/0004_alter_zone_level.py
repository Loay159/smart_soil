# Generated by Django 4.2.1 on 2023-06-07 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0003_alter_zone_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zone',
            name='level',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
