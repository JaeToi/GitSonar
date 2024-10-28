# 1. Null 체크 누락 (잠재적 Null Pointer 문제)
def get_user_name(user):
    return user["name"]  # user가 None일 경우 예외 발생 가능

# 2. 부적절한 동시성 관리 (Race Condition 위험)
import threading

balance = 0

def deposit(amount):
    global balance
    for _ in range(100000):
        balance += amount

def withdraw(amount):
    global balance
    for _ in range(100000):
        balance -= amount

# 3. 불변 데이터를 가변으로 사용 (Immutable 객체를 가변으로 다룸)
def modify_tuple(t):
    t[0] = 10  # 튜플은 불변이므로 TypeError 발생

# 4. 중복된 조건문 (불필요한 코드 반복)
def check_status(status):
    if status == "active" or status == "ACTIVE":
        return True
    return False

# 5. 너무 많은 인자 전달 (함수 복잡도 증가)
def configure_system(ip, port, username, password, timeout, retries, log_file):
    print(f"Configuring system with {ip}:{port}...")

# 6. 너무 긴 클래스 (SRP 위반)
class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(str(self.users))

# 문제 있는 함수 실행
try:
    print(get_user_name(None))
except Exception as e:
    print(f"Error: {e}")

t1 = threading.Thread(target=deposit, args=(1,))
t2 = threading.Thread(target=withdraw, args=(1,))
t1.start()
t2.start()
t1.join()
t2.join()

print(f"Final Balance: {balance}")

try:
    modify_tuple((1, 2, 3))
except Exception as e:
    print(f"Error: {e}")

print(check_status("ACTIVE"))
configure_system("192.168.1.1", 8080, "admin", "password", 30, 3, "log.txt")