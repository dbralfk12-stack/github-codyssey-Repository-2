# Python Console 퀴즈 게임: 객체 지향과 데이터 영속성 실습

Python 기초 문법, 객체 지향 프로그래밍(OOP), JSON 파일 입출력 학습을 위해 구현된 터미널 기반 대화형 퀴즈 게임 프로젝트입니다. 코드의 단순 구현을 넘어, 기술 도입 근거와 예외 처리에 중점을 두고 설계되었습니다.

## 프로젝트 개요
* **목표:** Python 객체지향 설계(클래스) 및 JSON을 활용한 데이터 영속성 구현
* **환경:** Python 3.10 이상 (외부 라이브러리 없음)
* **주요 기술:** Python(OOP), JSON, Git Branch 전략
* **기간:** 2026년 8월

## 핵심 기술 스택 및 도입 근거

**1. 객체 지향(OOP) 설계 및 클래스 분리**
단일 모듈로 구성될 경우 발생할 수 있는 유지보수 한계를 극복하기 위해, 역할과 책임에 따라 클래스를 분리하여 설계했습니다.
* **Quiz 클래스:** 개별 문제에 대한 내용, 선택지, 정답 번호를 관리하는 데이터 객체입니다.
  ```python
  class Quiz:
      def __init__(self, question, choices, answer):
          self.question = question
          self.choices = choices
          self.answer = answer
  ```
* **QuizGame 클래스:** 문제 출제, 점수 계산, 데이터 입출력 등 핵심 비즈니스 로직을 담당합니다.
  ```python
  class QuizGame:
      def __init__(self):
          self.quizzes = []
          self.best_score = 0
          self.state_file = "state.json"
          self.load_state()
          
      def play_quiz(self):
          # 퀴즈 진행 및 점수 계산 로직
          ...
  ```
* **main.py:** 사용자 입력 처리 및 터미널 UI 렌더링을 담당하는 엔트리 포인트입니다.
  ```python
  def main():
      game = QuizGame()
      while True:
          game.print_menu()
          choice = input("선택: ")
          # 입력값에 따른 QuizGame 메서드 호출 (UI와 로직의 분리)
          ...
  ```
* **도입 효과:** 향후 터미널 기반 UI에서 웹 또는 모바일 환경으로 확장 시, 핵심 로직(`QuizGame`)의 수정 없이 `main.py`만 교체하여 유연한 대응이 가능합니다.

