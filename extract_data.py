import pandas as pd
import select_excel_file

df = select_excel_file.select_file()
last_column_index = df.columns[-1]

# 예제로 함수를 호출하는 방법:
print(last_column_index)
