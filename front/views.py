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
           Artist('Вакуленко Екатерина', 'Vakulenko Ekaterina', email='ekaterina.vakulenko@yahoo.com',
                  tumblr='ovche.tumblr.com'),
           Artist('Вебб Дарья', 'Webb Daria', email='webb.dasha@gmail.com', instagram='kalervo'),
           Artist('Дымова Анастасия', 'Dymova Anastasia', email='nastiawee@gmail.com', facebook='nastasita'),
           Artist('Женуньк Анастасия', 'Zhenyuk Anastasia', tumblr='zhenunk.tumblr.com', instagram='zhenunk',
                  behance='zhenunk'),
           Artist('Закирова Лика', 'Zakirova Lika', email='lika.zakirova413@gmail.com',
                  tumblr='likazakirova.tumblr.com'),
           Artist('Зафт Лизавета', 'Zaft Lizaveta', email='lizabeth.zaft@gmail.com',
                  tumblr='liazabeth-zaft.tumblr.com'),
           Artist('Ирлянова Анна', 'Irlyanova Anna', email='irlyanova@gmailc.om', website='annamiyu.com',
                  instagram='annamiyu', behance='annamiyu'),
           Artist('Кирсанова Анна', 'Kirsanova Anna', email='lala.la2010@yandex.ru',
                  website='cargocollective.com/annakirsanova', instagram='kirsanova_st'),
           Artist('Козлова Елена', 'Kozlova Elena', email='lena.kozlova.gd@gmail.com', behance='lenakozlova'),
           Artist('Чарли О’Конар', 'Charlie O\'Connar', email='charlie.o.konar@gmail.com', tumblr='o-konar.tumblr.com'),
           Artist('Копалова Ксения', 'Kopalova Ksenia', email='ksenia.jpg@gmail.com', website='kseniakopalova.com',
                  behance='boothehamster'),
           Artist('Макеева Елизавета', 'Makeeva Elizabeth', email='ni.shoroha@gmail.com'),
           Artist('Мамедова Камилла', 'Mamedova Camilla', email='kamillam04@gmail.com', website='kameeellah.com',
                  instagram='kameeellah'),
           Artist('Меркулова Дарья', 'Merkulova Darya', email='daria.merkulova15@gmail.com',
                  tumblr='mrklvillustrations.tumblr.com'),
           Artist('Мордякова Эя', 'Mordyakova Eya', email='eya.mordyakova@gmail.com', vk='mordyakovaeya',
                  behance='moonzayats'),
           Artist('Рафаилова Соня', 'Rafailova Sonia', email='tata.shmyk@gmail.com',
                  website='cargocollective.com/shmyk', instagram='shmyk_art'),
           Artist('Савинова Наталья', 'Savinova Natalia', email='natavolpesavinova@mail.ru',
                  instagram='natalia_savinova'),
           Artist('Саламатова Ольга', 'Salamatova Olga', email='stoggyo@gmail.com', instagram='stoggyo',
                  behance='stogova-ol68a'),
           Artist('Симачева Екатерина', 'Simacheva Ekaterina', email='simacheva.katya@gmail.com',
                  tumblr='vuorisima.tumblr.com'),
           Artist('Чухрова Дарья', 'Chukhrova Daria', email='chukhrovad@mail.ru',
                  website='cargocollective.com/D_A_III_A', instagram='chukhrova'),
           Artist('Тогонидзе Франческо', 'Togonidze Francesco', email='francescogeo@gmail.com', vk='dailyfrank'),
           Artist('Шатохин Илья', 'Shatokhin Ilya', email='ilia@shatokhin.me', website='shatokhin.me'),
           Artist('Шевченко Александра', 'Shevchenko Alexandra', email='alexandra.shevchenko95@gmail.com',
                  vk='coolshura', behance='alexandrasecea'),
           Artist('Шилкините Полина', 'Shilkinite Polina', email='paulshilkinis@gmail.com', vk='shlkns',
                  behance='paulshilkinis'),
           Artist('Янин Вениамин', 'Yanin Veniamin', email='yanin.veniamin@gmail.com', instagram='venyaminish',
                  vk='club112844040'),
           Artist('Хункаева Амина', 'Khunkaeva Amina', email='amina.khunkaeva@mail.ru', instagram='ami.naeva'),
           Artist('Ангелина Попелных', 'Angelina Popelnykh', email='popelnykhangelina@gmail.com',
                  instagram='sleepylina_art')]

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
