def select_sheet(data_frame):
    #사용자의 입력값을 저장할 리스트
    input_list = []
    #엑셀 시트 목록을 저장할 리스트
    sheet_list = []

    # data_frame의 sheet 목록을 sheet_list에 저장합니다.
    for i in data_frame.sheet_names:
        sheet_list.append(i)

    # 사용자가 q! 를 입력할 때까지 input을 받아 리스트에 저장하는 코드 작성해줘.
    while True:
        print("작업할 sheet 이름을 입력한 후 엔터키를 눌러 추가시키세요. 종료하려면 q!를 입력하세요.")
        input_sheet = input("작업할 sheet 이름을 입력하세요: ") # sheet 이름을 입력받습니다.
        if input_sheet == "q!":
            print("사용자가 입력을 완료했습니다.")
            break
        else:
            input_list.append(input_sheet)
            print("추가된 sheet 목록: ", input_list)

    # 사용자가 입력한 sheet 목록을 출력합니다.
    print("선택된 sheet 목록으로 작업합니다.: ", input_list)
    return input_list



    
    
    
