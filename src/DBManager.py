import psycopg2


class DBManager():
    """
    Подключается к БД и работает с ней
    """

    def __init__(self):
        self.conn = psycopg2.connect(
            host='localhost',
            port='1024',
            database='HHru',
            user='postgres',
            password='12345'
        )
        self.cur = self.conn.cursor()

    def data_input_company(self, list_data):
        """
        Вводит данные о компании в соответствующую таблицу
        :return: None
        """

        for i in list_data:
            self.cur.execute(
                'INSERT INTO company(company_id, name_company, vacancies) '
                'VALUES (%s, %s, %s)',
                (i['company_id'], i['name_company'], i['vacancies'])
            )
            self.conn.commit()

    def data_input_vacancies(self, list_vacancies):
        """
        Вводит данные о вакансиях в соответствующую таблицу
        :param list_vacancies: (list) список вакансий
        :return: None
        """
        for i in list_vacancies:
            self.cur.execute(
                'INSERT INTO vacancies ('
                'vacancy_id, '
                'company_id, '
                'company_name, '
                'vacancy_name, '
                'salary_from, '
                'salary_to, '
                'url_vacancy, '
                'responsibility) '
                'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                (
                    i['vacancy_id'],
                    i['company_id'],
                    i['company_name'],
                    i['name'],
                    i['salary_from'],
                    i['salary_to'],
                    i['url'],
                    i['responsibility']
                )
            )
            self.conn.commit()

    def get_companies_and_vacancies_count(self):
        """Получает список всех работодателей и сумму
        вакансий этой компании
        :return: (str)
        """
        self.cur.execute('SELECT name_company, vacancies FROM company')
        result = self.cur.fetchall()
        for i in result:
            print (f'{i[0]} - {i[1]} вакансий')

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию
        :return: (str)
        """
        self.cur.execute('SELECT vacancy_name, company_name, salary_from, salary_to, url_vacancy vacancies FROM vacancies')
        result = self.cur.fetchall()
        for i in result:
            print(f'{i[0]} ({i[1]}) зароботная плата от {i[2]} до {i[3]}, ссылка {i[4]}')

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям
        :return: (str)
        """
        self.cur.execute('SELECT AVG(salary_from) FROM vacancies')
        result = self.cur.fetchall()
        for i in result:
            print(f'Средняя заработная плата по предложенным вакансиям -> {i}')


    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий,
        у которых зарплата выше средней по всем вакансиям.
        :return: (str)
        """
        self.cur.execute('SELECT vacancy_name, url_vacancy FROM vacancies'
                    'WHERE salary_from>AVG(salary_from)')
        result = self.cur.fetchall()
        for i in result:
            print(f'{i[0]}, ссылка {i[1]}')


    def get_vacancies_with_keyword(self, word):
        """
        Получает список всех вакансий,
        в названии которых содержатся переданные в метод слова
        :return:
        """
        self.cur.execute('SELECT vacancy_name, url_vacancy FROM vacancies'
                    'WHERE vacancy_name LIKE %{words}%')
        result = self.cur.fetchall()
        for i in result:
            print(f'{i[0]}, ссылка {i[1]}')

    def close_db(self):
        self.conn.close()
