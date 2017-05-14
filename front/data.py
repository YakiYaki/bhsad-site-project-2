class Artist:
    def __init__(self, name_ru, name_en, email='', website='', tumblr='', instagram='', facebook='', vk='', behance=''):
        self.name_ru = name_ru
        self.name_en = name_en
        if website:
            self.website = website
        if email:
            self.email = email
        if tumblr:
            self.tumblr = tumblr
        if instagram:
            self.instagram = instagram
        if vk:
            self.vk = vk
        if facebook:
            self.facebook = facebook
        if behance:
            self.behance = behance


artists = [Artist('Арсентьев Артемий', 'Arsentyev Artemy', email='ars.tema@yandex.ru',
                  tumblr='artemiyarsentyev.tumblr.com'),
           Artist('Борисова Нелли', 'Borisova Nelly', tumblr='nellyliii.tumblr.com', instagram='bonelly.illustrating',
                  email='nelly_borisova@mail.ru'),
           Artist('Вакуленко Екатерина', 'Vakulenko Ekaterina'),
           Artist('Вебб Дария', 'Webb Daria'),
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
           Artist('Хункаева Амина', 'Khunkaeva Amina')]
