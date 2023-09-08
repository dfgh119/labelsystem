import tkinter as tk
from tkinter import filedialog
import pandas as pd

def select_file():
    # tkinter 초기화
    root = tk.Tk()
    root.withdraw() # 루트창 숨김

    # 파일 선택
    file_path = filedialog.askopenfilename(filetypes=[("excel file", "*.xlsx")])

    # 파일이 선택되지 않았을 경우
    if file_path == "":
        print("파일이 선택되지 않았습니다.")
        return None

    # 파일 읽기
    df = pd.read_excel(file_path)

    # 파일 출력
    print("불러온 데이터 : ", df)

    # 프로그램 종료
    root.destroy()

    return df

# 예시 사용법
# data_frame = select_file()

# 이제 data_frame 변수에 엑셀 데이터가 저장됩니다.
