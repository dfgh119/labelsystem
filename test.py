import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filename = askopenfilename(initialdir=".")

# 엑셀 파일을 읽어옵니다.
df = pd.read_excel(filename)

# 사용자가 원하는 조건 열과 값을 지정합니다.
조건_열 = '조건_열_이름'
조건_값 = '조건_값'

# 조건에 맞는 행을 선택합니다.
조건에_맞는_행 = df[df[조건_열] == 조건_값]

# 결과를 출력합니다.
print("조건에 맞는 행:")
print(조건에_맞는_행)
