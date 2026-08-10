import json # 텍스트(JSON)를 파이썬의 번역기로 바꿔주는 도구 가져오기
import os   # 내 컴퓨터의 파일(폴더) 시스템을 다루는 도구 가져오기
import shutil # 파일 복사를 위한 도구 가져오기
from helpers import read_int, read_nonempty # 입력 검증 모듈 가져오기

class Quiz: # "앞으로 'Quiz'라는 이름의 붕어빵 기계(틀)를 만들 거야!" (퀴즈 문제 1개를 찍어내는 틀)
    def __init__(self, question, choices, answer): # 붕어빵이 처음 만들어질 때 무조건 필요한 3가지 재료
        """
        개별 퀴즈를 표현하는 클래스
        :param question: 문제 (str)
        :param choices: 4개의 선택지 (list)
        :param answer: 정답 번호 1~4 (int)
        """
        self.question = question # 첫 번째 재료: 질문 내용을 붕어빵 안에 채워 넣어라
        self.choices = choices   # 두 번째 재료: 4개의 선택지를 채워 넣어라
        self.answer = answer     # 세 번째 재료: 정답 번호를 채워 넣어라

    def display(self): # 기계(Quiz)에 달린 '화면에 보여주기' 버튼
        """퀴즈 문제와 선택지를 화면에 출력합니다."""
        print(f"\n[문제] {self.question}")
        for i, choice in enumerate(self.choices, 1): # 선택지 4개를 1번부터 순서대로 번호를 매겨서 보여줌
            print(f"{i}. {choice}")
            
    def check_answer(self, user_answer): # 기계에 달린 '정답 맞는지 확인하기' 버튼
        """사용자가 입력한 정답이 맞는지 확인합니다."""
        return self.answer == user_answer # "내가 알고 있는 정답과 네가 쓴 답이 같으면 True(맞음)를 알려줄게!"

