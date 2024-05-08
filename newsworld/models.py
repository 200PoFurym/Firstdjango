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

class MyUserModel(models.Model):
    username =models.CharField(max_length=60)
    email = models.EmailField()
    phone_number = models.IntegerField()
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'MyUser'
        verbose_name_plural = 'MyUsers'

class CartModel(models.Model):
    user_id = models.IntegerField()
    user_news = models.ForeignKey(News, on_delete=models.CASCADE)
    user_add_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user_id)
    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
class LikeModel(models.Model):
    user_id = models.IntegerField()
    user_news = models.ForeignKey(News, on_delete=models.CASCADE)
    user_add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id)
    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
