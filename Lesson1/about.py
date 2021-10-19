import time
from tqdm.auto import tqdm


def show_info_me():
    """ Показывает инфо о коллеге


    """

    about_me = {
        'ФИО': 'Левченко Алексей',
        'Должность': 'Ведущий исследователь данных',
        'Блок': 'Технологии',
        'Делаю': 'рекомендательные системы в HR',
    }
    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)

def show_info_ekaterina():
    """ Показывает инфо о коллеге """
    about_me = {
        'ФИО': 'Лось Екатерина',
        'Должность': 'Менеджер по ипотечному кредитованию',
        'Блок': 'Розничный блок',
        'Делаю': 'Помогаю людям стать счастливыми обладателями объекта недвижимости',
    }
    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)



def show_info_igor():
    """ Показывает инфо о коллеге """
    about_me = {
        'ФИО' : 'Карайман Игорь',
        'Должность' : 'Менеджер',
        'Блок' : 'Сервисы',
        'Делаю' : 'Интеграции в новой архивной системе Сбера'
    }

    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)

def show_info_artem():
    """ Показывает инфо о коллеге """
    about_me = {
        'ФИО': 'Забродин Артём',
        'Должность': 'Ведущий специалист',
        'Блок': 'Риски',
        'Делаю': 'корпоративную риск отчетность и анализирую портфель',
    }

    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)

def show_info_alexander():
    """ Показывает инфо о коллеге """

    about_me = {
        'ФИО': 'Захаров Александр Владимирович',
        'Должность': 'Старший менеджер по обслуживанию',
        'Блок': 'Розничный бизнес',
        'Делаю': 'делаю все',
    }

    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)

def show_info_maxim():
    """ Показывает инфо о коллеге """

    about_me={
    'ФИО':'Малинин Максим',
    'Должность':'Старший специалист',
    'Блок':'Корпоративный бизнес',
    'Делаю':'мониторинг залогов',
    }

    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)


def show_info_maria():
    """ Показывает инфо о коллеге """

    about_me = {
    'ФИО': 'Чалкина Мария Александровна',
    'Должность': 'Старший специалист',
    'Блок': 'Сервисы',
    'Делаю': 'Сопровождение КО',
    }

    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)


def show_into_maria_i():
    about_me = {
        'ФИО':'Истомина Мария',
        'Должность':'Ведущий аудитор',
        'Блок': 'Управление внутреннего аудита',
        'Делаю': 'Выявляю отклонения в процессах Банка'
    }
    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)


def show_into_tatiana():
    about_me = {
        'ФИО': 'Дудина Татьяна',
        'Должность': 'Ассистент КМ',
        'Блок': 'Розничный бизнес',
        'Делаю': 'делаю все',
    }
    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)

def show_into_svetlana():
    about_me = {
        'ФИО': 'Зейналова Светлана Владимировна',
        'Должность': 'Старший менеджер',
        'Блок': 'Розничный блок',
        'Делаю': ' продажи'
    }
    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)

def show_into_roman():
    about_me = {
        'ФИО' : 'Янов Роман',
        'Должность' : 'Старший Клиентский Менеджер',
        'Блок' : 'Розничный бизнес',
        'Делаю' : 'Людей счастливыми'
    }
    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)

def show_into_andrew():
    about_me = {
        'ФИО': 'Фёдоров Андрей',
        'Должность': 'Старший клиентский менеджер',
        'Блок': 'Розничный блок',
        'Делаю': 'все',
    }
    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)


def show_into_vladimir():
    about_me = {
        'ФИО': 'Литвинов Владимир',
        'Должность': 'Ведущий специалист',
        'Блок': 'Технологии',
        'Делаю': 'Помогаю клиентам стать счастливыми обладателями пластиковых карт',
    }

    for k, v in about_me.items():
        print(f'{k}:{v}')
    else:
        print('_' * 30)


info_list = [
    show_info_me,
    show_info_ekaterina,
    show_info_igor,
    show_info_artem,
    show_info_alexander,
    show_info_maxim,
    show_info_maria,
    show_into_maria_i,
    show_into_tatiana,
    show_into_svetlana,
    show_into_roman,
    show_into_andrew,
    show_into_vladimir,

]

if __name__ == "__main__":
    for show_info in info_list:
        show_info()
        for i in tqdm(range(30)):
            time.sleep(1)

        print('Спасибо за инфо!')
        print('_' * 30)
