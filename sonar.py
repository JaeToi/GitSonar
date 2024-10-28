import os

# 1. 불필요한 변수 사용 (사용되지 않는 변수)
unused_variable = 1111111

# 2. 하드코딩된 비밀번호 (보안 이슈)
def login(user, password):
    if password == "1234":  # 하드코딩된 비밀번호
        print(f"Welcome, {user}!")
    else:
        print("Invalid password")

# 3. 예외를 제대로 처리하지 않음 (취약한 에러 처리)
def divide(a, b):
    try:
        return a / b
    except:
        print("Something went wrong!")  # 구체적 예외를 사용하지 않음

# 4. 복잡한 함수 (복잡도 이슈)
def complex_function(x):
    if x > 0:
        if x % 2 == 0:
            print("Positive even number")
        else:
            print("Positive odd number")
    else:
        if x % 2 == 0:
            print("Negative even number")
        else:
            print("Negative odd number")

# 5. 불필요한 파일 읽기 (자원 낭비)
def read_secret_file():
    with open("/etc/passwd", "r") as file:  # 민감한 파일 접근
        print(file.readline())

login("admin", "1234")
divide(10, 0)
complex_function(3)
read_secret_file()