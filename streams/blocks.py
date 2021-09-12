"""Stream fields live here"""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text='Add your Title')
    text = blocks.TextBlock(required=True, help_text='Add your Text')

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class CardBlock(blocks.StructBlock):
    """Cards with image and Title"""

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required = True)),
                ("title", blocks.CharBlock(required = True, max_length = 40)),
                ("button_page", blocks.PageChooserBlock(required=False))
            ]
        )
    )

    class Meta :
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Cards"