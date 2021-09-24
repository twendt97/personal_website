# Generated by Django 3.1.8 on 2021-09-24 16:51

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogindex_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=wagtail.core.fields.StreamField([('cards', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(help_text='Section Heading', required=False)), ('content', wagtail.core.blocks.RichTextBlock(features=['ol', 'ul', 'link'], help_text='Write the subsection here', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('gallery_images', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(required=True)))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='summary',
            field=models.TextField(help_text='Write a summary of your blog post here', max_length=250, null=True),
        ),
    ]
