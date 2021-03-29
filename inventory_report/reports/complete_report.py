from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        # https://www.w3schools.com/python/ref_func_super.asp
        simple_report = super().generate(products)

        companies = Counter(
            [company["nome_da_empresa"] for company in products]
        )

        quantity = []
        for company in companies:
            quantity.append(f"- {company}: {companies[company]}\n")

        product_quantity = "".join(map(str, quantity))

        report = (
            f"{simple_report}\n"
            f"Produtos estocados por empresa: \n"
            f"{product_quantity}"
        )

        return report
