from openpyexcel import load_workbook, workbook

def Excel_data_read(excel_file, sheet_name, column1, coloumn2):
    locators_dict   = {}
    wb = load_workbook(rf"{excel_file}")
    ws = wb[sheet_name]
    max_rows = ws.max_row
    max_col = ws.max_column
    for row in range(2, max_rows+1):
        for col in range(1, max_col+1):
            locators_dict[ws[column1+str(row)].value] = ws[coloumn2+str(row)].value
    return locators_dict
            
# res = Excel_data_read(r"../Data_setup/test_data_fk.xlsx", 'locators', 'A', 'B')
# print(res)
# for key, item in res.items():
#     print(key, item)