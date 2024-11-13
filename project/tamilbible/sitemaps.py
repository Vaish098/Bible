from django.contrib.sitemaps import Sitemap
from django.urls  import reverse
from .models import BilbleDb
from django.utils.text import slugify
from datetime import datetime





class StaticViewSitemap(Sitemap):

    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['index','songslist']

    def location(self, item):
        return reverse(item)




class songsSitemap(Sitemap):

    def items(self):
        return BilbleDb.objects.all()


    def location(self,obj):
         url=obj.url
         id=obj.id
         return '/tamil-christian-songs/%s' %(slugify(url))
