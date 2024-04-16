import psycopg2
from GetData import GetData


class Database:
    """
    Подключется к базе данных и работает с ней
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
            password='Kkn_250600'
        )
        return conn

    def data_input_company(self, list_data):
        """
        Вводит данные о компании в соответствующую таблицу
        :return: None
        """
        conn = self.connection_database()
        cur = conn.cursor()
        for i in list_data:
            cur.execute(
                'INSERT INTO company(company_id, name_company, vacancies) '
                'VALUES (%s, %s, %s)',
                (i['company_id'], i['name_company'], i['vacancies'])
            )
            conn.commit()
        conn.close()

    def data_input_vacancies(self, list_vacancies):
        """
        Вводит данные о вакансиях в соответствующую таблицу
        :param list_vacancies: (list) список вакансий
        :return: None
        """
        conn = self.connection_database()
        cur = conn.cursor()

        for i in list_vacancies:
            cur.execute(
                'INSERT INTO vacancies ('
                'vacancy_id, '
                'company_id, '
                'vacancy_name, '
                'salary_from, '
                'salary_to, '
                'url_vacancy, '
                'responsibility) '
                'VALUES (%s, %s, %s, %s, %s, %s, %s)',
                (
                    i['vacancy_id'],
                    i['company_id'],
                    i['name'],
                    i['salary_from'],
                    i['salary_to'],
                    i['url'],
                    i['responsibility']
                )
            )
            conn.commit()
        conn.close()
