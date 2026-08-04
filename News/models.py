from django.db import models
from django.utils.text import slugify 
from .utils import relative_time

class Logo(models.Model):
    logo = models.ImageField(upload_to='images/') 

    def __str__(self):
        return "Logo"


class Slidertxt(models.Model):
    text_slider = models.CharField(max_length=200)

    def __str__(self):
        return self.text_slider


class Newsoftheday(models.Model):
    txt_news = models.CharField(max_length=100)
    title_news = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True, allow_unicode=True) 
    views = models.PositiveIntegerField(default=0)
    img_ftheday = models.ImageField(upload_to='images/')
    page_newsoftheday_title = models.TextField(default='یوخدی')
    pagetxt_newsoftheday = models.CharField(max_length=100 , default='یوخدی')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = f"{slugify(self.title_news[:50], allow_unicode=True)}-{self.id}"
            super().save(update_fields=['slug'])

    def add_view(self):
        Newsoftheday.objects.filter(pk=self.pk).update(views=models.F('views') + 1)
        self.refresh_from_db()

    def __str__(self):
        return self.title_news[:50]


class NewsLifestyle(models.Model):
    begtxt = models.CharField(max_length=100)
    longtitle = models.TextField()
    img_Lifestyle = models.ImageField(upload_to='images/')
    publish_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True, allow_unicode=True) 
    views = models.PositiveIntegerField(default=0)
    page_newsLifestyle_title = models.TextField(default='یوخدی')
    pagetxt_newsLifestyle = models.CharField(max_length=100,default='یوخدی')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = f"{slugify(self.longtitle[:50], allow_unicode=True)}-{self.id}"
            super().save(update_fields=['slug'])

    def add_view(self):
        NewsLifestyle.objects.filter(pk=self.pk).update(views=models.F('views') + 1)
        self.refresh_from_db()

    def __str__(self):
        return self.longtitle[:50]


class NewsDecoration(models.Model):
    text = models.CharField(max_length=100)
    title = models.TextField()
    img_Decoration = models.ImageField(upload_to='images/')
    publish_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True, allow_unicode=True) 
    views = models.PositiveIntegerField(default=0)
    page_newsDecoration_title = models.TextField(default='یوخدی')
    pagetxt_newsDecoration = models.CharField(max_length=100,default='یوخدی')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = f"{slugify(self.title[:50], allow_unicode=True)}-{self.id}"
            super().save(update_fields=['slug'])

    def add_view(self):
        NewsDecoration.objects.filter(pk=self.pk).update(views=models.F('views') + 1)
        self.refresh_from_db()

    def __str__(self):
        return self.title[:50]


class NewsTechnology(models.Model):
    matn = models.CharField(max_length=100) 
    explanation = models.TextField()
    img_Technology = models.ImageField(upload_to='images/')
    publish_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True, allow_unicode=True) 
    views = models.PositiveIntegerField(default=0)
    page_newsTechnology_title = models.TextField(default='یوخدی')
    pagetxt_newsTechnology= models.CharField(max_length=100,default='یوخدی')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = f"{slugify(self.explanation[:50], allow_unicode=True)}-{self.id}"
            super().save(update_fields=['slug'])

    def add_view(self):
        NewsTechnology.objects.filter(pk=self.pk).update(views=models.F('views') + 1)
        self.refresh_from_db()

    def __str__(self):
        return self.explanation[:50]


class NewsArtculture(models.Model):
    dodslg = models.CharField(max_length=100)
    Artculture_title = models.TextField()
    img_Artculture = models.ImageField(upload_to='images/')
    publish_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True, allow_unicode=True) 
    views = models.PositiveIntegerField(default=0)
    page_newsArtculture_title = models.TextField(default='یوخدی')
    pagetxt_newsArtculture = models.CharField(max_length=100,default='یوخدی')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = f"{slugify(self.Artculture_title[:50], allow_unicode=True)}-{self.id}"
            super().save(update_fields=['slug'])

    def add_view(self):
        NewsArtculture.objects.filter(pk=self.pk).update(views=models.F('views') + 1)
        self.refresh_from_db()

    def __str__(self):
        return self.Artculture_title[:50]


class Slidernews(models.Model):
    Typenews = models.CharField(max_length=30)
    category_tag = models.CharField(max_length=100)
    display_title = models.TextField()
    slider_image = models.ImageField(upload_to='images/') 
    publish_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True, allow_unicode=True) 
    views = models.PositiveIntegerField(default=0)
    page_slidernews_title = models.TextField(default='یوخدی')
    pagetxt_slidernews = models.CharField(max_length=100,default='یوخدی')


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = f"{slugify(self.display_title[:50], allow_unicode=True)}-{self.id}"
            super().save(update_fields=['slug'])

    def add_view(self):
        Slidernews.objects.filter(pk=self.pk).update(views=models.F('views') + 1)
        self.refresh_from_db()

    def __str__(self):
        return self.display_title[:50]





class Coment(models.Model):
    news_slug = models.CharField(max_length=200, null=True, blank=True)
    coment_usernameandlastname = models.CharField(max_length=50, verbose_name="نام و نام خانوادگی")
    coment_title = models.CharField(max_length=300, verbose_name="متن نظر")
    imguser = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="تصویر کاربر")
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار")
    is_approved = models.BooleanField(default=False, verbose_name="تایید شده")

    def __str__(self):
        return f"{self.coment_usernameandlastname} - {self.coment_title[:20]}"

    






class Visit(models.Model):
    device = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class PageVideo(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='video/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    






class Portfolio(models.Model):
    text_portfolio = models.CharField(max_length=100)
    ttile_portfolio = models.TextField()
    img_portfolio = models.ImageField(upload_to='images/')
    file_portfoli = models.FileField()
    def __str__(self):
        return self.ttile_portfolio