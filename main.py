from fpdf import FPDF
import pandas as pd
import random

pdf = FPDF(orientation='P', unit='mm', format='A4')

df = pd.read_csv('topics.csv',  sep=',')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font('Times', style='B', size=24)
    pdf.set_text_color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    #pdf.cell(w=0, h=12, txt=row["Topic"], align='L', ln=1, border='B')
    pdf.cell(w=0, h=12, txt=row["Topic"], align='L', ln=1)
    pdf.line(10, 21, 200, 21)
    num_pages = row['Pages'] - 1
    #while True:
    #    if num_pages == 0:
    #        break
    #    else:
    #        pdf.add_page()
    #        num_pages = num_pages - 1
    for i in range(row['Pages'] - 1):
        pdf.add_page()


pdf.output('output.pdf')