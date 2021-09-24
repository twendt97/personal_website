# Generated by Django 3.1.8 on 2021-09-24 17:49

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210924_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=wagtail.core.fields.StreamField([('cards', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(help_text='Section Heading', required=False)), ('content', wagtail.core.blocks.RichTextBlock(features=['ol', 'ul', 'link'], help_text='Write the subsection here', required=True)), ('gallery_images', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(required=True), label='Gallery Images'))]))], blank=True, null=True),
        ),
    ]
