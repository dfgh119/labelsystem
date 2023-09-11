import tkinter as tk
from tkinter import ttk
import pandas as pd

def select_sheet(data_frame):
    selected_sheets = []

    def add_sheet():
        selected_indices = sheet_listbox.curselection()
        for index in selected_indices:
            selected_sheet = sheet_listbox.get(index)
            if selected_sheet not in selected_sheets:
                selected_sheets.append(selected_sheet)
        selected_sheets_label.config(text=f"선택된 시트 목록: {', '.join(selected_sheets)}")

    def remove_sheet():
        selected_indices = sheet_listbox.curselection()
        for index in selected_indices:
            selected_sheet = sheet_listbox.get(index)
            if selected_sheet in selected_sheets:
                selected_sheets.remove(selected_sheet)
        selected_sheets_label.config(text=f"선택된 시트 목록: {', '.join(selected_sheets)}")

    def done():
        root.quit()

    root = tk.Tk()
    root.title("시트 선택")

    sheet_list = data_frame.sheet_names

    sheet_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
    for sheet in sheet_list:
        sheet_listbox.insert(tk.END, sheet)
    sheet_listbox.pack(padx=20, pady=10)

    add_button = ttk.Button(root, text="추가", command=add_sheet)
    add_button.pack()

    remove_button = ttk.Button(root, text="제거", command=remove_sheet)
    remove_button.pack()

    selected_sheets_label = ttk.Label(root, text="선택된 시트 목록:")
    selected_sheets_label.pack(pady=10)

    done_button = ttk.Button(root, text="완료", command=done)
    done_button.pack()

    root.mainloop()

    return selected_sheets

# 사용 예시:
# data_frame = pd.read_excel('파일경로/파일이름.xlsx')
# selected_sheets = select_sheet(data_frame)
# print("선택된 시트 목록:", selected_sheets)
