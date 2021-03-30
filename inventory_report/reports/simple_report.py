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
    return most_common_company[0][0]


class SimpleReport:
    @classmethod
    def generate(cls, productsList):
        a = get_oldest_fabrication_date(productsList)
        al = f"Data de fabricação mais antiga: {a}"
        b = nearest_due_date(productsList)
        bl = f"Data de validade mais próxima: {b}"
        c = big_stock(productsList)
        cl = f"Empresa com maior quantidade de produtos estocados: {c}"

        return (
          al + "\n" +
          bl + "\n" +
          cl + "\n"
        )


test = [
        {
            "id": "1",
            "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2020-07-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
            "instrucoes_de_armazenamento": "in blandit ultrices enim",
        },
        {
            "id": "2",
            "nome_do_produto": "sodium ferric gluconate complex",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2020-05-31",
            "data_de_validade": "2023-01-17",
            "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
            "instrucoes_de_armazenamento": "duis bibendum morbi",
        },
        {
            "id": "3",
            "nome_do_produto": "Dexamethasone Sodium Phosphate",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2019-09-13",
            "data_de_validade": "2023-02-13",
            "numero_de_serie": "BA52 2034 8595 7904 7131",
            "instrucoes_de_armazenamento": "morbi quis tortor id",
        },
        {
            "id": "4",
            "nome_do_produto": "Uricum acidum, Benzoicum acidum",
            "nome_da_empresa": "Newton Laboratories",
            "data_de_fabricacao": "2019-11-08",
            "data_de_validade": "2019-11-25",
            "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
            "instrucoes_de_armazenamento": "velit eu est congue elementum",
        },
    ]
# print(get_oldest_fabrication_date(test))
# print(nearest_due_date(test))
# print(big_stock(test))

print(SimpleReport.generate(test))
