from __future__ import unicode_literals

from django.db import models
from organizer.models import Startup, Tag


class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63, help_text='A lable for URL config', unique_for_month="pub_date")
    text = models.TextField()
    pub_date = models.DateField('date_published', auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    startups = models.ManyToManyField(Startup)

    def __str__(self):
        return "{} on {}".format(
            self.title,
            self.pub_date.strftime('%Y-%m-%d'))


    class Meta:
        verbose_name = 'blog post'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'
