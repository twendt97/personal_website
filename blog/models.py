from django.db import models
from datetime import date

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField

from streams import blocks
# Create your models here.


class BlogPost(Page):
    """Page that holds an individual blog post"""
    template ="blog/blog_post.html"

    custom_title = models.CharField(max_length=20,
        blank=False,
        null=True, 
        help_text="This title is displayed on the page")
    
    author = models.CharField(max_length=50, blank=False, null=True, default="Thilo")
    date = models.DateField("Post date",default=date.today)
    summary = models.TextField(
        blank=False,
        null=True,
        help_text='Write a summary of your blog post here',
        max_length=250
    )

    thumbnail = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content = StreamField(
        [
            ("cards", blocks.BlogItemBlock())
        ],
        null = True,
        blank = True
    )

    content_panels = Page.content_panels + [
        FieldPanel('custom_title'),
        MultiFieldPanel(
            [
                FieldPanel('summary'),
                ImageChooserPanel('thumbnail'),
            ],
            heading="Thumbnail on Blog Index Page",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('author'),
                FieldPanel('date'),
            ],
            heading="Meta data of the post",
            classname="collapsible collapsed"
        ),
        StreamFieldPanel('content'),
    ]

# Parent page / subpage type rules

    parent_page_types = ['blog.BlogIndex']
    subpage_types = []


class BlogIndex(Page):
    """Index Page that displays a summary of the blog posts"""

    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        help_text='Overwrites the default title',
    )

    description = models.TextField(
        blank=False,
        null=True,
        help_text='Write a description of the journey',
    )


    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("description"),
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = BlogPost.objects.live().public().order_by('-first_published_at')

        context["posts"] = all_posts
        return context

    template ="blog/blog_index.html"