class QuizGame: # "이번엔 'QuizGame'이라는 게임 전체를 관리하는 더 큰 붕어빵 기계를 만들 거야!"
    def __init__(self): # 게임 기계가 처음 설치될 때 하는 기본 세팅
        """게임 전체를 관리하는 클래스"""
        self.quizzes = [] # 아직 문제는 없으니 빈 바구니(리스트)를 하나 준비해둬
        self.best_score = 0 # 최고 점수는 일단 0점으로 세팅
        self.state_file = "state.json" # 데이터를 저장할 공책(파일) 이름은 state.json으로 정함
        self.backup_file = "state.json.bak" # 만약을 대비한 백업 공책 이름
        self.load_state() # "기계 설치가 끝나면, 과거에 저장해둔 공책(파일)을 먼저 읽어와라!"
        
    def load_state(self): # '과거 기록 불러오기' 기능
        """state.json 파일에서 데이터를 불러옵니다. 실패 시 백업본, 그 다음엔 기본 데이터를 로드합니다."""
        # 1. 시도할 파일 목록 (원본 -> 백업본 순서)
        for target_file in [self.state_file, self.backup_file]:
            if not os.path.exists(target_file):
                continue
                
            try:
                with open(target_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                self.best_score = data.get("best_score", 0)
                
                quiz_data_list = data.get("quizzes", [])
                self.quizzes = []
                for q_data in quiz_data_list:
                    quiz = Quiz(q_data["question"], q_data["choices"], q_data["answer"])
                    self.quizzes.append(quiz)
                    
                print(f"📂 {target_file}에서 데이터를 성공적으로 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score}점)")
                return # 성공했으니 멈추고 돌아가!
                
            except (json.JSONDecodeError, KeyError, Exception):
                print(f"⚠️ {target_file} 파일이 손상되었습니다. 다음 복구 단계를 시도합니다.")
                
        # 2. 원본과 백업본이 모두 없거나 망가졌을 때 (최후의 보루)
        print("⚠️ 읽을 수 있는 저장 데이터가 없어 기본 퀴즈로 복구합니다.")
        self.quizzes = []
        self.best_score = 0
        self.load_default_quizzes()

    def save_state(self): # '현재 기록을 공책에 쓰기' 기능
        """현재 퀴즈 목록과 최고 점수를 state.json에 저장합니다."""
        data = { # 공책에 적을 내용물(딕셔너리)을 예쁘게 정리함
            "best_score": self.best_score,
            "quizzes": []
        }
        
        for quiz in self.quizzes: # 내 바구니에 있는 붕어빵들을 하나씩 꺼내서
            data["quizzes"].append({ # 글자(JSON)로 바꾸기 쉽게 딕셔너리 형태로 포장함
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer
            })
            
        try: # "포장한 걸 공책(파일)에 쓰려고 시도해봐(try)"
            # 쓰기 전에 기존 정상 파일이 있다면 백업본으로 복사해둠 (백업 훅)
            if os.path.exists(self.state_file):
                shutil.copy2(self.state_file, self.backup_file)
                
            with open(self.state_file, 'w', encoding='utf-8') as f: # 쓰기 모드('w')로 공책을 엶 (기존 내용 덮어씀)
                json.dump(data, f, ensure_ascii=False, indent=4) # 예쁜 포맷(indent=4)으로 파일에 씀
            print("💾 (System) 변경된 데이터가 성공적으로 저장되었습니다.")
        except Exception as e: # 만약 디스크 꽉 참 등으로 에러가 나면
            print(f"⚠️ (System) 데이터 저장 중 오류가 발생했습니다. 권한이나 디스크 용량을 확인하세요: {e}")
        
    def load_default_quizzes(self): # '기본 문제 채워넣기' 기능
        """기본 파이썬 상식 퀴즈 5개를 메모리에 로드합니다."""
        self.quizzes = [ # 바구니에 Quiz 붕어빵 5개를 쾅쾅쾅쾅쾅 찍어냄
            Quiz("파이썬의 창시자는 누구인가요?", ["귀도 반 로섬", "제임스 고슬링", "데니스 리치", "리누스 토발즈"], 1),
            Quiz("파이썬에서 리스트 맨 끝에 요소를 추가할 때 사용하는 메서드는?", ["add()", "insert()", "append()", "push()"], 3),
            Quiz("파이썬의 데이터 타입 중 값이 변하지 않는(Immutable) 자료형은?", ["list", "dict", "set", "tuple"], 4),
            Quiz("다음 중 파이썬에 존재하지 않는 반복문은?", ["for", "while", "do-while", "모두 존재한다"], 3),
            Quiz("파이썬에서 예외(에러)를 처리하기 위해 사용하는 기본 구문은?", ["try-except", "catch-throw", "if-else", "switch-case"], 1)
        ]
        
    def play_quiz(self): # '퀴즈 풀기' 게임 시작!
        """퀴즈 풀기 기능을 수행합니다."""
        if not self.quizzes: # 만약 바구니가 비어있다면
            print("\n⚠️ 등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해주세요.")
            return # 게임 그만하고 돌아가!
            
        print(f"\n📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)\n" + "-"*40)
        
        score = 0 # 내 점수는 0점에서 시작
        for idx, quiz in enumerate(self.quizzes, 1): # 바구니에서 문제를 하나씩 순서대로 꺼내옴
            quiz.display() # 꺼내온 붕어빵(퀴즈)의 '화면에 보여주기' 기능 실행
            
            # helpers 모듈을 사용하여 1~4 사이의 숫자만 안전하게 받음 (책임 분리)
            answer_num = read_int("\n정답 입력 (1-4): ", 1, 4)
            
            if quiz.check_answer(answer_num): # "내가 입력한 번호가 정답인지 확인해줘!"
                print("✅ 정답입니다!")
                score += 1 # 점수 1점 획득!
            else:
                print(f"❌ 오답입니다! (정답: {quiz.answer}번)")
            
            print("-" * 40)
                    
        print("\n" + "="*40)
        print(f"🏆 결과: {len(self.quizzes)}문제 중 {score}문제 정답! ({(score/len(self.quizzes))*100:.0f}점)")
        
        if score > self.best_score: # 만약 방금 얻은 점수가 내 최고 점수보다 높다면
            print("🎉 새로운 최고 점수입니다!")
            self.best_score = score # 내 최고 점수를 갱신해라!
            self.save_state() # "기록이 바뀌었으니 당장 공책(state.json)에 새로 적어둬라!"
        print("="*40)
        
    def add_quiz(self): # '새로운 퀴즈 문제 만들기' 기능
        """새로운 퀴즈를 입력받고 목록에 추가합니다."""
        print("\n📌 새로운 퀴즈를 추가합니다.")
        
        # helpers 모듈을 사용하여 빈 값 입력을 철저히 차단
        question = read_nonempty("\n문제를 입력하세요: ")
            
        choices = []
        for i in range(1, 5): # 1번부터 4번까지 4번 반복해서 선택지를 물어봄
            choice = read_nonempty(f"선택지 {i}: ")
            choices.append(choice) # 물어본 선택지를 빈 바구니(choices)에 차곡차곡 담음
            
        # helpers 모듈을 사용하여 1~4 사이의 숫자만 엄격하게 받음
        answer = read_int("정답 번호 (1-4): ", 1, 4)
                
        # 사용자가 입력한 재료들로 새로운 Quiz 붕어빵을 하나 찍어냄
        new_quiz = Quiz(question, choices, answer) 
        self.quizzes.append(new_quiz) # 찍어낸 새 붕어빵을 내 퀴즈 바구니에 담음
        self.save_state() # "새 퀴즈가 생겼으니 공책(state.json)에 적어둬라!"
        print("\n✅ 퀴즈가 성공적으로 추가되었습니다!")

    def list_quizzes(self): # '퀴즈 목록 보기' 기능
        """저장된 퀴즈 목록을 출력합니다."""
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다.")
            return
            
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)\n" + "-"*40)
        for idx, quiz in enumerate(self.quizzes, 1):
            print(f"[{idx}] {quiz.question}")
        print("-" * 40)

    def check_score(self): # '최고 점수 확인하기' 기능
        """저장된 최고 점수를 확인합니다."""
        print("\n" + "="*40)
        if self.best_score > 0:
            print(f"🏆 현재 최고 점수: {self.best_score}점")
        else:
            print("아직 기록된 점수가 없습니다. 퀴즈를 풀어보세요!")
        print("="*40)

    def print_menu(self): # '화면에 메뉴판 띄우기' 기능
        """메뉴 화면을 출력합니다."""
        print("\n" + "="*40)
        print("        🎯 나만의 퀴즈 게임 🎯")
        print("="*40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("="*40)
