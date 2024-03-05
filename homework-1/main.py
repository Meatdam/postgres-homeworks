"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
from config import CUSTOMERS, EMPLOYEES, ORDERS


def open_file(file_name) -> list:
    """
    Открывает csv файл и добавляет все элементы в список словарей "file_list"
    меняет и явно указывает на employee_id значение (Integer)
    :return: list(file_list)
    """
    file_list = []

    with open(file_name) as file:
        csv_file = csv.DictReader(file)
        for files in csv_file:
            if files.get('employee_id'):
                files['employee_id'] = int(files['employee_id'])
            file_list.append(files)
    return file_list


def add_database_posgres(data_list: list, name_table: str) -> None:
    """
    Коннектится с базой данных "north"
    Добавляет список словарей в базу данных "north"
    Количество столбцов не имеет значение так как явно умножатся на ее длину
    :return: None
    print(все значения таблицы)
    """
    with psycopg2.connect(host='localhost', database='north', user='postgres',
                          password='1234') as conn:
        with conn.cursor() as cur:
            for data_info in data_list:
                count = '%s ' * len(data_info)
                val = tuple(data_info.values())
                cur.execute(f"INSERT INTO {name_table} VALUES ({', '.join(count.split())})", val)
                print(val)
    conn.close()


if __name__ == '__main__':
    data_employees = open_file(EMPLOYEES)
    add_database_posgres(data_employees, 'employees')

    data_customers = open_file(CUSTOMERS)
    add_database_posgres(data_customers, 'customers')

    data_orders = open_file(ORDERS)
    add_database_posgres(data_orders, 'orders')
