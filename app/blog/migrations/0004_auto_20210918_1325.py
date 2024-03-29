# Generated by Django 3.1.8 on 2021-09-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210912_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindex',
            name='custom_title',
            field=models.CharField(help_text='Overwrites the default title', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='custom_title',
            field=models.CharField(help_text='This title is displayed on the page', max_length=20, null=True),
        ),
    ]
