import itertools
import time
from threading import Thread, Event 

def spin(msg: str, done: Event) -> None:
    for char in itertools.cycle(r'\|/-'):    # itertools.cycle 一次产出一个字符，一直反复迭代字符串。
        status = f'\r{char} {msg}'      # 用文本实现动画的技巧：使用 ASCII 回车符（'\r'）把光标移到行头。
        print(status, end='', flush=True)  # 显示空格，并把光标移到开头，清空状态行。
        if done.wait(.1):
            break
        blanks = ' ' * len(status)
        print(f'\r{blanks}\r', end='')

def slow() -> int:
    time.sleep(3)
    return 42

def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args=('thinking!', done))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = slow()
    done.set()
    spinner.join()  # 等待，直到 spinner 线程结束。
    return result

result = supervisor()
print(f'Answer: {result}')
