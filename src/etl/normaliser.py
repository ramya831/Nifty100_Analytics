import re


def normalize_year(year):

    year = str(year).strip()

    # Handle FY2024, FY-2024, 2024 etc.
    match = re.search(r"\d{4}", year)

    if match:
        return int(match.group())

    # Handle 2024.0
    return int(year.replace(".0", ""))


def normalize_ticker(ticker):

    if ticker is None:
        return None

    return str(ticker).upper().strip()


def normalize_company_name(name):

    if name is None:
        return None

    return str(name).strip()


def normalize_text(value):

    if value is None:
        return None

    return str(value).strip()