from django.db import models
from django.db.models.fields import Field

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.admin.edit_handlers import RichTextField
from wagtail.core.fields import StreamField

from streams import blocks

class HomePage(Page):
    """Home page class"""

    template = "home/home_page.html"

    my_title = models.CharField(max_length=100, blank=False, null=True)

    content = StreamField(
        [
            ("cards", blocks.CardBlock())
        ],
        null = True,
        blank = True
    )

    content_panels = Page.content_panels + [
        FieldPanel("my_title"),
        StreamFieldPanel("content")
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
