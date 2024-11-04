from typing import List
from collections import namedtuple

from django.db import connections


def fetch_data_from_mysql(table_name: str) -> List[namedtuple]:
    query = f"SELECT * FROM {table_name}"
    with connections["mysql"].cursor() as cursor:
        cursor.execute(query)
        Row = namedtuple("Row", [col[0] for col in cursor.description])
        rows = [Row(*row) for row in cursor.fetchall()]
    return rows
