def add(a, b):
    return a+b


def mul(a, b):
    return a*b


def print_name():
    print(__name__)


# 시작점일 때만(단독으로 프로그램 실행하는 경우)
# 아래 코드 작성
if __name__ == '__main__':
    print(add(10, 20))
    print(mul(10, 20))
    print_name()
