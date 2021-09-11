from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import RichTextField

class HomePage(Page):

    template = "templates/home/home_page.html"

    privat_description = RichTextField(default="I like travelling")

    business_description = RichTextField(default="Trust me I am an engineer")

    content_panels = Page.content_panels + [
        FieldPanel("privat_description"),
        FieldPanel("business_description")
        ]
