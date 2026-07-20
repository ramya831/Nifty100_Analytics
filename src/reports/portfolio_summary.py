from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
import os


def generate_portfolio_summary(companies):

    os.makedirs("reports/portfolio", exist_ok=True)

    pdf = SimpleDocTemplate(
        "reports/portfolio/portfolio_summary.pdf"
    )

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<font size=22 color='navy'><b>Nifty100 Portfolio Summary</b></font>",
            styles["Title"]
        )
    )

    story.append(Spacer(1,20))

    for company in companies:

        story.append(
            Paragraph(
                f"<b>{company['Ticker']}</b> - {company['Sector']}",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                f"ROE : {company['ROE']}% ↑",
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                f"Revenue CAGR : {company['Revenue CAGR']}% ↑",
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                f"Debt Equity : {company['DE']}",
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                f"FCF Yield : {company['FCF']}%",
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                f"P/E : {company['PE']}",
                styles["BodyText"]
            )
        )

        story.append(Spacer(1,18))

    pdf.build(story)

    print("Portfolio Summary Generated")