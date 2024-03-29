# Generated by Django 3.1.8 on 2021-09-12 09:18

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210912_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='my_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('cards', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False))])))]))], blank=True, null=True),
        ),
    ]
