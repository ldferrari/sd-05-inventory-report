from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    # Always use cls for the first argument to class methods.
    @classmethod
    def generate(cls, list):
        # Herda metodo generate da classe SimpleReport
        simplereport = super().generate(list)

        # Lista de compreensão -  coloca todos itens
        # "nome_da_empresa" na lista empresas
        empresas = [data["nome_da_empresa"] for data in list]

        # Counter agrupa ocorrencias {"empresa_a", "2"}
        empresas_contadas = Counter(empresas)

        filtered_counter = []
        for nome in empresas_contadas:
            filtered_counter.append(f"- {nome}: {empresas_contadas[nome]}")

        # Ler o array e formata em uma unica string
        # Para facilitar o relatório
        completereport = ""
        for company in empresas_contadas:
            completereport += (
                f"- {company}: {empresas_contadas[company]}\n"
            )

        relatorio = (
                f"{simplereport}\n"
                f"Produtos estocados por empresa: \n"
                f"{completereport}"
            )

        return relatorio
