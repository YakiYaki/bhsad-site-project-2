# -*- coding: utf-8 -*-
from django.shortcuts import render


class Artist:
    def __init__(self, name_ru, name_en, email='', website='', tumblr='', instagram='', facebook='', vk='', behance=''):
        self.name_ru = name_ru
        self.name_en = name_en
        self.data = [behance, email, facebook, instagram, tumblr, vk, website]

    def get_data(self):
        return self.data


artists = [Artist('Арсентьев Артемий', 'Arsentyev Artemy', email='ars.tema@yandex.ru',
                  tumblr='artemiyarsentyev.tumblr.com'),
           Artist('Борисова Нелли', 'Borisova Nelly', tumblr='nellyliii.tumblr.com', instagram='bonelly.illustrating',
                  email='nelly_borisova@mail.ru'),
           Artist('Вакуленко Екатерина', 'Vakulenko Ekaterina'),
           Artist('Вебб Дарья', 'Webb Daria'),
           Artist('Дымова Анастасия', 'Dymova Anastasia'),
           Artist('Женуньк Анастасия', 'Zhenyuk Anastasia'),
           Artist('Закирова Лика', 'Zakirova Lika'),
           Artist('Зафт Лизавета', 'Zaft Lizaveta'),
           Artist('Ирлянова Анна', 'Irlyanova Anna'),
           Artist('Кирсанова Анна', 'Kirsanova Anna'),
           Artist('Козлова Елена', 'Kozlova Elena'),
           Artist('Чарли О’Конар', 'Charlie O\'Connar'),
           Artist('Копалова Ксения', 'Kopalova Ksenia'),
           Artist('Макеева Елизавета', 'Makeeva Elizabeth'),
           Artist('Мамедова Камилла', 'Mamedova Camilla'),
           Artist('Меркулова Дарья', 'Merkulova Darya'),
           Artist('Мордякова Эя', 'Mordyakova Eya'),
           Artist('Рафаилова Соня', 'Rafailova Sonia'),
           Artist('Савинова Наталья', 'Savinova Natalia'),
           Artist('Саламатова Ольга', 'Salamatova Olga'),
           Artist('Симачева Екатерина', 'Simacheva Ekaterina'),
           Artist('Чухрова Дарья', 'Chukhrova Daria'),
           Artist('Тогонидзе Франческо', 'Togonidze Francesco'),
           Artist('Шатохин Илья', 'Shatokhin Ilya'),
           Artist('Шевченко Александра', 'Shevchenko Alexandra'),
           Artist('Шилкините Полина', 'Shilkinite Polina'),
           Artist('Янин Вениамин', 'Yanin Veniamin'),
           Artist('Хункаева Амина', 'Khunkaeva Amina'),
           Artist('Ангелина Попельник', 'Angelina Popelnikh', email='Popelnykhangelina@gmail.com',
                  instagram='@sleepylina_art')]

content_en = [
    'FACETS is an exhibition by BHSAD illustration students, dedicated to documentary forms of illustration.',
    'An artist perceives reality through the prism of their own experience and personality, therefore even documentary '
    'works portray reality in a slightly distorted way. This exhibition includes documentary forms of illustration:',
    ['portraits', 'observation drawings', 'autobiographic works', 'reportage'],
    'Each of them is a facet of reality, reflected and modified by the author\'s view.',
    'Our exhibition FACETS is a reflection on the facets of artistic perceptions, the boundaries between the personal '
    'and objective, the diversity of this genre of documentary illustration and the variety of shapes of reality '
    'in the viewer’s eyes.',
    'ARTPLAY, SURF COFFEE',
    'Nizhnyaya Syromyatnicheskaya 10,',
    'bldg 2A, floor 2',
    'OPENING: 19 MAY 19:00',
    '20 MAY - 29 MAY'
]

content_ru = [
    'FACETS/ГРАНИ - выставка студентов-иллюстраторов Британской Высшей Школы Дизайна, посвященная документальным '
    'формам иллюстрации.',
    'Художник воспринимает реальность через призму своего опыта и личных качеств, поэтому даже документальные работы '
    'изображают ее в преобразованном виде. Выставка посвящена документальным формам иллюстрации:',
    ['портрет', 'наблюдения и зарисовки', 'автобиографические работы', 'репортаж'],
    'Каждая из этих форм - это грань реальности, отраженная и преобразованная авторским взглядом художника.',
    'Наша выставка FACETS/ГРАНИ - размышление о гранях художественного восприятия, границах между личным и '
    'объективным, о многогранности жанра документальной иллюстрации и о том, как разнообразны формы, '
    'которые принимает реальность в глазах смотрящего.',
    'Artplay, SURF coffee',
    'Нижняя Сыромятническая 10,',
    'стр. 2А, этаж 2',
    'Открытие: 19 мая 19:00',
    '20 мая - 29 мая'
]

# Create your views here.

context = {'lang': 'ru',
           'artists_half1': artists[:(len(artists) // 2)],
           'artists_half2': artists[(len(artists) // 2):],
           'content': content_ru}


def index(request):
    context['lang'] = 'ru'
    context['content'] = content_ru
    return render(request, "index.html", context)


def ru(request):
    context['lang'] = 'ru'
    context['content'] = content_ru
    return render(request, "index.html", context)


def en(request):
    context['lang'] = 'en'
    context['content'] = content_en
    return render(request, "index.html", context)
