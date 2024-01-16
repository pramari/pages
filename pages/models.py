from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager

from wagtail import blocks
from wagtail.search import index
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel


from taggit.models import TaggedItemBase


from wagtailmetadata.models import MetadataPageMixin


class HomeIndexPage(Page):
    """
    This is an index for all page content.
    """

    class Meta:
        verbose_name = "Index Page"

    intro = RichTextField(blank=True)
    require_registration = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full"),
        FieldPanel("require_registration"),
    ]


class HomePage(MetadataPageMixin, Page):
    class Meta:
        verbose_name = "Home Page"

    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)
    icon = models.CharField(max_length=64, default="files")
    date = models.DateField("Post date", null=True, blank=True)
    require_registration = models.BooleanField(default=False)
    frontpage = models.BooleanField(default=False)  # show on frontpage yes/no?

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
        FieldPanel("icon"),
        FieldPanel("date"),
        InlinePanel("related_links", heading="Related links", label="Related link"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        FieldPanel("frontpage"),
        FieldPanel("require_registration"),
    ]

    # Search index configuration

    search_fields = Page.search_fields + [
        index.SearchField("body"),
        index.FilterField("date"),
    ]

    def get_meta_title(self):
        """The title of this object"""
        return "My custom object"

    def get_meta_url(self):
        """The URL of this object, including protocol and domain"""
        return "http://example.com/my-custom-object/"

    def get_meta_description(self):
        """
        A short text description of this object.
        This should be plain text, not HTML.
        """
        return "This thing is really cool, you should totally check it out"

    def get_meta_image_url(self, request):
        """
        Return a url for an image to use, see the MetadataPageMixin if using a Wagtail image
        """
        return "https://neonjungle.studio/share.png"

    def get_meta_twitter_card_type(self):
        """
        What kind of Twitter card to show this as.
        Defaults to ``summary_large_photo`` if there is a meta image,
        or ``summary`` if there is no image. Optional.
        """
        return "summary_large_photo"


class HomePageRelatedLink(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name="related_links")
    name = models.CharField(max_length=255)
    url = models.URLField()

    panels = [
        FieldPanel("name"),
        FieldPanel("url"),
    ]


class MethodPageTag(TaggedItemBase):
    content_object = ParentalKey(
        "pages.MethodPage", on_delete=models.CASCADE, related_name="tagged_methods"
    )


class MethodPage(MetadataPageMixin, Page):
    class Meta:
        verbose_name = "method"

    date = models.DateField("Date")
    benefit = RichTextField()
    method_input = RichTextField()
    method_output = RichTextField()
    why = RichTextField()
    how = StreamField(
        [
            ("heading", blocks.CharBlock(form_classname="title")),
            ("paragraph", blocks.RichTextBlock()),
            ("image", ImageChooserBlock()),
        ],
        use_json_field=True,
    )
    tags = ClusterTaggableManager(through=MethodPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("benefit"),
        FieldPanel("method_input"),
        FieldPanel("method_output"),
        FieldPanel("why"),
        FieldPanel("how"),
        FieldPanel("tags"),
    ]

    def get_meta_title(self):
        """The title of this object"""
        return "My custom object"

    def get_meta_url(self):
        """The URL of this object, including protocol and domain"""
        return "http://example.com/my-custom-object/"

    def get_meta_description(self):
        """
        A short text description of this object.
        This should be plain text, not HTML.
        """
        return "This thing is really cool, you should totally check it out"

    def get_meta_image_url(self, request):
        """
        Return a url for an image to use, see the MetadataPageMixin if using a Wagtail image
        """
        return "https://neonjungle.studio/share.png"

    def get_meta_twitter_card_type(self):
        """
        What kind of Twitter card to show this as.
        Defaults to ``summary_large_photo`` if there is a meta image,
        or ``summary`` if there is no image. Optional.
        """
        return "summary_large_photo"


"""
class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]



class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
    ]
"""
