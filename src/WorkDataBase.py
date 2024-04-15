import psycopg2
from GetData import GetData

class Database:
    """
    Подключется к базе данных и работает с ней
    """

    def connection(self):
        """
        Подключение к БД
        :return: None
        """
        conn = psycopg2.connect(
            host = 'localhost',
            port = '1024',
            database = 'HHru',
            user = 'postgres',
            password = 'Kkn_250600'
        )
        return conn

    def data_input_company(self, list_data):
        """
        Вводит данные о компании в соответствующую таблицу
        :return: None
        """
        conn = self.connection()
        cur = conn.cursor()
        for i in list_data:
            cur.execute(
                'INSERT INTO company(company_id, name_company, vacancies) '
                'VALUES (%(company_id),%(name_company),%(vacancies))',
                (i['company_id'], i['name_company'], i['vacancies'])
                )
        conn.close()

if __name__ == '__main__':
    emp = Database()
    value = GetData()
    list_data = value.vacancies_company()
    emp.data_input_company(list_data)