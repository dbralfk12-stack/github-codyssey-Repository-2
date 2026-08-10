import sys
from quiz import QuizGame # 외부 파일(quiz.py)에서 붕어빵 기계(QuizGame) 도면을 가져옴

def main(): # "이제부터 main이라는 이름의 작업 지시서를 만들 거야!" (프로그램의 시작점)
    game = QuizGame() # 가져온 도면으로 실제 붕어빵 기계를 한 대 설치함 (게임 객체 생성)
    
    while True: # "밑에 있는 일들을 무한히(True) 계속 반복해!" (게임 루프)
        game.print_menu() # 기계에 달린 메뉴판 출력 버튼을 누름
        
        try: # "일단 밑에 있는 코드를 시도해봐(try). 에러가 나도 프로그램 끄지 마!" (안전 그물망)
            choice_str = input("선택: ").strip() # 사용자에게 글자를 입력받고 양옆 공백을 쳐냄
            
            # 빈 입력 처리
            if not choice_str: # 만약(if) 입력한 글자가 아무것도 없다면(not)
                print("⚠️ 입력값이 없습니다. 숫자를 입력해주세요.")
                continue # "이번 바퀴는 무효야! 다시 맨 위(while)로 올라가서 메뉴부터 다시 띄워!"
            
            choice = int(choice_str) # 입력받은 글자(str)를 계산 가능한 숫자(int)로 변환해라
            
            # 허용 범위 외 처리
            if choice < 1 or choice > 5: # 만약 숫자가 1보다 작거나(or) 5보다 크다면
                print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
                continue
            
            # 각 메뉴별 기능 호출 (선택한 숫자에 따라 기계의 각 버튼을 누름)
            if choice == 1:
                game.play_quiz()
            elif choice == 2: # 그렇지 않고 만약(elif) 2번을 눌렀다면
                game.add_quiz()
            elif choice == 3:
                game.list_quizzes()
            elif choice == 4:
                game.check_score()
            elif choice == 5:
                print("\n게임을 안전하게 종료합니다. (현재 상태는 state.json에 자동 저장되었으며, 재실행 시 복원됩니다) 안녕히 가세요!")
                break # "이 무한 반복(while) 감옥에서 빠져나가라!" (게임 종료)

        except ValueError: # 만약 위에서 시도(try)하다가 '숫자가 아닌 글자'를 넣어서 에러(ValueError)가 났다면
            print("⚠️ 잘못된 입력입니다. 숫자로만 입력해주세요.") # 튕기는 대신 이 경고창만 띄워라
        except (KeyboardInterrupt, EOFError):
            # 사용자가 강제로 Ctrl+C를 눌러서 끄려고 할 때의 대처법
            print("\n\n⚠️ 프로그램이 강제 종료되었습니다. 안전하게 종료합니다.")
            sys.exit(0) # 프로그램을 완전히 꺼버려라

if __name__ == "__main__": # "만약 이 파일이 다른 곳에 불려간 게 아니라, 직접 실행된 거라면" (시작 주문)
    main() # 위에서 만들어둔 main 작업 지시서를 지금 당장 실행해라!
