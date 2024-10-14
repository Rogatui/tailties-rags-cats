import sqlite3 as sq

def create():
    connection = sq.connect('database.db')
    cursor = connection.cursor()
    # cursor.execute('''Create table Profile(
    #     ID Integer Primary Key Autoincrement,
    #     Name Text Not Null,
    #     Type Text Not Null,
    #     Stat Text Not Null,
    #     Age Integer,
    #     Email Text Not Null Unique,
    #     Password Text Not Null,
    #     Passport_id Integer Not Null Unique,
    #     Photo_id Text
    # );''')
    # cursor.execute('''Create table Veterinary(
    #         ID Integer Primary Key Autoincrement,
    #         Title Text Not Null,
    #         Des Text Not Null,
    #         Price Text Not Null,
    #         Img Text Not Null
    #     );''')
    #
    # cursor.execute('''Create table Photograph(
    #         ID Integer Primary Key Autoincrement,
    #         Title Text Not Null,
    #         Des Text Not Null,
    #         Price Text Not Null,
    #         Img Text Not Null
    #     );''')
    #
    # cursor.execute('''Create table Restaurant(
    #         ID Integer Primary Key Autoincrement,
    #         Title Text Not Null,
    #         Des Text Not Null,
    #         Price Text Not Null,
    #         Img Text Not Null
    #     );''')
    #
    # cursor.execute('''Create table Ceremony(
    #         ID Integer Primary Key Autoincrement,
    #         Title Text Not Null,
    #         Des Text Not Null,
    #         Price Text Not Null,
    #         Img Text Not Null
    #     );''')
    #
    # cursor.execute('''Create table Honeymoon(
    #         ID Integer Primary Key Autoincrement,
    #         Title Text Not Null,
    #         Des Text Not Null,
    #         Price Text Not Null,
    #         Img Text Not Null
    #     );''')
    #
    # cursor.execute('''Create table Documents(
    #         ID Integer Primary Key Autoincrement,
    #         Name Text Not Null,
    #         Type Text Not Null,
    #         Stat Text Not Null,
    #         Age Real,
    #         Email Text Not Null Unique,
    #         Passport_id Integer Not Null Unique,
    #         Photo_id Text
    #     );''')
    #
    # cursor.execute('''Create table My_bag(
    #         ID Integer Primary Key Autoincrement,
    #         Title Text Not Null,
    #         Des Text Not Null,
    #         Price Text Not Null,
    #         Img Text Not Null
    #     );''')
    #
    # cursor.execute('''Create table Registration(
    #         ID Integer Primary Key Autoincrement,
    #         Passport_1 Integer Not Null Unique,
    #         Passport_2 Integer Not Null Unique
    #     );''')
    # cursor.execute('''Create table My_bagg(
    #         ID Integer Primary Key Autoincrement,
    #         Person Text Not Null,
    #         Title Text Not Null,
    #         Des Text Not Null,
    #         Price Text Not Null,
    #         Img Text Not Null
    #     );''')
    # cursor.execute('''Create table Profilee(
    #     ID Integer Primary Key Autoincrement,
    #     Name Text Not Null,
    #     Type Text Not Null,
    #     Stat Text Not Null,
    #     Age Real,
    #     Email Text Not Null Unique,
    #     Password Text Not Null,
    #     Passport_id Integer Not Null Unique,
    #     Photo_id Text
    # );''')
    # cursor.execute('''Create table Answer(
    #         ID Integer Primary Key Autoincrement,
    #         Email Text Not Null,
    #         Phone Text Not Null,
    #         Data Text Not Null
    #     );''')
    # connection.commit()
    # connection.close()
# create()

def get_db():
    connection = sq.connect('database.db', timeout=10)
    connection.row_factory = sq.Row
    return connection

# Взаємодія з профілями користувачів

def add_profile(Name, Type, Stat, Age, Email, Password, Passport_id, Photo_id):
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute('''
        Insert Into Profilee(Name, Type, Stat, Age, Email, Password, Passport_id, Photo_id)
            Values (?,?,?,?,?,?,?,?)
    ''', (Name, Type, Stat, Age, Email, Password, Passport_id, Photo_id))
    connection.commit()
    connection.close()

