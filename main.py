import pandas as pd
import select_excel_file
import select_sheet


# 엑셀 파일 선택, select_file.py의 select_file() 함수를 사용합니다.
data_frame = select_excel_file.select_file()
# 사용자가 선택한 sheet 목록을 불러옵니다.
sheet_list = select_sheet.select_sheet(data_frame)
print ("선택된 시트 목록:", sheet_list)
