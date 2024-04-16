import psycopg2


class DBManager():
    """
    Подключается к БД и работает с ней
    """

    def connection_database(self):
        """
        Подключение к БД
        :return: None
        """
        conn = psycopg2.connect(
            host='localhost',
            port='1024',
            database='HHru',
            user='postgres',
            password='12345'
        )
        return conn

    def get_companies_and_vacancies_count(self):
        """Получает список всех работодателей и сумму
        вакансий этой компании
        :return: (str)
        """
        conn = self.connection_database()
        cur = conn.cursor()
        cur.execute('SELECT name_company, vacancies FROM company')
        result = cur.fetchall()
        for i in result:
            print (f'{i[0]} - {i[1]} вакансий')

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию
        :return: (str)
        """
        conn = self.connection_database()
        cur = conn.cursor()
        cur.execute('SELECT vacancy_name, company_name, salary_from, salary_to, url_vacancy vacancies FROM vacancies')
        result = cur.fetchall()
        for i in result:
            print(f'{i[0]} ({i[1]}) зароботная плата от {i[2]} до {i[3]}, ссылка {i[4]}')

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям
        :return: (str)
        """
        conn = self.connection_database()
        cur = conn.cursor()
        cur.execute('SELECT AVG(salary_from) FROM vacancies')
        result = cur.fetchall()
        for i in result:
            print(f'Средняя заработная плата по предложенным вакансиям -> {i}')


    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий,
        у которых зарплата выше средней по всем вакансиям.
        :return: (str)
        """
        conn = self.connection_database()
        cur = conn.cursor()
        cur.execute('SELECT vacancy_name, url_vacancy FROM vacancies'
                    'WHERE salary_from>AVG(salary_from)')
        result = cur.fetchall()
        for i in result:
            print(f'{i[0]}, ссылка {i[1]}')


    def get_vacancies_with_keyword(self, word):
        """
        Получает список всех вакансий,
        в названии которых содержатся переданные в метод слова
        :return:
        """
    conn = self.connection_database()
    cur = conn.cursor()
    cur.execute('SELECT vacancy_name, url_vacancy FROM vacancies'
                'WHERE vacancy_name LIKE %{words}%')
    result = cur.fetchall()
    for i in result:
        print(f'{i[0]}, ссылка {i[1]}')




