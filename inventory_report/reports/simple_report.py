import datetime
from collections import Counter


def string_template(f, v, e):
    return f"""Data de fabricação mais antiga: {f}
Data de validade mais próxima: {v}
Empresa com maior quantidade de produtos estocados: {e}
"""


class SimpleReport:

    datas_de_fabricacao = []
    datas_de_validade = []
    empresas = []

    @classmethod
    def is_date_ok(self, param):
        current = datetime.datetime.now().date()
        if param > current:
            self.datas_de_validade.append(param)

    @classmethod
    def generate(self, data_list):

        for report in data_list:
            self.datas_de_fabricacao.append(
                datetime.date.fromisoformat(report["data_de_fabricacao"])
                )
            self.is_date_ok(
                datetime.date.fromisoformat(report["data_de_validade"])
                )
            self.empresas.append(report["nome_da_empresa"])
            c = Counter(self.empresas)

        fabric = min(self.datas_de_fabricacao).isoformat()
        valid = min(self.datas_de_validade).isoformat()
        emp = c.most_common(1)[0][0]

        return string_template(fabric, valid, emp)
