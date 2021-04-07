from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):

    @classmethod
    def product_by_company(cls, list):
        companys = [data["nome_da_empresa"] for data in list]
        companys_number = Counter(companys)

        edit_companys = ""
        for company in companys_number:
            edit_companys += (f"- {company}: {companys_number[company]}\n")
        return edit_companys

    @classmethod
    def generate(cls, list):
        simple_report = super().generate(list)
        report = ""
        report += (f"{simple_report}\n")
        report += ("Produtos estocados por empresa: \n")
        products = cls.product_by_company(list)
        report += (f"{products}")
        return report
