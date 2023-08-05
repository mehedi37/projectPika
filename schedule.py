import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import datetime
load_dotenv()

def routine():
    sheetJson = os.getenv("SHEET_JSON")
    sheetName = os.getenv("SHEET_NAME")
    workSheetName = os.getenv("WORK_SHEET_NAME")

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(sheetJson, scope)

    client = gspread.authorize(credentials)

    spreadsheet = client.open(sheetName)

    worksheet = spreadsheet.worksheet(workSheetName)

    data = worksheet.get_all_values()

    # Get current time
    current_time = datetime.datetime.now().time()

    # Find today's date
    today = datetime.datetime.now().strftime("%A")

    # Find tomorrow's date
    tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%A")
    # print(today, tomorrow)

    # Find the row index corresponding to today's or tomorrow's date
    date_row_index = None
    for i, row in enumerate(data):
        if row[0].strip() == today:
            date_row_index = i
            break
        if row[0].strip() == tomorrow:
            date_row_index = i
            break

    # Get column index of current time
    column_index = None
    if date_row_index is not None:
        for i, time_slot in enumerate(data[date_row_index][1:]):
            # print(data[0][i+1])
            if time_slot != 'No Class':
                time_slot_time = datetime.datetime.strptime(data[0][i+1], "%I:%M %p").time()
                if current_time < time_slot_time:
                    column_index = i + 1
                    break

    # If current time is between 12:00 am and 8:00 am, set column index to 1 (today's first class)
    if datetime.time(hour=0) <= current_time < datetime.time(hour=8):
        column_index = 1


    # If current time is after 5 PM or no valid column index found, set column index to 1 and increment date_row_index
    if datetime.datetime.now().time() >= datetime.time(hour=17) or column_index is None:
        column_index = 1
        date_row_index += 1


    # Get next class time from the next row
    next_class = data[date_row_index][column_index]
    response = f"Next class is {next_class},At {data[0][column_index]}, At {data[date_row_index][0]}"
    return(response)

if __name__ == "__main__":
    print(routine())