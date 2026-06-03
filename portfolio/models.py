from django.db import models


class SiteSettings(models.Model):
    full_name = models.CharField(
        max_length=150,
        verbose_name='ФИО'
    )
    position = models.CharField(
        max_length=150,
        verbose_name='Должность'
    )
    about = models.TextField(
        verbose_name='О себе'
    )
    photo = models.ImageField(
        upload_to='profile/',
        blank=True,
        null=True,
        verbose_name='Фото'
    )
    resume = models.FileField(
        upload_to='resume/',
        blank=True,
        null=True,
        verbose_name='Резюме'
    )
    github_url = models.URLField(
        blank=True,
        verbose_name='GitHub'
    )
    telegram_url = models.URLField(
        blank=True,
        verbose_name='Telegram'
    )
    email = models.EmailField(
        blank=True,
        verbose_name='Email'
    )

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'

    def __str__(self):
        return 'Настройки сайта'


class Project(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Название проекта'
    )
    short_description = models.TextField(
        verbose_name='Краткое описание'
    )
    stack = models.CharField(
        max_length=255,
        verbose_name='Стек технологий'
    )
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True,
        verbose_name='Обложка проекта'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок отображения'
    )
    full_description = models.TextField(
        blank=True,
        verbose_name='Полное описание'
    )
    github_url = models.URLField(
        blank=True,
        verbose_name='Ссылка на GitHub'
    )
    demo_url = models.URLField(
        blank=True,
        verbose_name='Ссылка на демо'
    )
    featured = models.BooleanField(
        default=False,
        verbose_name='Показывать на главной'
    )


    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Название сертификата'
    )
    organization = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Организация'
    )
    issue_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата выдачи'
    )
    file = models.FileField(
        upload_to='certificates/',
        verbose_name='Файл сертификата'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок отображения'
    )

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'

    def __str__(self):
        return self.title
