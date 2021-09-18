from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField

from streams import blocks

class HomePage(Page):
    """Home page class"""

    template = "home/home_page.html"

    author_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    welcome_text = models.TextField(
        blank=False,
        null=True,
        help_text='Welcome text on the Home Page',
        max_length=100
    )

    image_caption = models.TextField(
        blank=False,
        null=True,
        help_text='Caption below the image of the Author',
        max_length=100
    )

    content = StreamField(
        [
            ("subject", blocks.SubjectBlock())
        ],
        null = True,
        blank = True
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('welcome_text'),
                ImageChooserPanel('author_image'),
                FieldPanel('image_caption'),
            ],
            heading="Welcome Section",
            classname="collapsible"
        ),
        StreamFieldPanel("content")
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
