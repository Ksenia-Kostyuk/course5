from src.DBManager import DBManager


def main():
    print('Добро пожаловать. Предлагаю вам топ-10 работодателей сегодня')
    dbm = DBManager()
    print(dbm.get_companies_and_vacancies_count())

    input_user = ('Вот некоторые функции нашей программы:\n'
                  '1 - показать список вакансий\n'
                  '2 - показать среднюю зарплату по вакансиям\n'
                  '3 - показать список вакансий с зарплатой выше средней\n'
                  '4 - показать список вакансий, в которых есть ключевое слово\n'
                  '5 - выход из программы\n'
                  'Для продолжения укажите одно из перечисленных выше чисел: ')

    match input_user:
        case '1': dbm.get_all_vacancies()
        case '2': dbm.get_avg_salary()
        case '3': dbm.get_vacancies_with_higher_salary()
        case '4': dbm.get_vacancies_with_keyword()
        case '5': dbm.close_db(), print('Ждем вас снова, спасибо за внимание!')
        case _: print('Ошибка, введите число из указанных выше')


if __name__ == '__main__':
    main()