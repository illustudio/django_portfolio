from django.db import models
from slugger import AutoSlugField
from django.urls import reverse
from taggit.managers import TaggableManager
from taggit.models import (
    TagBase, TaggedItemBase
)


class Artwork(models.Model):
    title = models.CharField(verbose_name="제목", max_length=100)
    slug = AutoSlugField(verbose_name="슬러그", populate_from='title', unique=True, allow_unicode=True)
    description = models.TextField(verbose_name="설명", null=True, blank=True)
    client = models.CharField(verbose_name="클라이언트", null=True, blank=True, max_length=100)
    period = models.IntegerField(verbose_name="작업기간", null=True, blank=True)
    created = models.DateTimeField(verbose_name="작성일자", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="업데이트", auto_now=True)

    class Meta:
        ordering = ['-updated']
        verbose_name = "포트폴리오"
        verbose_name_plural = "작업들"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:artwork_detail', args=[self.id])