def read_profile(idd):
    connection = sq.connect('database.db')
    cursor = connection.cursor()
    result = cursor.execute('''Select * From Profilee Where Passport_id = ?''', (idd, )).fetchall()
    connection.close()
    return result


def read_profilee():
    connection = sq.connect('database.db')
    cursor = connection.cursor()
    result = cursor.execute('''Select * From Profilee''').fetchall()
    connection.close()
    return result

def delete_profile(idd):
    conection = get_db()
    conection.execute('''Delete From Profilee Where ID = ?''', (idd, ))
    conection.commit()

def read_profile_passport_id():
    connection = sq.connect('database.db')
    cursor = connection.cursor()
    result = cursor.execute('''Select Passport_id From Profilee''').fetchall()
    connection.close()
    return result

def read_profile_email(idd):
    connection = sq.connect('database.db')
    cursor = connection.cursor()
    result = cursor.execute('''Select * From Profilee Where Email = ?''', (idd, )).fetchone()
    connection.close()
    return result

# Взаємодія з послугами

def add_position(Title, name, des, price, img):
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute(f'''
                Insert Into {Title}(Title, Des, Price, Img)
                    Values (?,?,?,?)
            ''', (name, des, price, img))
    connection.commit()
    connection.close()

def read_position(Title):
    connection = sq.connect('database.db')
    cursor = connection.cursor()
    result = cursor.execute(f'''Select * From {Title}''').fetchall()
    connection.close()
    return result

def delete_position(Title,idd):
    conection = get_db()
    conection.execute(f'''Delete From {Title} Where ID = ?''', (idd, ))
    conection.commit()

# Взаємодія з регістрацією

def add_registration(pass1,pass2):
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute('''
            Insert Into Registration(Passport_1, Passport_2)
                Values (?,?)
        ''', (pass1, pass2))
    connection.commit()
    connection.close()

def read_registration():
    connection = sq.connect('database.db')
    cursor = connection.cursor()
    result = cursor.execute(f'''Select * From Registration''').fetchall()
    connection.close()
    return result

def read_registration_id(idd):
    connection = sq.connect('database.db')
    cursor = connection.cursor()
    result = cursor.execute(f'''Select * From Registration Where Passport_1 = ? or Passport_2 = ?''', (idd, idd)).fetchone()
    connection.close()
    return result

# print(read_registration())
def delete_registration(idd):
    conection = get_db()
    conection.execute('''Delete From Registration Where ID = ?''', (idd,))
    conection.commit()

# print(read_registration())
# Взаємодія з покупками

def add_my_bag(name, person, des, price, img):
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute('''
                    Insert Into My_bagg(Person, Title, Des, Price, Img)
                        Values (?,?,?,?,?)
                ''', (name, person, des, price, img))
    connection.commit()
    connection.close()

def add_answer(email, phone, data):
    connection  = get_db()
    cursor = connection.cursor()
    cursor.execute('''
                    Insert Into Answer(Email, Phone, Data)
                        Values (?,?,?)
                ''', (email, phone, data))
    connection.commit()
    connection.close()

def read_my_bag(email):
    conn = sq.connect('database.db')
    cur = conn.cursor()
    result = cur.execute('''SELECT * FROM My_bagg Where Person = ?''', (email, )).fetchall()
    conn.close()
    return result

def read_answer(email):
    conn = sq.connect('database.db')
    cur = conn.cursor()
    result = cur.execute('''SELECT * FROM Answer Where Person = ?''', (email, )).fetchall()
    conn.close()
    return result

def delete_my_bag(idd):
    conection = get_db()
    conection.execute('''Delete From My_bagg Where ID = ?''', (idd,))
    conection.commit()
