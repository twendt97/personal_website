from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.admin.edit_handlers import RichTextField
from wagtail.core.fields import StreamField

from streams import blocks

class HomePage(Page):
    """Home page class"""

    template = "home/home_page.html"

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock())
        ],
        null = True,
        blank = True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("content")
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
