from files.flat import Bill, FlatMate
from files.report import PdfReport

the_bill = Bill(amount=120, period="April 2021")
john = FlatMate(name="John", days_in_house=20)
mary = FlatMate(name="marie", days_in_house=25)
print(john.pays(bill=the_bill,flatmate2=mary))
print(mary.pays(bill=the_bill,flatmate2=john))

pdf_report = PdfReport("Report.pdf")
pdf_report.generate(john, mary, the_bill)