#Пошук по бд
def search(words):
    connection = sq.connect('database.db')
    cursor = connection.cursor()
    try:
        result = cursor.execute('''
            Select * From Veterinary Where
            Lower(Title) Like Lower(?) Or
            Lower(Des) Like Lower(?)
        ''', ('%'+words+'%', '%'+words+'%')).fetchall()
        result2 = cursor.execute('''Select * From Photograph Where
            Lower(Title) Like Lower(?) Or
            Lower(Des) Like Lower(?)''', ('%'+words+'%', '%'+words+'%')).fetchall()
        result3 = cursor.execute('''Select * From Restaurant Where
                    Lower(Title) Like Lower(?) Or
                    Lower(Des) Like Lower(?)''', ('%' + words + '%', '%' + words + '%')).fetchall()
        result4 = cursor.execute('''Select * From Ceremony Where
                    Lower(Title) Like Lower(?) Or
                    Lower(Des) Like Lower(?)''', ('%' + words + '%', '%' + words + '%')).fetchall()
        result5 = cursor.execute('''Select * From Honeymoon Where
                    Lower(Title) Like Lower(?) Or
                    Lower(Des) Like Lower(?)''', ('%' + words + '%', '%' + words + '%')).fetchall()
        result.extend(result2)
        result.extend(result3)
        result.extend(result4)
        result.extend(result5)
        connection.close()
        return result
    except sq.Error as error:
        if error:
            print(f'Error {error}')

def search_ragistration(pass1, pass2):
    connection = sq.connect('database.db')
    cursor = connection.cursor()
    result = cursor.execute('''Select * From Registration Where Passport_1 = ?''', (pass1, )).fetchall()
    result2 = cursor.execute('''Select * From Registration Where Passport_2 = ?''', (pass2,)).fetchall()
    result.extend(result2)
    connection.close()
    return result

