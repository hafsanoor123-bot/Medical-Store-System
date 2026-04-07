from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

def generate_bill_pdf(filename, table_data, discount=0, total_amount=0):
    pdf = SimpleDocTemplate(filename, pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
    elements = []

    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleH = styles['Heading2']

    # Shop Name
    elements.append(Paragraph(f"<b>Rehman Medical Store</b>", styleH))
    elements.append(Paragraph(f"<b>Society Sukkur</b>", styleN))
    elements.append(Paragraph(f"Date/Time: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}", styleN))
    elements.append(Spacer(1, 12))  # space

    # Table
    table = Table(table_data, hAlign='LEFT', colWidths=[40, 200, 60, 60, 80])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.white),
        ('TEXTCOLOR',(0,0),(-1,0),colors.black),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('ALIGN',(1,1), (1,-1), 'LEFT')  # Description left align
    ]))
    elements.append(table)
    elements.append(Spacer(1, 12))

    # Discount and Total
    elements.append(Paragraph(f"Discount: {discount}", styleN))
    elements.append(Paragraph(f"<b>Total Amount: {total_amount}</b>", styleN))

    pdf.build(elements)