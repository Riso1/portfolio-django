from django.db import models
from django.utils.text import slugify


class SiteSettings(models.Model):
    full_name = models.CharField(
        max_length=150,
        verbose_name='ФИО'
    )

    position = models.CharField(
        max_length=150,
        verbose_name='Должность'
    )

    site_title = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Название сайта во вкладке'
    )

    meta_description = models.TextField(
        blank=True,
        verbose_name='SEO-описание'
    )

    favicon = models.ImageField(
        upload_to='favicon/',
        blank=True,
        null=True,
        verbose_name='Favicon'
    )

    og_image = models.ImageField(
        upload_to='og/',
        blank=True,
        null=True,
        verbose_name='Картинка для превью ссылки'
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


class PageSection(models.Model):
    key = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='Ключ секции'
    )

    title = models.CharField(
        max_length=150,
        verbose_name='Заголовок'
    )

    subtitle = models.TextField(
        blank=True,
        verbose_name='Подзаголовок / описание'
    )

    is_published = models.BooleanField(
        default=True,
        verbose_name='Показывать'
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок'
    )

    show_in_menu = models.BooleanField(
        default=True,
        verbose_name='Показывать в меню'
    )

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Секция страницы'
        verbose_name_plural = 'Секции страницы'

    def __str__(self):
        return self.title


class TextBlock(models.Model):
    key = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='Ключ блока'
    )
    title = models.CharField(
        max_length=150,
        verbose_name='Заголовок'
    )
    content = models.TextField(
        verbose_name='Текст'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Показывать'
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок'
    )

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Текстовый блок'
        verbose_name_plural = 'Текстовые блоки'

    def __str__(self):
        return self.title


class TimelineItem(models.Model):
    CATEGORY_CHOICES = [
        ('experience', 'Опыт'),
        ('education', 'Образование'),
    ]

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        verbose_name='Категория'
    )
    period = models.CharField(
        max_length=100,
        verbose_name='Период'
    )
    title = models.CharField(
        max_length=150,
        verbose_name='Название'
    )
    subtitle = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Подзаголовок'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Показывать'
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок'
    )

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Опыт / образование'
        verbose_name_plural = 'Опыт и образование'

    def __str__(self):
        return f'{self.get_category_display()} — {self.title}'


class Technology(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название технологии'
    )
    icon_class = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='CSS-класс иконки'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Показывать'
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок'
    )

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Технология'
        verbose_name_plural = 'Технологии'

    def __str__(self):
        return self.title


class HeroStat(models.Model):
    value = models.CharField(
        max_length=50,
        verbose_name='Значение'
    )
    label = models.CharField(
        max_length=150,
        verbose_name='Подпись'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Показывать'
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок'
    )

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Показатель на главном экране'
        verbose_name_plural = 'Показатели на главном экране'

    def __str__(self):
        return f'{self.value} — {self.label}'


class ContactLink(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    url = models.CharField(
        max_length=255,
        verbose_name='Ссылка или контакт'
    )
    icon_class = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='CSS-класс иконки'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Показывать'
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок'
    )

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Контакт / ссылка'
        verbose_name_plural = 'Контакты и ссылки'

    def __str__(self):
        return self.title


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

    project_status = models.CharField(
        max_length=50,
        default='Завершён',
        verbose_name='Статус проекта'
    )

    slug = models.SlugField(
        max_length=150,
        unique=True,
        blank=True,
        null=True,
        verbose_name='URL-адрес проекта'
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


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


class TemplateUseCase(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=120, unique=True, verbose_name='URL-адрес')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    class Meta:
        verbose_name = 'категория применения'
        verbose_name_plural = 'Для чего подходит'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class TemplateDemo(models.Model):
    difficulty = models.CharField(
        max_length=30,
        default='Средняя',
        verbose_name='Сложность'
    )

    features = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Что использует'
    )

    use_cases = models.ManyToManyField(
        TemplateUseCase,
        blank=True,
        related_name='templates',
        verbose_name='Для чего подходит'
    )

    CATEGORY_CHOICES = [
        ('ui', 'UI-компоненты'),
        ('animation', 'Анимации'),
        ('carousel', 'Карусели'),
        ('form', 'Формы'),
        ('auth', 'Авторизация'),
        ('other', 'Другое'),
    ]

    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL-адрес')
    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default='ui',
        verbose_name='Категория'
    )

    short_description = models.TextField(verbose_name='Краткое описание')
    cover = models.ImageField(
        upload_to='template_demos/',
        blank=True,
        null=True,
        verbose_name='Обложка'
    )

    html_code = models.TextField(blank=True, verbose_name='HTML')
    css_code = models.TextField(blank=True, verbose_name='CSS')
    js_code = models.TextField(blank=True, verbose_name='JavaScript')

    github_url = models.URLField(blank=True, verbose_name='GitHub')
    demo_url = models.URLField(blank=True, verbose_name='Демо-ссылка')

    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    class Meta:
        verbose_name = 'шаблон'
        verbose_name_plural = 'Шаблоны'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
