from __future__ import unicode_literals

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField( max_length=31, unique=True, help_text='A label for URL config')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Startup(models.Model):
    name = models.CharField(max_length=31, db_index=True)
    slug = models.SlugField(max_length=31, unique=True, help_text='A label for URL config')
    description = models.TextField()
    founded_date = models.DateField('date_founded')
    contact =  models.EmailField()
    website = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'

class NewsLink(models.Model):
    title = models.CharField(max_length=63)
    pub_date = models.DateField('date_published')
    link = models.URLField(max_length=255)
    startup = models.ForeignKey(Startup)

    def __str__(self):
        return "{}:{}".format(self.startaup, self.title)

    verbose_name = 'news article'
    ordering = ['-pub_date'] #  Dash in front defines our direction of ordering.  Switches order from ascending to descending
    get_latest_by = 'pub_date'
