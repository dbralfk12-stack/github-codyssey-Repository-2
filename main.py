import sys
from quiz import QuizGame # 외부 파일(quiz.py)에서 붕어빵 기계(QuizGame) 도면을 가져옴
from helpers import read_int # 입력 검증 책임을 분리한 공통 모듈 호출

def main(): # "이제부터 main이라는 이름의 작업 지시서를 만들 거야!" (프로그램의 시작점)
    game = QuizGame() # 가져온 도면으로 실제 붕어빵 기계를 한 대 설치함 (게임 객체 생성)
    
    while True: # "밑에 있는 일들을 무한히(True) 계속 반복해!" (게임 루프)
        game.print_menu() # 기계에 달린 메뉴판 출력 버튼을 누름
        
        try: # 안전 그물망 (Ctrl+C 방어용)
            # 입력 검증을 helpers.py 모듈로 완벽히 위임 (책임 분리)
            choice = read_int("선택: ", 1, 5)
            
            # 각 메뉴별 기능 호출 (선택한 숫자에 따라 기계의 각 버튼을 누름)
            if choice == 1:
                game.play_quiz()
            elif choice == 2:
                game.add_quiz()
            elif choice == 3:
                game.list_quizzes()
            elif choice == 4:
                game.check_score()
            elif choice == 5:
                print("\n게임을 안전하게 종료합니다. (현재 상태는 state.json에 자동 저장되었으며, 재실행 시 복원됩니다) 안녕히 가세요!")
                break # "이 무한 반복(while) 감옥에서 빠져나가라!" (게임 종료)

        except (KeyboardInterrupt, EOFError):
            # 사용자가 강제로 Ctrl+C를 눌러서 끄거나 EOF 신호를 보낼 때의 대처법
            print("\n\n⚠️ 프로그램이 강제 종료되었습니다. 현재 상태를 저장하고 안전하게 종료합니다.")
            game.save_state() # 강제 종료 직전에도 데이터 유실 방지를 위해 강제 저장
            sys.exit(0) # 프로그램을 완전히 꺼버려라

if __name__ == "__main__": # "만약 이 파일이 다른 곳에 불려간 게 아니라, 직접 실행된 거라면" (시작 주문)
    main() # 위에서 만들어둔 main 작업 지시서를 지금 당장 실행해라!
