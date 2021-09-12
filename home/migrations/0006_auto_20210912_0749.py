# Generated by Django 3.1.8 on 2021-09-12 07:49

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210503_2043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Home Page', 'verbose_name_plural': 'Home Pages'},
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='business_description',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='privat_description',
        ),
        migrations.AddField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your Title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add your Text', required=True))]))], blank=True, null=True),
        ),
    ]
