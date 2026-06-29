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

    pwa_icon = models.ImageField(
        upload_to='pwa/',
        blank=True,
        null=True,
        verbose_name='PWA-иконка'
    )

    admin_pwa_icon = models.ImageField(
        upload_to='pwa/admin/',
        blank=True,
        null=True,
        verbose_name='PWA-иконка админки'
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


class ProjectOrder(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('done', 'Завершена'),
        ('rejected', 'Отклонена'),
    ]

    PROJECT_TYPE_CHOICES = [
        ('website', 'Сайт'),
        ('bot', 'Telegram-бот'),
        ('webapp', 'Веб-приложение'),
        ('improvement', 'Доработка'),
        ('other', 'Другое'),
    ]

    name = models.CharField(max_length=120, verbose_name='Имя')
    contact = models.CharField(max_length=200, verbose_name='Контакт')
    project_type = models.CharField(
        max_length=30,
        choices=PROJECT_TYPE_CHOICES,
        verbose_name='Тип проекта'
    )
    budget = models.PositiveIntegerField(default=0, verbose_name='Предварительная стоимость')
    description = models.TextField(blank=True, verbose_name='Описание проекта')
    selected_options = models.TextField(blank=True, verbose_name='Выбранные опции')
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name='Статус'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создана')

    class Meta:
        verbose_name = 'заявка на проект'
        verbose_name_plural = 'Заявки на проекты'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.get_project_type_display()}'


class OrderProjectType(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название')
    slug = models.SlugField(max_length=80, unique=True, verbose_name='Код')
    subtitle = models.CharField(max_length=200, blank=True, verbose_name='Подпись')
    base_price = models.PositiveIntegerField(default=0, verbose_name='Базовая цена')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    class Meta:
        verbose_name = 'тип проекта'
        verbose_name_plural = 'Оформление заказа: типы проектов'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class OrderOptionGroup(models.Model):
    project_type = models.ForeignKey(
        OrderProjectType,
        on_delete=models.CASCADE,
        related_name='option_groups',
        verbose_name='Тип проекта'
    )
    title = models.CharField(max_length=120, verbose_name='Название группы')
    input_type = models.CharField(
        max_length=20,
        choices=[
            ('radio', 'Один вариант'),
            ('checkbox', 'Несколько вариантов'),
        ],
        default='checkbox',
        verbose_name='Тип выбора'
    )
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    class Meta:
        verbose_name = 'группа опций заказа'
        verbose_name_plural = 'Оформление заказа: группы опций'
        ordering = ['order', 'title']

    def __str__(self):
        return f'{self.project_type} — {self.title}'


class OrderOption(models.Model):
    group = models.ForeignKey(
        OrderOptionGroup,
        on_delete=models.CASCADE,
        related_name='options',
        verbose_name='Группа'
    )
    title = models.CharField(max_length=160, verbose_name='Название')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')
    is_default = models.BooleanField(default=False, verbose_name='Выбрано по умолчанию')
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    class Meta:
        verbose_name = 'опция заказа'
        verbose_name_plural = 'Оформление заказа: опции'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class OrderDeadline(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название')
    multiplier = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=1,
        verbose_name='Множитель цены'
    )
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    class Meta:
        verbose_name = 'срок выполнения'
        verbose_name_plural = 'Оформление заказа: сроки'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class OrderWorkTerm(models.Model):
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    class Meta:
        verbose_name = 'условие работы'
        verbose_name_plural = 'Оформление заказа: условия работы'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class OrderWebsiteGroup(OrderOptionGroup):
    class Meta:
        proxy = True
        verbose_name = 'Сайт'
        verbose_name_plural = 'Оформление заказа: Сайт'


class OrderBotGroup(OrderOptionGroup):
    class Meta:
        proxy = True
        verbose_name = 'Telegram-бот'
        verbose_name_plural = 'Оформление заказа: Telegram-бот'


class OrderWebAppGroup(OrderOptionGroup):
    class Meta:
        proxy = True
        verbose_name = 'Веб-сервис'
        verbose_name_plural = 'Оформление заказа: Веб-сервис'


class OrderImprovementGroup(OrderOptionGroup):
    class Meta:
        proxy = True
        verbose_name = 'Доработка'
        verbose_name_plural = 'Оформление заказа: Доработка'


class OrderPaymentSettings(models.Model):
    title = models.CharField(max_length=120, default='Оплата по СБП', verbose_name='Заголовок')
    bank_name = models.CharField(max_length=120, default='Альфа-Банк', verbose_name='Банк')
    recipient_name = models.CharField(max_length=160, blank=True, verbose_name='Получатель')
    phone_or_payment_info = models.CharField(max_length=200, blank=True, verbose_name='Телефон / реквизиты')
    qr_code = models.ImageField(upload_to='payment/', blank=True, null=True, verbose_name='QR-код')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'настройки оплаты'
        verbose_name_plural = 'Оформление заказа: оплата'

    def __str__(self):
        return self.title


class PaymentConfirmation(models.Model):
    name = models.CharField(max_length=120, verbose_name='Имя')
    contact = models.CharField(max_length=160, verbose_name='Контакт')
    amount = models.PositiveIntegerField(verbose_name='Сумма')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')

    class Meta:
        verbose_name = 'подтверждение оплаты'
        verbose_name_plural = 'Подтверждения оплат'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.amount} ₽'


class LegalDocument(models.Model):
    title = models.CharField(max_length=160, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')
    content = models.TextField(verbose_name='Содержание')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    class Meta:
        verbose_name = 'юридический документ'
        verbose_name_plural = 'Юридическая информация'
        ordering = ['title']

    def __str__(self):
        return self.title


class ClientDocument(models.Model):
    title = models.CharField(max_length=160, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    file = models.FileField(upload_to='client_documents/', verbose_name='Файл')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')

    class Meta:
        verbose_name = 'документ для клиента'
        verbose_name_plural = 'Документы для клиентов'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
