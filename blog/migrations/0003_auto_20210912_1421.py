# Generated by Django 3.1.8 on 2021-09-12 14:21

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210912_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=wagtail.core.fields.StreamField([('cards', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(help_text='Section Heading', required=False)), ('content', wagtail.core.blocks.RichTextBlock(features=['ol', 'ul', 'link'], help_text='Write the subsection here', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))]))], blank=True, null=True),
        ),
    ]
