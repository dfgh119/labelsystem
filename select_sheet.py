def select_sheet(data_frame):
    #사용자의 입력값을 저장할 리스트
    input_list = []
    #엑셀 시트 목록을 저장할 리스트
    sheet_list = []
    # data_frame의 sheet 목록을 sheet_list에 저장합니다.
    for i in data_frame.sheet_names:
        sheet_list.append(i)
    count_x = 0
    for i in sheet_list:
        print("엑셀의 작업시트 목록입니다.", count_x, i)
        count_x += 1

    # 숫자 번호로 시트 선택가능
    while True:
            print("작업할 sheet 번호를 입력하세요 (종료하려면 0을 입력하세요):")
            try:
                selected_index = int(input("작업할 sheet 번호를 입력하세요: "))
                if selected_index == 0:
                    print("사용자가 입력을 완료했습니다.")
                    break
                elif 1 <= selected_index <= len(sheet_list):
                    selected_sheet_name = sheet_list[selected_index - 1]
                    if selected_sheet_name in input_list:
                        print("이미 추가된 sheet입니다. 다시 입력하세요.")
                        continue
                    input_list.append(selected_sheet_name)
                    print(f"{selected_sheet_name} sheet가 추가되었습니다.")
                else:
                    print("올바른 번호를 입력하세요.")
            except ValueError:
                print("올바른 숫자를 입력하세요.")


    # 사용자가 입력한 sheet 목록을 출력합니다.
    print("선택된 sheet 목록으로 작업합니다.: ", input_list)

    return input_list



        
        
        