> [!TIP]
> **💡 객체 지향 프로그래밍(OOP) 핵심 개념 요약**
> 클래스(Class)는 데이터(속성)와 기능(메서드)을 하나로 묶어놓은 '설계도(Blueprint)'이며, 객체(Object)는 이 설계도를 바탕으로 메모리에 실체화된(Instantiated) 개별 단위를 의미합니다. 위 코드에서 `Quiz` 클래스는 퀴즈 데이터의 구조를 정의하는 '설계도'이고, `QuizGame` 클래스는 데이터들을 조작하고 게임 흐름을 제어하는 '컨트롤러(Controller)' 역할을 수행합니다. 보다 깊이 있는 객체 지향의 4대 원칙(캡슐화, 상속, 다형성, 추상화)을 이해하고 싶다면 아래 **개발자 기술 블로그**를 참고해 보세요!
> 
> 📚 **추천 기술 블로그 (Velog):**
> - [파이썬 객체지향(OOP) 기초부터 심화까지 - Velog](https://velog.io/search?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC%20%EA%B0%9D%EC%B2%B4%EC%A7%80%ED%96%A5) (선배 개발자들의 쉬운 비유와 실무 예제 총집합)
> - 단순히 코드를 길게 나열하는 것(절차지향)과, 역할별로 파일을 쪼개서 관리하는 것(객체지향)의 유지보수성 차이를 중심으로 읽어보시길 강력히 권장합니다.
**2. 데이터 영속성 유지를 위한 JSON 채택**
프로그램 종료 시에도 사용자 데이터(퀴즈 목록, 최고 점수)가 보존되도록 파일 시스템을 활용한 데이터 영속성을 구현했습니다. 여러 포맷 중 JSON을 선택한 이유는 파이썬의 `Dictionary` 자료구조와 1:1 매핑이 가능하여 **직렬화(Serialization)** 및 **역직렬화(Deserialization)** 과정이 매우 효율적이고 직관적이기 때문입니다.

**데이터 변환 (직렬화/역직렬화) 개념 정리:**
컴퓨터 메모리(RAM)에 있는 파이썬 객체를 하드디스크에 텍스트 파일로 저장하거나, 반대로 텍스트 파일을 읽어 파이썬 객체로 되돌리는 과정을 의미합니다.

| 용어 | 방향 | 개념 설명 | 본 프로젝트 적용 사례 (`quiz.py`) |
|---|---|---|---|
| **직렬화 (Serialization)** | 파이썬 딕셔너리 ➡️ JSON 파일 | 메모리의 데이터를 통신이나 저장이 쉬운 '연속된 텍스트(JSON)'로 변환하는 과정 | 새로운 퀴즈나 점수 갱신 시 `json.dump()`를 이용해 `state.json` 파일에 쓰기(Write) |
| **역직렬화 (Deserialization)** | JSON 파일 ➡️ 파이썬 딕셔너리 | 텍스트로 저장된 JSON 데이터를 프로그램이 다룰 수 있는 파이썬 객체(딕셔너리)로 복원하는 과정 | 프로그램 시작 시 `json.load()`를 이용해 `state.json` 파일을 읽어오기(Read) |
| **1:1 매핑** | 구조의 완벽한 일치 | 파이썬의 `{키: 값}` 구조가 JSON 포맷과 완벽히 일치하여, 개발자가 별도의 데이터 가공(파싱)을 할 필요가 없음 | `{"best_score": 100}` 형태가 파이썬 변수와 JSON 파일 양쪽에서 동일한 형태로 다뤄짐 |

> [!TIP]
> **💡 `Dictionary`와 `JSON` 개념이 헷갈리시나요?**
> 파이썬의 딕셔너리(Dictionary)는 `{키: 값}` 형태로 데이터를 효율적으로 묶고 관리하는 핵심 자료구조입니다. 이 파이썬의 딕셔너리 구조를 텍스트 파일로 고스란히 옮겨놓은 포맷이 바로 JSON입니다. 완벽한 이해를 위해 아래 **유튜브 무료 강의** 시청을 권장합니다.
> 
> 📺 **추천 유튜브 강의:**
> - [나도코딩 파이썬 기초 (사전/Dictionary 파트)](https://youtu.be/kWiCuklohdY) (초보자 맞춤 기초 문법 설명)
> - 영상을 보시며 코드를 직접 타이핑해 보고, 키(Key)와 값(Value)이 어떻게 쌍으로 연결되는지 실습해 보세요!

**3. 예외 처리를 통한 프로그램 안정성 확보**
사용자로부터 예상치 못한 입력(문자열, 범위 외 값 등)이 주어지더라도 프로그램이 강제 종료(Crash)되지 않도록 `try-except` 구문을 활용하여 방어 코드를 작성했습니다.

> [!TIP]
> **💡 `try-except` 예외 처리 개념이 처음이신가요?**
> 예외 처리는 에러가 발생할 가능성이 있는 코드를 `try` 블록에 넣고, 에러 발생 시 프로그램 종료 대신 우회할 코드를 `except`에 작성하는 기법입니다. 완벽한 이해를 위해 아래 **유튜브 무료 강의** 시청을 강력히 권장합니다.
> 
> 📺 **추천 유튜브 강의:**
> - [나도코딩 파이썬 기초 (예외 처리 파트)](https://youtu.be/kWiCuklohdY) (초보자에게 가장 직관적이고 친절한 설명)
> - 눈으로만 보지 말고, 직접 에러(ZeroDivisionError 등)를 내보고 프로그램이 죽지 않고 살아남는 과정을 영상과 함께 실습해 보세요!

## 수행 체크리스트
- [x] 터미널 기본 입출력 구현
- [x] 클래스(Quiz, QuizGame) 기반 객체지향 설계
- [x] JSON 파일 입출력을 통한 데이터 영속성 유지
- [x] 예외 처리(try-except)를 통한 비정상 종료 방지
- [x] 파일 손상 시 자동 복구 로직 구현
- [x] Git 브랜치 전략을 통한 기능 단위 개발 및 병합

## 디렉토리 구조 및 파일 역할
```text
python-quiz-game/
├── main.py       # 프로그램의 진입점. 메뉴 선택 입력을 처리함 (UI)
├── quiz.py       # 개별 퀴즈를 정의하는 Quiz 클래스 & 상태를 관리하는 QuizGame 클래스 (Logic)
├── state.json    # 퀴즈 문제 및 최고 점수를 저장하는 로컬 DB 역할 파일 (Data)
├── .gitignore    # 파이썬 캐시 파일 등 깃허브에 올리지 않을 파일 정의
└── README.md     # 실습 수행 과정 및 결과를 기록한 기술 문서 (본 파일)
```

### 디렉토리 구조 설계 과정 및 시행착오 (Troubleshooting)

**1. UI와 비즈니스 로직의 분리 (`main.py` vs `quiz.py`)**
* **초기 문제점 (시행착오):** 개발 초기에는 `main.py` 파일 하나에 사용자 입력 처리(UI), 퀴즈 점수 계산(비즈니스 로직), 파일 저장(I/O) 코드를 모두 혼재하여 작성했습니다. 그 결과 코드가 길어지면서 단순한 안내 문구 하나를 수정하려 해도 핵심 점수 계산 로직까지 건드려야 하는 '스파게티 코드' 문제가 발생했습니다.
* **해결책 및 의도:** 이를 해결하기 위해 사용자와 맞닿아 있는 '안내데스크(UI)' 역할은 `main.py`에 남겨두고, 실제 퀴즈를 운영하고 데이터를 처리하는 '핵심 비즈니스 로직'은 `quiz.py`로 완전히 분리했습니다. 각 파일이 단 하나의 책임만 지게 됨으로써(단일 책임 원칙), 향후 코드 수정 시 발생할 수 있는 부작용(Side Effect)을 원천 차단할 수 있었습니다.

**2. 코드와 데이터 자원의 격리 (`state.json`)**
* **초기 문제점 (시행착오):** 초기 버전에서는 파이썬 코드(`quiz.py`) 내부에 리스트 형태로 퀴즈 데이터를 직접 하드코딩(Hardcoding) 해두었습니다. 하지만 이 방식은 사용자가 퀴즈를 직접 추가할 수 없고, 새로운 문제를 기본값으로 추가하려면 개발자가 직접 파이썬 소스 코드를 열어 수정해야만 하는 치명적인 단점이 있었습니다.
* **해결책 및 의도:** 퀴즈 데이터를 파이썬 소스 코드에서 완전히 분리하여 `state.json`이라는 독립적인 데이터 파일로 격리했습니다. 이를 통해 파이썬 코드를 전혀 모르는 비전공자도 JSON 파일만 열어 직관적으로 문제를 추가 및 수정할 수 있게 되었습니다. 또한 데이터가 손상되더라도 소스 코드를 건드릴 필요 없이 `state.json` 파일만 삭제(초기화)하면 되는 유지보수의 편리함을 확보했습니다.

## 구축 및 실행 과정

### 0. 초기 환경 설정 및 한글 인코딩 시행착오
**사전 준비 및 Python 실행 점검:**
본 프로젝트는 외부 라이브러리 없이 순수 파이썬(Vanilla Python) 모듈만으로 작성되었습니다. 터미널(CLI) 환경에서 `python` 명령어를 통해 프로그램이 정상적으로 동작하는지 확인해야 합니다.

**과정 및 시행착오 (Windows 환경의 한글 깨짐 현상):** 
개발 초기, 퀴즈 데이터를 `state.json` 파일에 읽고 쓰는 과정에서 퀴즈 문제나 선택지의 한글 텍스트가 알 수 없는 특수문자로 깨지거나(Mojibake), `UnicodeDecodeError`가 발생하는 문제를 겪었습니다. 원인을 분석해 보니, Windows 운영체제는 기본 텍스트 인코딩으로 `cp949`를 사용하는 반면 JSON 표준 포맷은 `utf-8`을 사용하기 때문에 발생하는 충돌이었습니다. 
이를 해결하기 위해 파이썬의 `open()` 함수에 `encoding='utf-8'` 옵션을 명시적으로 추가하였고, 결과적으로 Windows뿐만 아니라 Mac/Linux 등 어떤 OS에서도 한글 데이터가 안전하고 동일하게 입출력되도록 개선할 수 있었습니다.

**인코딩이 적용된 데이터 입출력 방어 코드 예시:**
```python
# 단순히 open()을 쓰지 않고, utf-8 인코딩을 강제하여 한글 깨짐 원천 차단
with open(self.state_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
```

### 기본 실행 명령어
| 명령어 | 기능 설명 |
|---|---|
| `python main.py` | 파이썬 프로그램을 실행합니다. (Mac/Linux 환경은 `python3 main.py` 사용) |
| `Ctrl + C` | 실행 중인 프로그램을 강제로 종료합니다. |

### 1. 프로그램 실행 및 예외 처리 검증
**개발 과정 및 개선 사항:** 초기 구현에서는 사용자가 숫자 대신 문자를 입력할 경우 시스템 에러가 발생하며 종료되는 문제가 있었습니다. 이를 개선하기 위해 입력값 검증 로직에 `ValueError` 예외 처리를 추가하여 재입력을 유도하도록 수정했습니다.

**실행 명령어:**
```bash
$ python main.py
```
**강제 종료 안전성 테스트:** 사용자가 `Ctrl+C` 입력으로 프로세스 강제 종료를 시도할 경우, `KeyboardInterrupt`를 처리하여 안내 메시지와 함께 프로세스가 안전하게(Graceful) 종료되도록 구현했습니다.

### 2. 데이터 영속성 및 복구 검증 (JSON)
**데이터 저장 방식의 근거:** 
일반적인 변수나 리스트에 저장된 데이터는 RAM(메모리)에 적재되므로 프로그램 종료와 동시에 모두 휘발됩니다. 이를 방지하고 사용자 경험을 지속시키기 위해, 새로운 퀴즈가 추가되거나 최고 점수가 갱신될 때마다 즉시 하드디스크의 `state.json` 파일에 데이터를 기록하는 방식을 채택했습니다. 이를 통해 프로그램을 재시작하더라도 이전 상태를 완벽하게 복원(영속성 보장)할 수 있습니다.

**자동 복구 로직 (Fail-safe) 설계 이유 및 구현 로직:** 
외부 파일 입출력(I/O) 과정은 런타임 환경에서 가장 변수가 많은 작업입니다. 사용자가 실수로 `state.json` 파일을 삭제하여 프로그램이 파일을 찾지 못하게 되거나(`FileNotFoundError`), 메모장으로 파일을 직접 편집하다가 쉼표(,)나 괄호 하나를 빠뜨려 JSON 포맷이 완전히 깨지는 경우(`json.JSONDecodeError`)가 언제든 발생할 수 있습니다. 

이러한 경우 일반적인 프로그램은 데이터를 읽어오는 초기 단계에서 치명적 에러(Crash)를 일으키며 뻗어버립니다. 이를 방지하기 위해 파일 로드 과정 전체를 `try-except` 블록으로 감싸는 방어막을 구축했습니다. 에러가 감지되면 즉시 사용자에게 복구 안내 메시지를 띄우고, 프로그램 내부에 미리 준비된 '기본 파이썬 상식 5문제'를 메모리에 강제 적재하여 **무중단 서비스(Zero-downtime)**를 제공하도록 설계했습니다.

> **💡 무중단 서비스(Zero-downtime)란?**
> 프로그램에 심각한 내부 오류가 발생하거나 파일이 손상된 상황에서도, 사용자는 어떠한 멈춤이나 에러 강제 종료(Crash)를 겪지 않고 서비스를 계속 이용할 수 있도록 보장하는 설계 기법입니다. 본 프로젝트에서는 핵심 데이터 파일(`state.json`)이 완전히 삭제되거나 훼손되더라도 프로그램이 죽지 않고 즉시 기본 제공 퀴즈로 전환되어, 사용자가 끊김 없이 게임을 즐길 수 있도록 구현했습니다.

**예외 처리가 적용된 파일 로드 방어 코드 (`quiz.py` 발췌):**
```python
def load_state(self):
    # 1. 파일이 아예 존재하지 않는 경우 (삭제됨 등) 방어
    if not os.path.exists(self.state_file):
        print("📂 저장된 데이터가 없습니다. 기본 퀴즈 데이터를 불러옵니다.")
        self.load_default_quizzes()
        return

    try:
        # 2. 파일은 존재하나 데이터가 깨진 경우 로드 시도
        with open(self.state_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # (...정상 데이터 처리 로직...)
            
    except (json.JSONDecodeError, KeyError, Exception):
        # 3. JSON 파싱 에러 발생 시 프로그램 튕김을 막고 자동 초기화
        print("⚠️ 데이터 파일이 손상되었습니다. 기본 데이터로 복구합니다.")
        self.quizzes = []
        self.load_default_quizzes()
```

### 3. Git 브랜치 운영 전략
**브랜치 분리 및 운영의 기술적 근거:**
단일 `main` 브랜치에 모든 코드를 직접 커밋(Commit)하는 방식은 코드 꼬임 현상이나 치명적인 버그를 유발하여 전체 시스템의 안정성을 위협할 수 있습니다. 이를 미연에 방지하기 위해 철저한 브랜치 격리 전략을 도입했습니다.
* **격리된 작업 환경 (`feature` 브랜치):** 새로운 기능 개발이나 로직 수정 시 반드시 `feature` 브랜치를 파생시켜 작업합니다. 이곳은 원본 코드에 영향을 주지 않는 독립된 샌드박스(Sandbox) 역할을 하므로, 자유롭고 안전한 코드 실험이 가능합니다.
* **서비스 안정성 보장 (`main` 브랜치):** `feature` 브랜치에서 개발 및 테스트가 100% 완료된 검증된 코드만을 `main` 브랜치에 병합(Merge)합니다. 이 원칙을 통해 `main` 브랜치는 언제 실행해도 에러 없이 구동되는 무결점 릴리즈(Release) 버전을 상시 유지하게 됩니다.

**원격 푸시(Push) 커밋 증거:**
```bash
$ git push origin main
Enumerating objects: 20, done.
Counting objects: 100% (20/20), done.
Delta compression using up to 8 threads
Compressing objects: 100% (15/15), done.
Writing objects: 100% (20/20), 8.12 KiB | 4.06 MiB/s, done.
Total 20 (delta 5), reused 0 (delta 0), pack-reused 0
To https://github.com/dbralfk12-stack/github-codyssey-Repository-2.git
 * [new branch]      main -> main
```

## 과제 제출용 실행 화면 캡처

### 개발 환경 및 버전 확인
- <img width="724" height="90" alt="7" src="https://github.com/user-attachments/assets/6d120a2d-ae7e-4508-b828-efb7c46b00f2" />

### 프로그램 실행 결과
- **메뉴 화면:** `(프로그램 초기 구동 화면)`
- <img width="756" height="356" alt="1" src="https://github.com/user-attachments/assets/c8eed5b1-decc-45a0-ab73-d8541fe3801e" />
- **퀴즈 풀기:** `(1번 메뉴 - 문제 풀이 진행 화면)`
  <img width="676" height="362" alt="4" src="https://github.com/user-attachments/assets/27428fb1-9117-435a-9dbe-ec93d384978c" />
- **점수 확인:** `(4번 메뉴 - 100점 및 최고 점수 갱신 화면)`
- <img width="740" height="550" alt="5" src="https://github.com/user-attachments/assets/c2f24fc4-df82-4c42-96ae-122fabe24842" />
- **퀴즈 추가:** `(2번 메뉴 - 새로운 퀴즈 입력 화면)`
- <img width="700" height="372" alt="2" src="https://github.com/user-attachments/assets/a7c1b0bd-c15f-43d2-be7c-f823659c3dc4" />
- **퀴즈 목록:** `(3번 메뉴 - 6문제가 모두 출력된 화면)`
- <img width="850" height="490" alt="3" src="https://github.com/user-attachments/assets/26754659-da60-443d-99cb-2f95ee71cf4f" />
- **Git 커밋 로그:** `(git log --oneline --graph 실행 화면)`
- <img width="850" height="1064" alt="6" src="https://github.com/user-attachments/assets/6b094df5-8b85-4c34-b604-a5b6e24b62ab" />
