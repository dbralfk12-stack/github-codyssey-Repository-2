# 🎯 나만의 파이썬 퀴즈 게임 (Python Console)

Python 기초 문법과 객체 지향 프로그래밍(클래스 분리), 그리고 JSON을 이용한 파일 입출력을 학습하기 위해 제작된 터미널 기반 대화형 퀴즈 게임입니다.

## 📖 1. 프로젝트 개요
본 프로젝트는 Python 기본 문법만으로 동작하는 콘솔(Terminal) 기반의 퀴즈 프로그램입니다. 
단순한 코드 작성을 넘어 **Git을 활용한 브랜치 전략(Branching Strategy)과 기능 단위 커밋(Commit)** 등 실제 협업 워크플로우를 그대로 적용하여 실습하는 것을 목표로 하였습니다. 사용자의 잘못된 입력(문자 입력, 엔터 등)에 의해 프로그램이 종료되지 않도록 `try-except` 구문을 활용한 예외 처리가 꼼꼼하게 적용되어 있습니다.

## 💡 2. 퀴즈 주제와 선정 이유
* **주제:** 파이썬 및 프로그래밍 상식
* **선정 이유:** 개발 입문 과정에서 배우는 파이썬의 기초 문법(창시자, 리스트 메서드, 자료형의 특징 등)을 퀴즈로 구현함으로써, 게임을 개발하는 동시에 본인의 언어 이해도를 스스로 점검하고 복습할 수 있는 가장 효과적이고 실용적인 주제라고 판단하여 선정했습니다.

## 🚀 3. 실행 방법
**개발 환경:** Python 3.10 이상 (외부 라이브러리 없음)
1. 저장소를 클론(Clone) 받거나 폴더로 이동합니다.
2. 터미널(Git Bash 또는 PowerShell)을 열고 아래 명령어를 입력합니다.
```bash
python main.py
# 윈도우 환경에 따라 py main.py 또는 python3 main.py 를 사용하세요.
```

## ✅ 4. 기능 목록
1. **퀴즈 풀기:**
   - `state.json`에 저장된 퀴즈를 순차적으로 1문제씩 출제합니다.
   - 사용자가 1~4 사이의 번호를 입력하여 정답을 맞힙니다.
   - 모든 문제를 풀면 정답 수와 점수를 계산하여 보여주며, 역대 최고 점수라면 자동으로 기록을 갱신합니다.
2. **퀴즈 추가:**
   - 퀴즈 문제 내용, 4개의 선택지, 정답 번호를 입력받아 실시간으로 새로운 퀴즈 객체를 생성합니다.
   - 추가된 데이터는 즉시 `state.json` 파일에 저장되어 프로그램을 껐다 켜도 유지됩니다.
3. **퀴즈 목록:**
   - 현재 시스템에 등록된 전체 퀴즈의 문항 목록과 총개수를 조회합니다.
4. **점수 확인:**
   - 플레이어가 달성한 역대 최고 득점을 확인합니다.

> **공통 예외 처리:** 모든 입력 구간에서는 빈 값(엔터), 문자열 입력(`abc`), 허용 범위 이탈(`9`) 등에 대해 튕기지 않고 안내 메시지와 함께 재입력을 요구합니다.

## 📁 5. 파일 구조
이 프로젝트는 기능과 책임의 분리를 위해 두 개의 파이썬 파일로 나뉘어져 있습니다.
```text
📦 python-quiz-game
 ┣ 📜 main.py       # 프로그램의 진입점. 게임 루프와 메뉴 선택 입력을 처리함
 ┣ 📜 quiz.py       # 핵심 로직. 개별 퀴즈를 정의하는 Quiz 클래스와 전체 상태를 관리하는 QuizGame 클래스 정의
 ┣ 📜 state.json    # 퀴즈 문제 및 최고 점수를 저장하는 로컬 DB 역할 파일
 ┣ 📜 .gitignore    # 파이썬 캐시 파일 등 깃허브에 올리지 않을 파일 정의
 ┗ 📜 README.md     # 프로젝트 및 실행 안내 문서 (본 파일)
```

## 💾 6. 데이터 파일 설명 (state.json)
프로그램을 종료해도 데이터가 유지(영속성)되도록 프로젝트 루트 경로에 `state.json` 파일을 자동으로 생성하고 관리합니다. 파일이 손상되었거나 삭제된 경우, 프로그램 실행 시 자동으로 감지하여 **기본 파이썬 퀴즈 5문항**으로 데이터를 안전하게 복구합니다. (UTF-8 인코딩)

* **스키마 (Schema) 구조:**
```json
{
    "best_score": 3,
    "quizzes": [
        {
            "question": "파이썬의 창시자는 누구인가요?",
            "choices": [
                "귀도 반 로섬",
                "제임스 고슬링",
                "데니스 리치",
                "리누스 토발즈"
            ],
            "answer": 1
        }
    ]
}
```

---

## 📸 7. 과제 제출용 스크린샷 (학습자 첨부 영역)

### 💻 개발 환경 및 버전
- **Python 버전 확인:** `(터미널에서 python --version 실행 화면)`
- <img width="724" height="90" alt="7" src="https://github.com/user-attachments/assets/6d120a2d-ae7e-4508-b828-efb7c46b00f2" />

- **VS Code 탐색기 뷰:** `(코드 파일들이 열려있는 VS Code 화면)`
- <img width="1912" height="1288" alt="8" src="https://github.com/user-attachments/assets/b7c9c076-9697-4c7e-b00e-ff5d0f5014a8" />

- **Git 커밋 로그:** `(git log --oneline --graph 실행 화면)`
<img width="850" height="1064" alt="6" src="https://github.com/user-attachments/assets/6b094df5-8b85-4c34-b604-a5b6e24b62ab" />

### 🎮 프로그램 실행 결과
- **메뉴 화면:** `(프로그램 초기 구동 화면)`
- <img width="756" height="356" alt="1" src="https://github.com/user-attachments/assets/c8eed5b1-decc-45a0-ab73-d8541fe3801e" />

- **퀴즈 풀기:** `(1번 메뉴 - 문제 풀이 진행 화면)`
  <img width="676" height="362" alt="4" src="https://github.com/user-attachments/assets/27428fb1-9117-435a-9dbe-ec93d384978c" />

- **점수 확인:** `(4번 메뉴 - 100점 및 최고 점수 갱신 화면)`
- ![Uploading 4.png…]()
<img width="740" height="550" alt="5" src="https://github.com/user-attachments/assets/c2f24fc4-df82-4c42-96ae-122fabe24842" />

- **퀴즈 추가:** `(2번 메뉴 - 새로운 퀴즈 입력 화면)`
- <img width="700" height="372" alt="2" src="https://github.com/user-attachments/assets/a7c1b0bd-c15f-43d2-be7c-f823659c3dc4" />

- **퀴즈 목록:** `(3번 메뉴 - 6문제가 모두 출력된 화면)`

- <img width="850" height="490" alt="3" src="https://github.com/user-attachments/assets/26754659-da60-443d-99cb-2f95ee71cf4f" />

