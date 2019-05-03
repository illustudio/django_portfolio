from django.db import models
from slugger import AutoSlugField
from taggit.managers import TaggableManager
from taggit.models import (
    TagBase, TaggedItemBase
)




class Artwork(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True, allow_unicode=True)
    description = models.TextField(null=True)
    period = models.IntegerField()
