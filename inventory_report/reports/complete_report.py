from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def products_by_company(cls, list):
        companies = [data["nome_da_empresa"] for data in list]
        companies_number = Counter(companies)

        new_company = ""
        for company in companies_number:
            new_company += f"- {company}: {companies_number[company]}\n"
            return new_company

    @classmethod
    def generate(cls, list):
        simple_report = super().generate(list)
        report = ""
        report += f"{simple_report}\n"
        report += "Produtos estocados por empresa: \n"
        products = cls.product_by_company(list)
        report += f"{products}"
        return report
