from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, list):
        first = SimpleReport.generate(list)
        company = [comp["nome_da_empresa"] for comp in list]
        count = Counter(company)
        """ big_st = max(count) """
        stock = ''
        for com in count:
            stock += f"- {com}: {count[com]}\n"
        return (
            f"{first}\n"
            f"Produtos estocados por empresa: \n"
            f"{stock}"
        )
