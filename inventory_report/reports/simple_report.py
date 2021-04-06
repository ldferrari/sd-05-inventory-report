import datetime
from collections import Counter


def string_template(f, v, e):
    return f"""Data de fabricação mais antiga: {f}
Data de validade mais próxima: {v}
Empresa com maior quantidade de produtos estocados: {e}
"""


class SimpleReport:

    @classmethod
    def is_date_ok(self, param):
        current = datetime.datetime.now().date()
        if param > current:
            return param
        return False

    @classmethod
    def generate(self, data_list):
        empresas = []
        datas_de_fabricacao = []
        datas_de_validade = []

        for report in data_list:
            datas_de_fabricacao.append(
                datetime.date.fromisoformat(report["data_de_fabricacao"])
                )
            datein = self.is_date_ok(
                datetime.date.fromisoformat(report["data_de_validade"])
                )
            if datein:
                datas_de_validade.append(datein)    
            empresas.append(report["nome_da_empresa"])
            # c = Counter(self.empresas)

        fabric = min(datas_de_fabricacao).isoformat()
        valid = min(datas_de_validade).isoformat()
        emp = Counter(empresas).most_common(1)[0][0]

        return string_template(fabric, valid, emp)