print(read_profilee())
# delete_profile(13)
# print(read_position('Honeymoon'))
# print(read_position('Restaurant'))
# add_position("Ceremony", 'Мур-казка', 'Церемонія у вигляді казкового весілля з аркою, прикрашеною квітами, і ексклюзивними весільними вбраннями для котів. Професійний ведучий розповість романтичну історію знайомства ваших улюбленців, а під час обміну клятвами лунатиме ніжна арфа.', '12999', 'https://flores-shop.com.ua/wp-content/uploads/2019/01/svadebnaya-arka-klassicheskaya.png')
# add_position("Ceremony", 'Лапка в лапку', 'Класична весільна церемонія з невеликими прикрасами та свічками. Включає музичний супровід на скрипці, щоб створити ніжну атмосферу. Ваші коти зможуть обмінятися обручками у вигляді мініатюрних нашийників.', '4999', 'https://www.mebelok.com/image/data/statja/kontent/6f9c06da9fc6441a78ee54f063a00611.jpg')
# add_position("Ceremony", 'Мяу-обіцянка', "Просте весілля на подвір'ї або в парку. Коротка церемонія під муркіт і легкий вітерець. Прикраси з польових квітів і саморобний арка з гілок. Ідеально для котів, які люблять природну простоту та не терплять зайвого галасу.", '1999', 'https://image.varianty.lviv.ua/40830f8ad29bb02983c17cca1077776b.jpg')
# add_position("Ceremony", 'Королівська мрія', 'Розкішна церемонія в старовинному замку або на березі моря. Оформлення простору живими квітами, котячі нашийники з діамантами, виступ професійного хору мурчиків. Кульмінацією буде запуск золотих кульок і грандіозне шоу з вогняними котячими фігурами.', '29999', 'https://pershyj.com/uploaded/images/thumbs/960x540/xo/mu/5tJj4wDl3ZrhNW3IySPPOn2EpOZyYWfi61dD4tLd.jpeg?v=3')
# add_position("Ceremony", 'Зіркова мить', 'Весільна церемонія під відкритим небом увечері, прикрашена свічками та ліхтариками. Феєрверк з пухнастих блискіток після обміну клятвами. Спеціальна фотозона для ваших котів на тлі зоряного неба, щоб закарбувати найкрасивіші моменти.', '7999', 'https://images.pexels.com/photos/6279053/pexels-photo-6279053.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')
# add_position('Veterinary', 'Бюджетна лапка', "Основний огляд без зайвих процедур. Ветеринар перевірить основні життєві показники, дасть поради щодо здорового харчування та гігієни. Обстеження проводиться швидко, але з любов'ю.", '400', 'https://furnitex.ua/upload/iblock/332/3p2hoo4lg0dgwacafpadeey2punthq8o.jpeg')
# add_position('Veterinary', 'Кіт-лікарня', "Спеціалізоване медичне обслуговування для котів з хронічними захворюваннями. Включає щотижневі обстеження, постійний моніторинг здоров'я, персонального ветеринара та преміум-ліки для підтримки якості життя.", '39999', 'https://furnitex.ua/upload/iblock/332/3p2hoo4lg0dgwacafpadeey2punthq8o.jpeg')
# add_position('Veterinary', 'Муркіт-мед', 'Повна діагностика, включно з УЗД та індивідуальними консультаціями. Ваш кіт отримає персоналізований план лікування, спеціальні вітаміни, а також VIP-обслуговування без черг.', '9999', 'https://furnitex.ua/upload/iblock/332/3p2hoo4lg0dgwacafpadeey2punthq8o.jpeg')
# add_position('Veterinary', 'Муркіт-діагноз', "Комплексний огляд з базовим аналізом крові, перевіркою зубів і шерсті. Лікар надасть детальні рекомендації для підтримання здоров'я, а також просту дієту для кота.", '2999', 'https://furnitex.ua/upload/iblock/332/3p2hoo4lg0dgwacafpadeey2punthq8o.jpeg')
# add_position('Veterinary', 'Пухнаста допомога', 'Повний медичний огляд із додатковими аналізами, щепленнями та обробкою від паразитів. У пакет входить консультація щодо психологічного комфорту кота під час візиту.', '5999', 'https://furnitex.ua/upload/iblock/332/3p2hoo4lg0dgwacafpadeey2punthq8o.jpeg')
# add_position('Photograph', 'Кіт за кадром', 'Ваш весільний фотограф буде робити фото випадкових моментів, навіть коли ви не дивитеся! Жодної постановки — тільки натуральні котячі емоції. Камера старенька, але настрій відмінний.', '3999', 'https://cdn.pixabay.com/photo/2016/10/10/14/45/icon-1728545_1280.jpg')
# add_position('Photograph', 'Мур-моделі', 'Фотосесія з професійними котячими моделями на фоні розкішних декорацій! Ваші коти отримають власний фотосет у шовкових стрічках та діамантових нашийниках. Плюс — альбом ручної роботи з золотим тисненням.', '89999', 'https://cdn.pixabay.com/photo/2016/10/10/14/45/icon-1728545_1280.jpg')
# add_position('Photograph', 'Лапки на згадку', 'Фотограф захопить усі найважливіші моменти, включно з тим, як ваші коти плутаються у стрічках та атакують кішки. Фото не будуть найвищої якості, але кожен кадр буде по-своєму кумедним.', '10999', 'https://cdn.pixabay.com/photo/2016/10/10/14/45/icon-1728545_1280.jpg')
# add_position('Photograph', 'Кото-гламур', 'Професійна команда зі стилю, світла і фотографії працює над тим, щоб зробити котячий день незабутнім! Студійна зйомка з найкращими фільтрами та ретушуванням, щоб ваші коти виглядали на всі сто.', '53999', 'https://cdn.pixabay.com/photo/2016/10/10/14/45/icon-1728545_1280.jpg')
# add_position('Photograph', 'Хвостата мить', 'Власний весільний фоторепортаж для ваших котів, де знімається все: від першого зустрічного "мяу" до вечірніх лапок у танці. Альбом з фото на флешці й зручна рамка для найбільшого портрета!', '23999', 'https://cdn.pixabay.com/photo/2016/10/10/14/45/icon-1728545_1280.jpg')
# add_position("Honeymoon", 'Париж на Лапках', 'Романтична прогулянка по Ейфелевій вежі з видом на Сене. Для котів, що цінують французький шарм і теплі місця для дрімоти в кафе.', '55000', 'https://gde-ostanovitsya.com/wp-content/uploads/2023/07/tour_eiffel.jpg')
# add_position("Honeymoon", 'Пухнастий тур по Карпатах', "Експедиція по зелених горах і ночівля в затишних дерев'яних будиночках. Ідеально для активних котів, що люблять свіже повітря та відпочинок біля каміна.", '12000', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Morskie_oko_o_swicie.jpg/280px-Morskie_oko_o_swicie.jpg')
# add_position("Honeymoon", 'Королівська подорож до Версалю', 'Приватний тур палацом Версаля для справжніх королівських котів. Чотири дні розкоші з індивідуальним персоналом і ексклюзивними ласощами.', '130000', 'https://turpoisk.ua/images/blog/versal/versalj-s-verhu.jpg')
# add_position("Honeymoon", 'Італійська сієста', 'Спокійний відпочинок на узбережжі Амальфі, із рибними делікатесами і сном під південним сонцем. Дводенний медовий місяць для ледачих котів, що люблять комфорт.', '46000','https://www.pizzatravel.com.ua/uploads/2020/38047.jpg')
# add_position("Honeymoon", 'Скарби Єгипту', 'Містичний тур по пірамідах Гізи з можливістю побувати в котячих храмах фараонів. Ідеально для котів, що обожнюють стародавню історію.', '23000', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYhZllNPDBjvfuP4W34DQp-7_PkZy2odNp9T7izoPeXpghv0ha1oCZTQEnw9ITUFx4-J8&usqp=CAU')
# add_position('', '', '', '', '')
# add_position('Restaurant', 'Котяча вечірка в парку', 'Невеликий банкет на свіжому повітрі з простими закусками: канапе, фрукти, легкі напої та десерти. Ідеально підходить для невеликих святкувань на відкритому повітрі.', '14000', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Dublin_Stephen%27s_Green-44_edit.jpg/280px-Dublin_Stephen%27s_Green-44_edit.jpg')
# add_position('Restaurant', 'Королівське весілля для котів', 'Грандіозне весілля з кількома курсами страв: фуа-гра, лобстери, елітні вина та ікри. Розкішні квіткові декорації, живий оркестр та персонал у стилі аристократичного котячого двору.', '170000', 'https://premiumbanquet.ru/uploads/s/a/h/b/ahbmqoghi4ui/img/autocrop/590466dc6a6b3a12a1fc9aa18b3d40ac.jpg')
# add_position('Restaurant', 'Вечірка з котячими коктейлями', 'Урочистий банкет, що включає коктейльний бар з фірмовими напоями, закуски на основі морепродуктів та котячі тематичні десерти.', '45000', 'https://www.ramadalviv.com.ua/wp-content/uploads/2019/10/photo_2019-10-22_14-51-02.jpg')
# add_position('Restaurant', 'Котяче весілля в кафе', 'Тематичний весільний банкет у невеликому кафе, де подають різноманітні закуски, міні-бургери, салати та напої. Прикрашене котячими елементами, меню включає торти у формі лапок.', '22000', 'https://reservehall.com/images/restourants/initially/berezovka_bp_zal12-6_1566218752.jpg')
# add_position('Restaurant', 'Весільна вечеря в котячому стилі', 'Класичне весільне меню з котячими мотивами, що включає кілька страв з вибору (риба, курка, вегетаріанське меню), легкі салати та тематичні торти. Ідеально для тих, хто хоче інтегрувати легку котячу естетику у святковий захід.', '37000', 'https://faber-restaurant.com/uploads/slider/zaxodi-dlia-biznesu_59a.jpg')
# add_position('Restaurant', 'Гала-вечірка у котячому особняку', 'Вечірній банкет у розкішному залі з вишуканими стравами: устриці, стейки, рідкісні види сирів, фруктові тарілки та ексклюзивні вина. Все супроводжується живою музикою і розкішним декором.', '76000', 'https://kasla-wed.ru/upload/uf/048/syra4tp7g54yxfn5ke4jk1j882tchudj.jpg')
# add_position('Restaurant', 'Котячий бал-маскарад', 'Вечірній бал у розкішному залі з вишуканим меню: кілька видів основних страв, елітні десерти, шампанське та авторські коктейлі. Гості приходять у масках з котячими мотивами.', '122000', 'https://premiumbanquet.ru/uploads/s/a/h/b/ahbmqoghi4ui/img/autocrop/59d5e47ca43da2ea2a91b3706a0bd841.jpg')