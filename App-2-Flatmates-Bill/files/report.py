import os
import webbrowser

from fpdf import FPDF


class PdfReport:
    """ create a pdf report contain data about flatmates, bill, period"""
    def __init__(self, file):
        self.file = file

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation="P",
                   unit='pt',
                   format='A4')

        pdf.add_page()

        # add an image
        pdf.image("house.png", w=30, h=30)
        flatmate1_pays = str(round(flatmate1.pays(bill, flatmate2),2))
        flatmate2_pays = str(round(flatmate2.pays(bill, flatmate1),2))
        # add some text
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatemates Bill", border=0, align='C', ln=1)
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0,ln=1)

        # insert name and bill
        pdf.set_font(family='Times', size=12, style='B')
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt= flatmate1_pays, border=0, ln=1)

        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pays, border=0)
        pdf.output(self.file)
        webbrowser.open('file://' + os.path.realpath(self.file))
        #pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        #pdf.cell(w=150, h=40, txt=bill.period, border=1)
        #pdf.output("bill.pdf")
        #pass