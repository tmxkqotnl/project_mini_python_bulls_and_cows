# 랭킹을 저장 여부

def input_rank() :
    while True:
        res = input("랭킹을 저장하시겠습니까? yes or no ")

        if res == 'yes' :
            print("랭크 DB에 추가되었습니다")
            #게임결과를 DB에 넣는 함수나 작업을 동훈님이 해주실거야
            break
        elif res =='no' :
            print("okay goodbye")
            break
        else :
            print("yes or no 중에 입력하세요")

input_rank()

