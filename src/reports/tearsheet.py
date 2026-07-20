from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


def generate_tearsheet(company):

    pdf = SimpleDocTemplate(
        f"reports/{company}_tearsheet.pdf"
    )

    styles = getSampleStyleSheet()

    story = []

    # =========================
    # HEADER
    # =========================

    story.append(
        Paragraph(
            f"<font size='22' color='darkblue'><b>{company}</b></font>",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            "Nifty100 Analytics Company Tearsheet",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1, 0.3 * inch))

    # =========================
    # COMPANY INFORMATION
    # =========================

    company_info = [
        ["Company", company],
        ["Sector", "Information Technology"],
        ["Sub Sector", "Software Services"],
        ["NSE Symbol", company],
        ["Market Cap", "₹15,00,000 Cr"]
    ]

    table = Table(company_info, colWidths=[2 * inch, 4 * inch])

    table.setStyle(TableStyle([

        ("BACKGROUND", (0,0), (0,-1), colors.lightblue),

        ("GRID", (0,0), (-1,-1), 1, colors.black),

        ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),

        ("BOTTOMPADDING", (0,0), (-1,-1), 8)

    ]))

    story.append(table)

    story.append(Spacer(1, 0.3 * inch))

    # =========================
    # KPI SECTION
    # =========================

    story.append(
        Paragraph(
            "<b>Key Performance Indicators</b>",
            styles["Heading2"]
        )
    )

    kpi = [

        ["ROE", "24.6%"],

        ["ROCE", "31.2%"],

        ["Net Profit Margin", "19.5%"],

        ["Debt / Equity", "0.18"],

        ["Revenue CAGR", "15%"],

        ["Free Cash Flow", "₹12,000 Cr"]

    ]

    table = Table(kpi, colWidths=[3 * inch, 2 * inch])

    table.setStyle(TableStyle([

        ("GRID", (0,0), (-1,-1), 1, colors.black),

        ("BACKGROUND", (0,0), (0,-1), colors.whitesmoke),

        ("FONTNAME", (0,0), (-1,-1), "Helvetica"),

        ("BOTTOMPADDING", (0,0), (-1,-1), 8)

    ]))

    story.append(table)

    story.append(Spacer(1, 0.3 * inch))

    # =========================
    # REVENUE SUMMARY
    # =========================

    story.append(
        Paragraph(
            "<b>Revenue & Profit Summary</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            "Revenue has shown consistent growth over the past 10 years with improving profitability.",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 0.2 * inch))

    # =========================
    # BALANCE SHEET
    # =========================

    story.append(
        Paragraph(
            "<b>Balance Sheet</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            "Healthy equity base with low debt and improving reserves.",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 0.2 * inch))

    # =========================
    # CASH FLOW
    # =========================

    story.append(
        Paragraph(
            "<b>Cash Flow Summary</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            "Operating cash flow remains positive with healthy free cash flow generation.",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 0.3 * inch))

    # =========================
    # PROS
    # =========================

    story.append(
        Paragraph(
            "<font color='green'><b>Pros</b></font>",
            styles["Heading2"]
        )
    )

    pros = [

        "✔ High Return on Equity",

        "✔ Strong Free Cash Flow",

        "✔ Debt Free Balance Sheet",

        "✔ Consistent Revenue Growth"

    ]

    for item in pros:

        story.append(
            Paragraph(item, styles["BodyText"])
        )

    story.append(Spacer(1, 0.2 * inch))

    # =========================
    # CONS
    # =========================

    story.append(
        Paragraph(
            "<font color='red'><b>Cons</b></font>",
            styles["Heading2"]
        )
    )

    cons = [

        "✖ Premium Valuation",

        "✖ Revenue Growth Moderating",

        "✖ Expensive compared to peers"

    ]

    for item in cons:

        story.append(
            Paragraph(item, styles["BodyText"])
        )

    story.append(Spacer(1, 0.3 * inch))

    # =========================
    # CAPITAL ALLOCATION
    # =========================

    story.append(
        Paragraph(
            "<b>Capital Allocation</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            "Pattern : <b>Reinvestor</b>",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 0.4 * inch))

    # =========================
    # FOOTER
    # =========================

    story.append(
        Paragraph(
            "Generated by Nifty100 Analytics Dashboard",
            styles["Italic"]
        )
    )

    pdf.build(story)