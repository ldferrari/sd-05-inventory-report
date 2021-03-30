from datetime import datetime
from collections import Counter


def str_to_date(string):
    return datetime.strptime(string, "%Y-%m-%d").date()


# def is_oldest(date1, date2):
#     return str_to_date(date1) > str_to_date(date2)


def get_oldest_fabrication_date(productsList):
    oldest_fab_date = str_to_date(productsList[0]["data_de_fabricacao"])
    for company in productsList:
        new_date = str_to_date(company["data_de_fabricacao"])
        if(new_date < oldest_fab_date):
            oldest_fab_date = new_date
    return oldest_fab_date


def nearest_due_date(productsList):
    nearest = str_to_date(productsList[0]["data_de_validade"])
    now = str_to_date(datetime.today().strftime("%Y-%m-%d"))
    for company in productsList:
        new_date = str_to_date(company["data_de_validade"])
        if(nearest > new_date > now):
            nearest_due_date = new_date
    return nearest_due_date


def big_stock(productsList):
    companies_list = []
    for product in productsList:
        companies_list.append(product["nome_da_empresa"])
    most_common_company = Counter(companies_list).most_common()
    return most_common_company


class SimpleReport:
    @classmethod
    def generate(cls, productsList):
        a = get_oldest_fabrication_date(productsList)
        al = f"Data de fabricação mais antiga: {a}"
        b = nearest_due_date(productsList)
        bl = f"Data de validade mais próxima: {b}"
        c = big_stock(productsList)[0][0]
        cl = f"Empresa com maior quantidade de produtos estocados: {c}"

        return (
          al + "\n" +
          bl + "\n" +
          cl + "\n"
        )
