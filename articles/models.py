from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tag(models.Model):

    topic = models.CharField(max_length=256, verbose_name='Название')   
    article = models.ManyToManyField("Article", related_name='scopes', through='TagArticle', verbose_name='Статья')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['topic']

    def __str__(self):
        return self.topic

class TagArticle(models.Model):
    
    article_id = models.ForeignKey("Article", on_delete=models.CASCADE, blank=False, null=False, verbose_name='Статья')
    scopes = models.ForeignKey("Tag", on_delete=models.CASCADE, blank=False, null=False, verbose_name='Раздел', related_name='scopes')
    is_main = models.BooleanField(default=False, verbose_name='Основной')
