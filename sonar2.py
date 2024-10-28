# 1. 전역 변수 남용 (전역 변수 사용 지양)
counter = 0  # 전역 변수 사용

def increment():
    global counter  # 전역 변수 수정
    counter += 1

# 2. 불필요한 반복문 (비효율적인 코드)
def find_even_numbers(nums):
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    return result

# 3. 중복 코드 (중복 제거 권장)
def calculate_area_square(side):
    return side * side

def calculate_area_rectangle(width, height):
    return width * height

# 4. 리소스 누수 (파일 닫기 누락)
def write_to_file(data):
    f = open("output.txt", "w")  # 파일을 명시적으로 닫지 않음
    f.write(data)

# 5. deprecated 함수 사용 (비권장된 API 사용)
import imp  # Python 3에서는 deprecated된 모듈

def import_module(module_name):
    return imp.load_module(module_name, *imp.find_module(module_name))

# 함수 실행
increment()
print(f"Counter: {counter}")

print(find_even_numbers([1, 2, 3, 4, 5, 6]))
print(calculate_area_square(5))
print(calculate_area_rectangle(4, 7))
write_to_file("Hello, SonarQube!")
import_module("os")