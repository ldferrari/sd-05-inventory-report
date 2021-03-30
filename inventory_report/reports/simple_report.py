from datetime import date
from collections import Counter


# class SimpleReport:
# def generate(list):
#     today = date.today().isoformat()
#     oldest_fab_date = min([old["data_de_fabricacao"] for old in list])
#     closest_fab_date = min(
#         [
#             close["data_de_validade"]
#             for close in list
#             if close["data_de_validade"] > today
#         ]
#     )
#     return (
#         f"Data de fabricação mais antiga: {oldest_fab_date}\n"
#         f"Data de validade mais próxima: {closest_fab_date}\n"
#     )
class SimpleReport:
    @classmethod
    def generate(cls, list):
        today = date.today().isoformat()
        oldest_fab_date = min([old["data_de_fabricacao"] for old in list])
        next_fab_date = min(
            [
                close["data_de_validade"]
                for close in list
                if close["data_de_validade"] > today
            ]
        )
        companies = [co["nome_da_empresa"] for co in list]
        counting = Counter(companies)
        bs = max(counting)
        return (
            f"Data de fabricação mais antiga: {oldest_fab_date}\n"
            f"Data de validade mais próxima: {next_fab_date}\n"
            f"Empresa com maior quantidade de produtos estocados: {bs}\n"
        )