from openpyexcel import load_workbook, workbook
from appium.webdriver.common.appiumby import AppiumBy
class Excel_test_data:
    pass

def locators_fetch_from_excel(file_path,sheet_name, coloumn1, coloumn2):
    wb = load_workbook(file_path)
    ws = wb[sheet_name]
    max_rows = ws.max_row
    max_col = ws.max_column
    for row in range(2, max_rows+1):
        for col in range(1, max_col+1):
            setattr(Excel_test_data, ws[coloumn1+str(row)].value, eval(ws[coloumn2+str(row)].value))