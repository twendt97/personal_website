"""Stream fields live here"""
from wagtail.core import blocks
from wagtail.core.blocks.field_block import CharBlock
from wagtail.images.blocks import ImageChooserBlock


class BlogItemBlock(blocks.StructBlock):
    """Holds a part of a blog post"""

    heading = blocks.CharBlock(required=False, help_text='Section Heading')
    content = blocks.RichTextBlock(required=True,
        features=['ol','ul','link'],
        help_text='Write the subsection here'
    )

    gallery_images = blocks.ListBlock(
        ImageChooserBlock(required=True),
        label="Gallery Images"
    )

    class Meta:
        template = "streams/blog_item_block.html"
        icon = "edit"
        label = "Subsection"

class SubjectBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Add your Title')
    subtitle = blocks.TextBlock(required=True, help_text='Add a Subtitle')
    image = ImageChooserBlock(required = True)
    button_page = blocks.PageChooserBlock(required=False)

    class Meta:
        template = "streams/subject_block.html"
        icon = "edit"
        label = "Presentation of a Subject"