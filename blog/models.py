from django.db import models
from django.db.models.fields import Field
from datetime import date

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.admin.edit_handlers import RichTextField
from wagtail.core.fields import StreamField

from streams import blocks
# Create your models here.


class BlogPost(Page):
    """Page that holds an individual blog post"""
    template ="blog/blog_post.html"

    author = models.CharField(max_length=50, blank=False, null=True, default="Thilo")
    date = models.DateField("Post date",default=date.today)
    summary = models.TextField(
        blank=False,
        null=True,
        help_text='Write a summary of your blog post here',
        max_length=500
    )

    content = StreamField(
        [
            ("cards", blocks.BlogItemBlock())
        ],
        null = True,
        blank = True
    )

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('summary'),
        StreamFieldPanel('content'),
    ]

# Parent page / subpage type rules

    parent_page_types = ['blog.BlogIndex']
    subpage_types = []


class BlogIndex(Page):
    """Index Page that displays a summary of the blog posts"""
    template ="blog/blog_index.html"