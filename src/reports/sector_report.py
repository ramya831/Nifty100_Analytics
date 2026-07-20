from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import os


def generate_sector_report(sector_name, companies):
    os.makedirs("reports/sector", exist_ok=True)

    pdf = SimpleDocTemplate(
        f"reports/sector/{sector_name}_report.pdf"
    )

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            f"<font size=22 color='navy'><b>{sector_name} Sector Report</b></font>",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"Total Companies: {len(companies)}",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1, 15))

    data = [["Company", "ROE", "Revenue"]]

    for company in companies:
        data.append([
            company["Company"],
            company["ROE"],
            company["Revenue"]
        ])

    table = Table(data, colWidths=[2.5*inch, 1.2*inch, 2*inch])

    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.navy),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("BACKGROUND", (0,1), (-1,-1), colors.beige),
        ("ALIGN", (1,1), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0,0), (-1,0), 10),
    ]))

    story.append(table)

    pdf.build(story)

    print(f"{sector_name} Sector Report Generated")