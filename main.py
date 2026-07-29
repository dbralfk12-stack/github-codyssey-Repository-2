import sys
from quiz import QuizGame

def main():
    game = QuizGame()
    
    while True:
        game.print_menu()
        
        try:
            choice_str = input("선택: ").strip()
            
            # 빈 입력 처리
            if not choice_str:
                print("⚠️ 입력값이 없습니다. 숫자를 입력해주세요.")
                continue
            
            choice = int(choice_str)
            
            # 허용 범위 외 처리
            if choice < 1 or choice > 5:
                print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
                continue
            
            # 각 메뉴별 기능 호출
            if choice == 1:
                game.play_quiz()
            elif choice == 2:
                game.add_quiz()
            elif choice == 3:
                game.list_quizzes()
            elif choice == 4:
                print("\n[점수 확인 기능을 곧 구현합니다.]")
            elif choice == 5:
                print("\n게임을 안전하게 종료합니다. 안녕히 가세요!")
                break

        except ValueError:
            print("⚠️ 잘못된 입력입니다. 숫자로만 입력해주세요.")
        except (KeyboardInterrupt, EOFError):
            # Ctrl+C 등 비정상 종료 시 처리
            print("\n\n⚠️ 프로그램이 강제 종료되었습니다. 안전하게 종료합니다.")
            sys.exit(0)

if __name__ == "__main__":
    main()
