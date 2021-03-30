from datetime import date
from collections import Counter

products = [
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
        "nome_da_empresa": "Sanofi-aventis U.S. LLC",
        "data_de_fabricacao": "2020-05-31",
        "data_de_validade": "2023-01-17",
        "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
        "instrucoes_de_armazenamento": "duis bibendum morbi",
    },
    {
        "id": 3,
        "nome_do_produto": "Dexamethasone Sodium Phosphate",
        "nome_da_empresa": "Sanofi-aventis U.S. LLC",
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


class SimpleReport:
    def __init__(self):
        pass

    @classmethod
    def generate(cls, products):
        # https://docs.python.org/3/library/datetime.html#date-objects
        iso_today = date.today().isoformat()

        oldest_product = min(
            [expiration["data_de_fabricacao"] for expiration in products]
        )

        newest_product = min(
            [
                expiration["data_de_validade"]
                for expiration in products
                if expiration["data_de_validade"] > iso_today
            ]
        )

        # https://docs.python.org/3/library/collections.html#collections.Counter
        companies = Counter(
            company["nome_da_empresa"] for company in products
        ).most_common(1)[0][0]  # to get rid of [] and () and get only the str

        report = (
            f"Data de fabricação mais antiga: {oldest_product}\n"
            f"Data de validade mais próxima: {newest_product}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{companies}\n"
        )

        return report


SimpleReport.generate(products)
