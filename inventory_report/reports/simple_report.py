from datetime import date
from collections import Counter

stock = [
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


def string_template(f, v, e):
    return f"""Data de fabricação mais antiga: {f}
Data de validade mais próxima: {v}
Empresa com maior quantidade de produtos estocados: {e}
"""


class SimpleReport:
    @classmethod
    def generate(self, data_list):
        datas_de_fabricacao = []
        datas_de_validade = []
        empresas = []

        for report in data_list:
            datas_de_fabricacao.append(
                date.fromisoformat(report["data_de_fabricacao"])
                )
            datas_de_validade.append(
                date.fromisoformat(report["data_de_validade"])
                )
            empresas.append(report["nome_da_empresa"])
            c = Counter(empresas)

        fabric = min(datas_de_fabricacao).isoformat()
        valid = max(datas_de_validade).isoformat()
        emp = c.most_common(1)[0][0]
 
        return string_template(fabric, valid, emp)


if __name__ == "__main__":
    report = SimpleReport.generate(stock)
    print(report)
