from django.core.management.base import BaseCommand

from portfolio.models import Technology, TemplateDemo, TemplateUseCase


class Command(BaseCommand):
    help = 'Adds PWA technologies and a PWA template demo.'

    def handle(self, *args, **options):
        technologies = [
            ('PWA', 'fa-solid fa-mobile-screen-button', 95),
            ('Service Worker', 'fa-solid fa-bolt', 96),
            ('Web App Manifest', 'fa-solid fa-file-code', 97),
        ]

        for title, icon_class, order in technologies:
            Technology.objects.update_or_create(
                title=title,
                defaults={
                    'icon_class': icon_class,
                    'is_published': True,
                    'order': order,
                },
            )

        use_case, _ = TemplateUseCase.objects.update_or_create(
            slug='web-apps',
            defaults={
                'title': 'Веб-приложения',
                'order': 20,
                'is_active': True,
            },
        )

        template_demo, _ = TemplateDemo.objects.update_or_create(
            slug='pwa-app',
            defaults={
                'title': 'PWA-приложение для сайта',
                'category': 'other',
                'difficulty': 'Средняя',
                'features': 'Django • JavaScript • Web App Manifest • Service Worker • iOS/Android',
                'short_description': (
                    'Устанавливаемый режим для сайта: иконка на экране телефона, '
                    'запуск без адресной строки, manifest.json, service worker, '
                    'offline-страница и настройка иконки через админку.'
                ),
                'html_code': PWA_HTML,
                'css_code': PWA_CSS,
                'js_code': PWA_JS,
                'is_published': True,
                'order': 30,
            },
        )
        template_demo.use_cases.set([use_case])

        self.stdout.write(self.style.SUCCESS('PWA technology stack and template demo were added.'))


PWA_HTML = """<section class="pwa-demo">
    <div class="pwa-demo__phone">
        <div class="pwa-demo__status"></div>
        <div class="pwa-demo__icon">
            <span>&lt;/&gt;</span>
        </div>
        <h3>Сайт как приложение</h3>
        <p>Добавьте сайт на главный экран и открывайте его без адресной строки.</p>
        <button class="pwa-demo__button" type="button">Показать установку</button>
    </div>

    <div class="pwa-demo__steps" aria-live="polite">
        <div class="pwa-demo__step is-active">1. Открыть сайт в браузере</div>
        <div class="pwa-demo__step">2. Нажать «Добавить на экран Домой»</div>
        <div class="pwa-demo__step">3. Запускать сайт как приложение</div>
    </div>
</section>"""

PWA_CSS = """.pwa-demo {
    display: grid;
    grid-template-columns: minmax(220px, 320px) 1fr;
    gap: 24px;
    align-items: center;
    padding: 28px;
    border-radius: 24px;
    background: #0f172a;
    color: #f8fafc;
}

.pwa-demo__phone {
    padding: 24px;
    border: 1px solid rgba(148, 163, 184, 0.24);
    border-radius: 28px;
    background: linear-gradient(180deg, #111827, #020617);
    text-align: center;
}

.pwa-demo__status {
    width: 82px;
    height: 6px;
    margin: 0 auto 26px;
    border-radius: 999px;
    background: #334155;
}

.pwa-demo__icon {
    display: grid;
    place-items: center;
    width: 96px;
    height: 96px;
    margin: 0 auto 18px;
    border-radius: 24px;
    background: linear-gradient(135deg, #1d4ed8, #0f172a);
    box-shadow: 0 18px 44px rgba(37, 99, 235, 0.32);
}

.pwa-demo__icon span {
    color: #fff;
    font-size: 30px;
    font-weight: 800;
}

.pwa-demo__button {
    border: 0;
    border-radius: 999px;
    padding: 12px 18px;
    background: #2563eb;
    color: #fff;
    font-weight: 700;
}

.pwa-demo__steps {
    display: grid;
    gap: 12px;
}

.pwa-demo__step {
    padding: 16px 18px;
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-radius: 16px;
    background: rgba(15, 23, 42, 0.72);
    color: #94a3b8;
}

.pwa-demo__step.is-active {
    border-color: #38bdf8;
    color: #f8fafc;
}

@media (max-width: 720px) {
    .pwa-demo {
        grid-template-columns: 1fr;
    }
}"""

PWA_JS = """document.querySelectorAll('.pwa-demo').forEach(function (demo) {
    const button = demo.querySelector('.pwa-demo__button');
    const steps = demo.querySelectorAll('.pwa-demo__step');
    let index = 0;

    button.addEventListener('click', function () {
        steps[index].classList.remove('is-active');
        index = (index + 1) % steps.length;
        steps[index].classList.add('is-active');
    });
});"""
