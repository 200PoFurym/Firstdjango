from django.db import models

# Create your models here.
class NewsCategory(models.Model):
    category_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Все новости'

class News(models.Model):
    news_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.FileField(upload_to='News_image')

    def __str__(self):
        return self.news_name

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Все новости'
