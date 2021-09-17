# Generated by Django 3.1.8 on 2021-09-17 17:17

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210917_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('subject', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your Title', required=True)), ('subtitle', wagtail.core.blocks.TextBlock(help_text='Add a Subtitle', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False))]))], blank=True, null=True),
        ),
    ]
