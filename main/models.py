from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Category(models.Model):
    c_name = models.CharField(_("Category Name"), max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CategoryTag(models.Model):
    c_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag_name = models.CharField(_("Tag Name"), max_length=40)

class Location(models.Model):
    image = models.FileField(upload_to='spot')
    l_name = models.CharField(_("Hotel Name"), max_length=50)
    l_tagline = models.CharField(_("Hotel Tagline"), max_length=150)
    l_summery = models.TextField(_("Hotel Summary"), max_length=300)
    l_description = models.TextField(_("Hotel Description"), max_length=200)
    tags = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.l_name

class Season(models.Model):
    s_tagline = models.CharField(_("Season Tagline"), max_length=100)
    s_name = models.CharField(_("Season Name"), max_length=50)
    s_description = models.TextField(_("Season Description"), max_length=250)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.s_name

class Feature(models.Model):
    sf_title = models.CharField(_("Title"), max_length=50)
    sf_description = models.TextField(_("Description"), max_length=150)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return self.sf_title