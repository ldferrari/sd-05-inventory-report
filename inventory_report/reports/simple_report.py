from datetime import date
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(self, list):
        nowadays = date.today().isoformat()
        old_fab = min([old["data_de_fabricacao"] for old in list])
        near_expire = min(
            [
                near["data_de_validade"]
                for near in list
                if near["data_de_validade"] > nowadays
            ]
        )
        company = [comp["nome_da_empresa"] for comp in list]
        count = Counter(company)
        big_st = max(count)
        return (
            f"Data de fabricação mais antiga: {old_fab}\n"
            f"Data de validade mais próxima: {near_expire}\n"
            f"Empresa com maior quantidade de produtos estocados: {big_st}\n"
        )
