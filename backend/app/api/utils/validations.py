import re


def is_cnpj_valid(cnpj: str) -> bool:
    if not re.match(r"\d{14}$", cnpj):
        return False
    return True
