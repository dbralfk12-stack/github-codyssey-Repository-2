# 사용자 입력을 받고 검증하는 공통 로직 모듈
# "입력 처리(검증)" 로직을 분리한 핵심 근거 파일입니다.

def read_int(prompt, min_val, max_val):
    """
    사용자로부터 숫자를 입력받고, 유효한 범위인지 검증합니다.
    (빈 값, 문자, 범위 초과 에러를 자체적으로 방어합니다)
    """
    while True:
        raw_input = input(prompt).strip() # 앞뒤 공백 제거
        
        # 1. 빈 값 방어
        if not raw_input:
            print(f"⚠️ 입력값이 없습니다. {min_val}-{max_val} 사이의 숫자를 입력해주세요.")
            continue
            
        try:
            # 2. 숫자 변환 시도
            value = int(raw_input)
            
            # 3. 범위 검사
            if not min_val <= value <= max_val:
                print(f"⚠️ 범위를 벗어났습니다. {min_val}-{max_val} 사이의 숫자를 입력해주세요.")
                continue
                
            return value # 모든 검증을 통과한 깨끗한 숫자만 반환!
            
        except ValueError:
            print("⚠️ 숫자가 아닙니다. 숫자로만 입력해주세요.")


def read_nonempty(prompt):
    """
    사용자로부터 텍스트를 입력받되, 빈 값 입력을 차단합니다.
    """
    while True:
        value = input(prompt).strip()
        if not value:
            print("⚠️ 내용을 입력해주세요. (빈칸 불가능)")
            continue
        return value
