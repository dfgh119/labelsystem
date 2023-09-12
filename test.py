import tkinter as tk
from tkinter import ttk

def add_table():
    # 표를 추가하고 크기 조정을 위한 새 창 생성
    table_window = tk.Toplevel(root)
    table_window.title("표 추가 및 크기 조정")

    # 표 크기를 조정하기 위한 스크롤바 생성
    table_scrollbar = ttk.Scrollbar(table_window, orient="vertical")
    table_scrollbar.grid(row=0, column=1, sticky="ns")

    # 표 생성 및 스크롤바 연결
    table = ttk.Treeview(table_window, yscrollcommand=table_scrollbar.set)
    table.grid(row=0, column=0)

    table_scrollbar.config(command=table.yview)

def main():
    global root
    root = tk.Tk()
    root.title("글 편집 프로그램")

    # 표 추가 버튼
    add_table_button = ttk.Button(root, text="표 추가", command=add_table)
    add_table_button.pack(padx=20, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
