import json
import os

class Quiz:
    def __init__(self, question, choices, answer):
        """
        개별 퀴즈를 표현하는 클래스
        :param question: 문제 (str)
        :param choices: 4개의 선택지 (list)
        :param answer: 정답 번호 1~4 (int)
        """
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        """퀴즈 문제와 선택지를 화면에 출력합니다."""
        print(f"\n[문제] {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")
            
    def check_answer(self, user_answer):
        """사용자가 입력한 정답이 맞는지 확인합니다."""
        return self.answer == user_answer

class QuizGame:
    def __init__(self):
        """게임 전체를 관리하는 클래스"""
        self.quizzes = []
        self.best_score = 0
        self.state_file = "state.json"
        self.load_state()
        
    def load_state(self):
        """state.json 파일에서 데이터를 불러옵니다. 실패 시 기본 데이터를 로드합니다."""
        if not os.path.exists(self.state_file):
            print("📂 저장된 데이터가 없습니다. 기본 퀴즈 데이터를 불러옵니다.")
            self.load_default_quizzes()
            return

        try:
            with open(self.state_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            self.best_score = data.get("best_score", 0)
            
            # JSON 딕셔너리를 다시 Quiz 객체 리스트로 변환
            quiz_data_list = data.get("quizzes", [])
            for q_data in quiz_data_list:
                quiz = Quiz(q_data["question"], q_data["choices"], q_data["answer"])
                self.quizzes.append(quiz)
                
            print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score}점)")
            
        except (json.JSONDecodeError, KeyError, Exception):
            print("⚠️ 데이터 파일이 손상되었습니다. 기본 데이터로 복구합니다.")
            self.quizzes = []
            self.best_score = 0
            self.load_default_quizzes()

    def save_state(self):
        """현재 퀴즈 목록과 최고 점수를 state.json에 저장합니다."""
        data = {
            "best_score": self.best_score,
            "quizzes": []
        }
        
        # Quiz 객체 리스트를 JSON 직렬화 가능한 딕셔너리로 변환
        for quiz in self.quizzes:
            data["quizzes"].append({
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer
            })
            
        try:
            with open(self.state_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"⚠️ 데이터 저장 중 오류가 발생했습니다: {e}")
        
    def load_default_quizzes(self):
        """기본 파이썬 상식 퀴즈 5개를 메모리에 로드합니다."""
        self.quizzes = [
            Quiz("파이썬의 창시자는 누구인가요?", ["귀도 반 로섬", "제임스 고슬링", "데니스 리치", "리누스 토발즈"], 1),
            Quiz("파이썬에서 리스트 맨 끝에 요소를 추가할 때 사용하는 메서드는?", ["add()", "insert()", "append()", "push()"], 3),
            Quiz("파이썬의 데이터 타입 중 값이 변하지 않는(Immutable) 자료형은?", ["list", "dict", "set", "tuple"], 4),
            Quiz("다음 중 파이썬에 존재하지 않는 반복문은?", ["for", "while", "do-while", "모두 존재한다"], 3),
            Quiz("파이썬에서 예외(에러)를 처리하기 위해 사용하는 기본 구문은?", ["try-except", "catch-throw", "if-else", "switch-case"], 1)
        ]
        
    def print_menu(self):
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
