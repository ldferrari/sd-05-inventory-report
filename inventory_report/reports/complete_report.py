from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, stock):
        simple = super().generate(stock)

        complete_report = simple + '\n' + "Produtos estocados por empresa: \n"

        companies_list = []
        for empresa in stock:
            companies_list.append(empresa["nome_da_empresa"])
        counted = Counter(companies_list)

        for key, value in dict(counted).items():
            complete_report += f"- {key}: {value}\n"

        return complete_report
