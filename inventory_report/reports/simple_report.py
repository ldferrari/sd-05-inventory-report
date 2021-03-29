from datetime import date
from collections import Counter

# mock taken from inventory.json
mock = [
  {
    "id": "1",
    "nome_do_produto": "Nicotine Polacrilex",
    "nome_da_empresa": "Target Corporation",
    "data_de_fabricacao": "2020-02-18",
    "data_de_validade": "2022-09-17",
    "numero_de_serie": "CR25 1551 4467 2549 4402 1",
    "instrucoes_de_armazenamento": "instrucao 1"
  },
  {
    "id": "2",
    "nome_do_produto": "fentanyl citrate",
    "nome_da_empresa": "Target Corporation",
    "data_de_fabricacao": "2019-12-06",
    "data_de_validade": "2022-12-25",
    "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
    "instrucoes_de_armazenamento": "instrucao 2"
  },
  {
    "id": "3",
    "nome_do_produto": "NITROUS OXIDE",
    "nome_da_empresa": "Galena Biopharma",
    "data_de_fabricacao": "2019-12-22",
    "data_de_validade": "2023-11-07",
    "numero_de_serie": "CZ09 8588 0858 8435 9140 2695",
    "instrucoes_de_armazenamento": "instrucao 3"
  }
]


def find_oldest(data):
    creation_dates = [
        product["data_de_fabricacao"] for product in data
    ]
    print(f"fabrication product dates: {creation_dates}")
    return min(creation_dates)
    # min takes the earliest date


def find_closest_expiry(data):
    today = date.today().isoformat()
    not_expired_product_dates = [
        product["data_de_validade"]
        for product in data
        if product["data_de_validade"] >= today
    ]
    print(f"product validity dates: {not_expired_product_dates}")
    return min(not_expired_product_dates)
    # extracting the closest future date from now on


def find_biggest_stock(data):
    count = Counter(company["nome_da_empresa"] for company in data)
    print(f"count: {count}")
    return max(count)


class SimpleReport:

    @classmethod
    def generate(cls, inventory):
        oldest = find_oldest(inventory)
        closest_expiry = find_closest_expiry(inventory)
        bg = find_biggest_stock(inventory)
        old_line = f"Data de fabricação mais antiga: {oldest}"
        expiry_line = f"Data de validade mais próxima: {closest_expiry}"
        cie_line = f"Empresa com maior quantidade de produtos estocados: {bg}"
        report = f"{old_line}\n{expiry_line}\n{cie_line}\n"
        return report


if __name__ == "__main__":
    # checks if file executed directly or called elsewhere
    print(SimpleReport.generate(mock))
# here used to test the generate method with an example of inventory

# https://docs.python.org/3/library/datetime.html#date-objects
# https://docs.python.org/3/library/collections.html#collections.Counter
