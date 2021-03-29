from datetime import datetime as d
from collections import Counter


def str_date_to_number(string_date):
    return d.strptime(string_date, "%Y-%m-%d").date()


def find_oldest_product(stock):
    oldest_date = str_date_to_number(stock[0]["data_de_fabricacao"])
    for empresa in stock:
        date_candidate = str_date_to_number(empresa["data_de_fabricacao"])
        if date_candidate < oldest_date:
            oldest_date = date_candidate
    return oldest_date


def find_first_product_to_expire(stock):
    nearest = str_date_to_number(stock[0]["data_de_validade"])
    today = str_date_to_number(d.today().strftime("%Y-%m-%d"))
    for empresa in stock:
        date_candidate = str_date_to_number(empresa["data_de_validade"])
        if date_candidate < nearest and date_candidate > today:
            nearest = date_candidate
    return nearest


def find_bigger_stock_company(stock):
    companies_list = []
    for empresa in stock:
        companies_list.append(empresa["nome_da_empresa"])
    most_repeated_company = Counter(companies_list).most_common(1)

    return most_repeated_company[0][0]


class SimpleReport:
    @classmethod
    def generate(cls, stock):
        oldest_date = find_oldest_product(stock)
        nearest_to_expire = find_first_product_to_expire(stock)
        bg = find_bigger_stock_company(stock)
        line1 = f"Data de fabricação mais antiga: {oldest_date}"
        line2 = f"Data de validade mais próxima: {nearest_to_expire}"
        line3 = f"Empresa com maior quantidade de produtos estocados: {bg}"
        return f"{line1}\n{line2}\n{line3}\n"
