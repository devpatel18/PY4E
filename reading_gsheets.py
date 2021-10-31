from _future_ import print_function
from auth import spreadsheet_service
from auth import drive_service

def create():
    spreadsheet_details = {
    'properties': {
        'title': 'Parent-Sheet-test'
        }
    }
    sheet = spreadsheet_service.spreadsheets().create(body=spreadsheet_details,fields='spreadsheetId').execute()
    sheetId = sheet.get('spreadsheetId')
    print('Spreadsheet ID: {0}'.format(sheetId))
    permission1 = {
    'type': 'user',
    'role': 'writer',
    'emailAddress': 'jaygala260@gmail.com'
    }
    drive_service.permissions().create(fileId=sheetId, body=permission1).execute()
    return sheetId

def read_range(rangename, sprdsht_id):
    range_name = rangename
    spreadsheet_id = sprdsht_id
    result = spreadsheet_service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    rows = result.get('values', [])
    print('{0} rows retrieved.'.format(len(rows)))
    print('{0} rows retrieved.'.format(rows))
    return rows


def write_range(write_sprdshit_id, rangename,sprdsht_id):
    spreadsheet_id = write_sprdshit_id
    range_name = 'Sheet1'
    values = read_range(rangename,sprdsht_id)
    value_input_option = 'USER_ENTERED'
    body = {
        'values': values
    }
    result = spreadsheet_service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_name,valueInputOption=value_input_option, body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))

#write_range('1Pknfu2fkQyo9uFEkTYA_IrWiEYup2PMmsoJ8Lv73CqE','Sheet1!A2:C','13bta29UdtPXWOwUoK9yuM0V8UQW5RI1f3NuTqf6g1bA')

write_range('1Pknfu2fkQyo9uFEkTYA_IrWiEYup2PMmsoJ8Lv73CqE','Sheet1!A1:C',
            '1mMkgXb_NxiOetdMAqHJtSMiy5p5OHgvzv14NmYO5Bco')

def read_ranges():
    write_range()
    sheetId = '1JCEHwIa4ZzwAiKGmAnWGfbjeVCH_tWZF6MkIU0zICwM'
    range_names = ['Sheet1!A2:H21', 'Sheet1!A42:H62']
    result = spreadsheet_service.spreadsheets().values().batchGet(
     spreadsheetId=sheetId, ranges=range_names).execute()
    ranges = result.get('valueRanges', [])
    print('{0} ranges retrieved.'.format(len(ranges)))
    return ranges

def append():
    values = read_range('Sheet1!A2:C','13bta29UdtPXWOwUoK9yuM0V8UQW5RI1f3NuTqf6g1bA')
    body = {
        'values': values
    }
    result = spreadsheet_service.spreadsheets().values().append(
        spreadsheetId='1Pknfu2fkQyo9uFEkTYA_IrWiEYup2PMmsoJ8Lv73CqE',range='Sheet1', valueInputOption='USER_ENTERED',insertDataOption='INSERT_ROWS',body=body).execute()
    print('{0} cells updated.'.format(result.get('totalUpdatedCells')))
append()

#'Sheet1!A1:C','1mMkgXb_NxiOetdMAqHJtSMiy5p5OHgvzv14NmYO5Bco'