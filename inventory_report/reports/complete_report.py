from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        report_p1 = SimpleReport.generate(list)
        companies = [co["nome_da_empresa"] for co in list]
        counting = Counter(companies)
        co_stock = ""
        for cia in counting:
            co_stock += f"- {cia}: {counting[cia]}\n"

        return (
            f"{report_p1}\n"
            f"Produtos estocados por empresa: \n"
            f"{co_stock}"
        )
