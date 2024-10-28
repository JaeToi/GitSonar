import time

# 1. 비효율적인 알고리즘 (시간 복잡도 문제)
def find_duplicates(nums):
    duplicates = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                duplicates.append(nums[i])
    return duplicates

# 2. 매직 넘버 사용 (의미 없는 숫자 값 사용)
def calculate_discount(price):
    if price > 1000:
        return price * 0.9  # 할인율 10% (매직 넘버)
    return price

# 3. 로그 미사용 (디버깅 어려움)
def perform_task():
    print("Task started")  # 로그 대신 print 사용
    time.sleep(1)  # 작업 지연 시뮬레이션
    print("Task completed")

# 4. 불필요한 else 문 (가독성 저하)
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# 5. 미사용된 import (불필요한 코드)
import math  # 사용되지 않는 모듈

# 6. 너무 긴 함수 (유지보수 어려움)
def process_data(data):
    # 데이터 전처리
    cleaned_data = [x.strip().lower() for x in data]
    # 데이터 필터링
    filtered_data = [x for x in cleaned_data if len(x) > 3]
    # 데이터 정렬
    sorted_data = sorted(filtered_data)
    return sorted_data

# 함수 실행
print(find_duplicates([1, 2, 3, 2, 4, 5, 5]))
print(calculate_discount(1200))
perform_task()
print(is_even(4))