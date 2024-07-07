from typing import List, Dict
from gspread import Client, Spreadsheet, Worksheet, service_account

from django.conf import settings


def client_init_json(file_path) -> Client:
    return service_account(filename=file_path)


def get_table_by_url(client: Client, table_url: str) -> Spreadsheet:
    return client.open_by_url(table_url)


def get_table_by_id(client: Client, table_url) -> Spreadsheet:
    return client.open_by_key(table_url)


def get_worksheet_info(table: Spreadsheet) -> dict:
    worksheets = table.worksheets()
    worksheet_info = {
        "count": len(worksheets),
        "names": [worksheet.title for worksheet in worksheets]
    }
    return worksheet_info


def extract_data_from_sheet(table: Spreadsheet, sheet_name: str) -> List[Dict]:
    worksheet = table.worksheet(sheet_name)
    rows = worksheet.get_all_records()
    return rows


async def get_data_from_sheet_a2():
    table_url = "https://docs.google.com/spreadsheets/d/1u7NZgcKDIZl_xXgYWpNju4GkIUc90F4SzqPLVYNQHdY/edit?gid=0#gid=0"
    client = client_init_json(f"{settings.BASE_DIR}/google-sheet.json")
    table = get_table_by_url(client, table_url)
    worksheet_info = get_worksheet_info(table)
    worksheet = table.worksheet(worksheet_info["names"][0])

    A2_value = worksheet.acell("A2").value

    return A2_value


async def add_data_to_sheet_b(value: str):
    table_url = "https://docs.google.com/spreadsheets/d/1u7NZgcKDIZl_xXgYWpNju4GkIUc90F4SzqPLVYNQHdY/edit?gid=0#gid=0"
    client = client_init_json(f"{settings.BASE_DIR}/google-sheet.json")
    table = get_table_by_url(client, table_url)
    worksheet_info = get_worksheet_info(table)
    worksheet = table.worksheet(worksheet_info["names"][0])
    worksheet.update_acell("B1", value)
