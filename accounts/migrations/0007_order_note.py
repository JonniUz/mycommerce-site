# Generated by Django 3.1.5 on 2021-07-10 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210710_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]