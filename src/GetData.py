import requests
from abc import ABC, abstractmethod

class AbstrGetData(ABC):
    """
    Определяет будущтий функционал класса,
    который получает данные о профессиях
    """

    @abstractmethod
    def connection_api(self):
        """Подключается к API"""
        pass


class GetData(AbstrGetData):
    """Подключается к серверу поиска вакансий"""

    def connection_api(self):
        """
        Осуществляет подключение к серверу
        :return:(int) статус подключения
        """
        response = requests.get("https://api.hh.ru/vacancies")
        return response.status_code

    def connection_api_comp(self):
        """
        Осуществляет подключение к серверу
        :return:(int) статус подключения
        """
        response = requests.get("http://api.hh.ru/employers/")
        return response.status_code

    def getting_employers(self):
        """
        Возвращает работодателей с удаленного сервера
        :return: (str) файл json
        """
        param = {"per_page": 10, "sort_by": "by_vacancies_open"}
        response = requests.get("http://api.hh.ru/employers/", param)
        return response.json().get("items")

    def list_employers(self):
        """
        Возвращает список компаний-работодателей и их id
        :return: (list) список компаний
        """
        data = self.getting_employers()
        employers = []
        for emp in data:
            employers.append(({
                'id': emp['id'],
                'name': emp['name'],
            }))
        return employers

    def vacancies_company(self):
        """
        Возвращает список компаний-работодателей, их id
        и количество открытых вакансий
        :return: (list) список компаний
        """
        data = self.getting_employers()
        employers = []
        for emp in data:
            employers.append(({
                'id': emp['id'],
                'name': emp['name'],
                'vacancies': emp['open_vacancies']
            }))
        return employers


    def getting_vacations(self):
        """
        Возвращает вакансий с удаленного сервера
        :return: (str) файл json
        """
        param = self.list_employers()
        response = requests.get("https://api.hh.ru/vacancies", param)
        return response.json().get("items")

    def filter_vacancy(self):
        """
        Формирует список вакансий, добавляемых в БД
        :return: (list) список вакансий
        """
        vacancies = self.getting_vacations()
        filter_data = []
        for vac in vacancies:
            if vac['salary'] == None:
                continue
            else:
                filter_data.append({
                    'vacancy_id': vac['id'],
                    'company_id': vac['employer'].get('id'),
                    'name': vac['name'],
                    'salary_from': vac['salary'].get('from'),
                    'salary_to': vac['salary'].get('to'),
                    "url": vac["alternate_url"],
                    'responsibility': vac['snippet'].get('responsibility')
                })
        return filter_data


if __name__ == '__main__':
    emp = GetData()
    print(emp.getting_employers())


