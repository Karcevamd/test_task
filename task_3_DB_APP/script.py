import psycopg2
from random import randint, uniform, choice
from faker import Faker

fake = Faker()

conn = psycopg2.connect(dbname="mydatabase", user="postgres", password="0000")
cur = conn.cursor()
ship_names = ["Адмирал", "Бриз", "Витязь", "Геракл", "Дельфин", "Европа", "Жемчужина", "Зефир", "Император", "Корсар"]
port_names = ["Гавань", "Морской бриз", "Портовая улица", "Маяк", "Бухта", "Волны", "Морское око", "Причал", "Морской горизонт", "Морской путь"]
cargo_names = [
    "Электроника",
    "Мебель",
    "Одежда и обувь",
    "Автозапчасти",
    "Продукты питания",
    "Химическая продукция",
    "Строительные материалы",
    "Медицинское оборудование",
    "Текстиль и текстильные изделия",
    "Алкогольные напитки",
    "Техническое оборудование",
    "Бытовая техника",
    "Книги и печатная продукция",
    "Удобрения и сельскохозяйственные материалы",
    "Драгоценные металлы и камни",
    "Подарочные товары",
    "Детские игрушки",
    "Топливо и нефтепродукты",
    "Животные и растения",
    "Ювелирные изделия",
    "Электроинструменты и оборудование",
    "Спортивные товары и инвентарь",
    "Автомобили и мотоциклы",
    "Офисная техника и принадлежности",
    "Медицинская одежда и оборудование",
    "Металлическая продукция",
    "Компьютеры и комплектующие",
    "Мобильные устройства и аксессуары",
    "Косметика и парфюмерия",
    "Электронные компоненты и аксессуары",
    "Инструменты и оборудование для ремонта",
    "Хозяйственные товары и бытовая химия",
    "Материалы для упаковки и транспортировки",
    "Товары для рыбалки и охоты",
    "Музыкальные инструменты и оборудование",
    "Поделки и рукоделие",
    "Подарочные наборы и корзины",
    "Продукция деревообрабатывающей промышленности",
    "Электронные книги и журналы",
    "Подписки на сервисы и услуги",
    "Электрооборудование и электроинструменты",
    "Садовый инвентарь и техника",
    "Семена и саженцы",
    "Игры и развлечения",
    "Подушки и одеяла",
    "Товары для дома и интерьера",
    "Туристическое снаряжение и средства передвижения",
    "Электронные системы безопасности",
    "Огнетушители и средства тушения пожаров",
    "Оружие и боеприпасы",
    "Эксклюзивная продукция и предметы искусства",
    "Подарочные сертификаты и карты",
    "Технологическое оборудование и системы",
    "Медицинская техника и инструменты",
    "Специализированная техника и оборудование",
    "Средства для ухода за домашними животными",
    "Канцелярские товары и школьные принадлежности",
    "Продукция для здоровья и красоты",
    "Товары для активного отдыха и спорта",
    "Комплектующие для бытовой техники",
    "Элементы декора и интерьера",
    "Инвентарь для виноделия и пивоварения",
    "Продукция для автосервиса и техобслуживания",
    "Товары для выращивания растений и цветов",
    "Растения для сада и огорода",
    "Услуги и сервисы по транспортировке и доставке",
    "Продукция для строительства и ремонта",
    "Подарочные упаковки и украшения",
    "Товары для офиса и бизнеса",
    "Товары для дачи и загородного отдыха",
    "Экологически чистая продукция и товары",
    "Подарочные сувениры и сувенирная продукция",
    "Подарки и сувениры с символикой городов и стран",
    "Товары для активного образа жизни и здоровья",
    "Электронные товары и цифровая продукция",
    "Оптическое оборудование и оптика",
    "Печатная продукция и издательские материалы",
    "Информационные продукты и сервисы",
    "Рекламная продукция и сувениры",
    "Товары для ухода за телом и волосами",
    "Украшения и аксессуары",
    "Экологически чистые товары и продукты",
    "Товары для здоровья и красоты",
    "Товары для ванной и душа",
    "Товары для питания и здорового образа жизни",
    "Товары для спорта и активного отдыха"]

for index, name in enumerate(ship_names):
    cur.execute("INSERT INTO СУДНО (ИДЕНТИФИКАТОР, НАЗВАНИЕ, ПОРТ_ПРИПИСКИ, ЛЬГОТА) VALUES (%s, %s, %s, %s)", 
                ('{:03d}'.format(index+1), name, choice(port_names), randint(0, 10)))

for _ in range(5):
    cur.execute("INSERT INTO МЕСТА_ПОГРУЗКИ (ИДЕНТИФИКАТОР, ПРИЧАЛ, ПОРТ, ОТЧИСЛЕНИЯ_НА_ПОГРУЗКУ, ДАТА) VALUES (%s, %s, %s, %s, %s)", 
                ('{:03d}'.format(randint(0, 999)), '№'+str(randint(0, 10)), choice(port_names), randint(0, 10), fake.date()))

for index, name in enumerate(cargo_names):
    cur.execute("INSERT INTO ГРУЗ (ИДЕНТИФИКАТОР, НАЗВАНИЕ, ПОРТ_СКЛАДИРОВАНИЯ, СТОИМОСТЬ, МАКС_КОЛ_ВО) VALUES (%s, %s, %s, %s, %s)", 
                ('{:03d}'.format(index+1), name, choice(port_names), uniform(0, 199999.99), randint(0, 10)))
days = ('ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС')
cur.execute("SELECT ИДЕНТИФИКАТОР FROM МЕСТА_ПОГРУЗКИ")
id = cur.fetchall()
for _ in range(5):
    cur.execute("INSERT INTO ПОГРУЗКА (НОМЕР_ВЕДОМОСТИ, ДАТА, СУДНО, МЕСТО_ПОГРУЗКИ, ГРУЗ, КОЛ_ВО, СТОИМОСТЬ ) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                (randint(10000, 99999), choice(days), '{:03d}'.format(randint(0, len(ship_names))), choice(id), '{:03d}'.format(randint(0, len(cargo_names))), randint(1, 99999),  uniform(1000, 199999.99)))

conn.commit()
cur.close()
conn.close()
