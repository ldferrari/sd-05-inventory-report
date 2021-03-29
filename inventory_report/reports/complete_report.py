from inventory_report.reports.simple_report import mock, SimpleReport
from collections import Counter


def mount_extra_report(data):
    companies = Counter(cie["nome_da_empresa"] for cie in data)
    # extracts company name as key and stock quantity as value
    products_stock = "Produtos estocados por empresa: \n"
    for cie in companies:
        products_stock = (
            products_stock + f"- {cie}: {companies[cie]}\n"
        )
    # mounting the report structure the way we want it
    # (with unique intro sentence and then each company with its stock qty)
    extra_report = products_stock
    return extra_report


class CompleteReport(SimpleReport):

    @classmethod
    def generate(cls, data):
        simple_report = SimpleReport.generate(data)
        # could also be: simple_report = super().generate(data)
        # https://www.w3schools.com/python/ref_func_super.asp
        extra_report = mount_extra_report(data)
        complete_report = f"{simple_report}\n{extra_report}"
        return complete_report


if __name__ == "__main__":
    print(CompleteReport.generate(mock))

# why cls instead of self
# "self is a parameter name used in instance methods,
#  cls is a parameter name used in class methods"
# https://www.quora.com/What-is-the-difference-between-self-and-cls-in-Python

# Academic honesty for reqs 1&2: consulted and combined PRs
# https://github.com/tryber/sd-05-inventory-report/pull/2/files
# https://github.com/tryber/sd-05-inventory-report/pull/4/files
# https://github.com/tryber/sd-04-inventory-report/pull/21/files
