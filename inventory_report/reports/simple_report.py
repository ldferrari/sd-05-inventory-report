# Referências:
# https://stackoverflow.com/questions/3922644/find-oldest-youngest-datetime-object-in-a-list
# https://stackoverflow.com/questions/29511131/python-get-the-most-frequent-value-in-a-list-of-dictionaries

from collections import Counter
from datetime import date


class SimpleReport:
    @classmethod
    def generate(self, products):
        oldest_manufactured = min(
            [product["data_de_fabricacao"] for product in products]
        )
        closest_to_expire = min(
            [
                product["data_de_validade"]
                for product in products
                if product["data_de_validade"] > str(date.today())
            ]
        )
        company = Counter(
            product["nome_da_empresa"] for product in products
        ).most_common(1)[0][0]

        str1 = f"Data de fabricação mais antiga: {oldest_manufactured}\n"
        str2 = f"Data de validade mais próxima: {closest_to_expire}\n"
        str3 = (
            f"Empresa com maior quantidade de produtos estocados: {company}\n"
        )

        return str1 + str2 + str3
