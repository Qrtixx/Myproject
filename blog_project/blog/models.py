from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Название', max_length=100, unique=True)
    slug = models.SlugField('Ссылка', max_length=110, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)
    slug = models.SlugField('Ссылка', max_length=60, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    content = models.TextField('Содержание')
    publish_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', verbose_name='автор')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles', verbose_name='категория')
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles', verbose_name='теги')
    image = models.ImageField('Изображение', upload_to='articles/%Y/%m/', blank=True, null=True)

    class Meta:
        ordering = ['-publish_date']
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='статья')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='автор')
    text = models.TextField('Комментарий')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return f'{self.author}: {self.text[:30]}'
