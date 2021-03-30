from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    # Always use cls for the first argument to class methods.
    @classmethod
    def generate(cls, list):
        simplereport = super().generate(list)

        empresas = [data["nome_da_empresa"] for data in list]
        empresas_contadas = Counter(empresas)

        filtered_counter = []
        for nome in empresas_contadas:
            filtered_counter.append(f"- {nome}: {empresas_contadas[nome]}")

        relatorio = (
                f"{simplereport}\n"
                f"Produtos estocados por empresa: \n"
                f"{filtered_counter[0]}\n"
                f"{filtered_counter[1]}\n"
                f"{filtered_counter[2]}\n"
            )

        return relatorio
