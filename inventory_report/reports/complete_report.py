from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        report = super().generate(list)

        company_name = [item["nome_da_empresa"] for item in list]

        product_by_company = ""
        company_total = Counter(company_name)
        for name in company_total:
            product_by_company += f"- {name}: {company_total[name]}\n"

        final_report = (
            f"{report}\n"
            f"Produtos estocados por empresa: \n"
            f"{product_by_company}"
        )

        return final_report
