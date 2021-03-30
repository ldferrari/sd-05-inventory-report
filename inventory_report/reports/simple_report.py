from datetime import date
from collections import Counter


test_function = [
    {
        "id": 1,
        "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2020-07-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
        "instrucoes_de_armazenamento": "in blandit ultrices enim",
    },
    {
        "id": 2,
        "nome_do_produto": "sodium ferric gluconate complex",
        "nome_da_empresa": "sanofi-aventis U.S. LLC",
        "data_de_fabricacao": "2020-05-31",
        "data_de_validade": "2023-01-17",
        "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
        "instrucoes_de_armazenamento": "duis bibendum morbi",
    },
    {
        "id": 3,
        "nome_do_produto": "Dexamethasone Sodium Phosphate",
        "nome_da_empresa": "sanofi-aventis U.S. LLC",
        "data_de_fabricacao": "2019-09-13",
        "data_de_validade": "2023-02-13",
        "numero_de_serie": "BA52 2034 8595 7904 7131",
        "instrucoes_de_armazenamento": "morbi quis tortor id",
    },
    {
        "id": 4,
        "nome_do_produto": "Uricum acidum, Benzoicum acidum",
        "nome_da_empresa": "Newton Laboratories, Inc.",
        "data_de_fabricacao": "2019-11-08",
        "data_de_validade": "2019-11-25",
        "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
        "instrucoes_de_armazenamento": "velit eu est congue elementum",
    },
]


def stock_count(products):
    companies = Counter(
        name["nome_da_empresa"] for name in products
    ).most_common(1)
    return companies


class SimpleReport:
    @classmethod
    def generate(self, products_list):
        oldest = min(
            data_fabrica["data_de_fabricacao"]
            for data_fabrica in products_list
        )
        next_to_expire = min(
            data_validade["data_de_validade"]
            for data_validade in products_list
            if data_validade["data_de_validade"] > str(date.today())
        )
        b_stock = stock_count(products_list)
        r1 = f"Data de fabricação mais antiga: {oldest}\n"
        r2 = f"Data de validade mais próxima: {next_to_expire}\n"
        r3 = "Empresa com maior quantidade de produtos estocados:"
        return f"{r1}{r2}{r3} {b_stock[0][0]}\n"


# print(SimpleReport.generate(test_function))
