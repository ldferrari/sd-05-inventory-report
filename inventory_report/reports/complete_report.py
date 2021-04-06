from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, lista):
        relatorio_simples = super().generate(lista)

        nome_empresa = [item["nome_da_empresa"] for item in lista]

        produtos_p_empresa = ""

        total_empresas = Counter(nome_empresa)
        for nome in total_empresas:
            produtos_p_empresa += f"- {nome}: {total_empresas[nome]}\n"

        relatorio_final = (
            f"{relatorio_simples}\n"
            f"Produtos estocados por empresa: \n"
            f"{produtos_p_empresa}"
        )

        return relatorio_final
