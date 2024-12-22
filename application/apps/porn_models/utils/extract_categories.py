from typing import List
import re


def extract_categories(content: str, categories: List[str]) -> List[str]:
    words = [word.strip() for word in re.split("\s+|'", content)]

    return list(set(categories).intersection(words))
