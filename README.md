# toolbox-py




```python
# 在 Python 3.10 中才能使用 TypeAlias 和类型联合运算符|。

# from lis.py
import math
import operator as op
from collections import ChainMap
from itertools import chain
from typing import Any, TypeAlias, NoReturn

Symbol: TypeAlias = str
Atom: TypeAlias = float | int | Symbol
Expression: TypeAlias = Atom | list

# lis.py：负责解析的主要函数
def parse(program: str) -> Expression:
    "从字符串中读取Scheme表达式。"
    return read_from_tokens(tokenize(program))

def tokenize(s: str) -> list[str]:
    "把字符串转换成词法单元列表。"
    return s.replace('(', ' ( ').replace(')', ' ) ').split()

def read_from_tokens(tokens: list[str]) -> Expression:
    "从一系列词法单元中读取表达式。"
    # 排版需要，省略了很多解析代码

# A ChainMap class is provided for quickly linking a number of mappings so they can be treated
# as a single unit. It is often much faster than creating a new dictionary and running multiple
# update() calls.

class Environment(ChainMap[Symbol, Any]):
    "ChainMap的子类，允许就地更改项。"

    # change 方法只更新现有的键。
    def change(self, key: Symbol, value: Any) -> None:
        "找到key在何处定义，更新对应的值。"
        for map in self.maps:
            if key in map:
                map[key] = value  # type: ignore[index]
                return
        raise KeyError(key)


def standard_env() -> Environment:
    "含有Scheme标准过程的环境。"
    env = Environment()
    env.update(vars(math))   # sin、cos、sqrt、pi等
    env.update({
            '+': op.add,
            '-': op.sub,
            '*': op.mul,
            '/': op.truediv,
            # 这里省略了很多运算符定义
            'abs': abs,
            'append': lambda *args: list(chain(*args)),
            'apply': lambda proc, args: proc(*args),
            'begin': lambda *x: x[-1],
            'car': lambda x: x[0],
            'cdr': lambda x: x[1:],
            # 这里省略了很多函数定义
            'number?': lambda x: isinstance(x, (int, float)),
            'procedure?': callable,
            'round': round,
            'symbol?': lambda x: isinstance(x, Symbol),
    })
    return env


def repl(prompt: str = 'lis.py> ') -> NoReturn:
    ""提示-读取-求值-输出"循环。"
    global_env = Environment({}, standard_env())
    while True:
        ast = parse(input(prompt))
        val = evaluate(ast, global_env)
        if val is not None:
            print(lispstr(val))

def lispstr(exp: object) -> str:
    "把Python对象转换成Lisp理解的字符串。"
    if isinstance(exp, list):
        return '(' + ' '.join(map(lispstr, exp)) + ')'
    else:
        return str(exp)


KEYWORDS = ['quote', 'if', 'lambda', 'define', 'set!']

def evaluate(exp: Expression, env: Environment) -> Any:
    "在环境中求解表达式。"
    match exp:
        case int(x) | float(x):
            return x
        case Symbol(var):
            return env[var]
        case ['quote', x]:
            return x
        case ['if', test, consequence, alternative]:
            if evaluate(test, env):
                return evaluate(consequence, env)
            else:
                return evaluate(alternative, env)
        case ['lambda', [*parms], *body] if body:
            return Procedure(parms, body, env)
        case ['define', Symbol(name), value_exp]:
            env[name] = evaluate(value_exp, env)
        case ['define', [Symbol(name), *parms], *body] if body:
            env[name] = Procedure(parms, body, env)
        case ['set!', Symbol(name), value_exp]:
            env.change(name, evaluate(value_exp, env))
        case [func_exp, *args] if func_exp not in KEYWORDS:
            proc = evaluate(func_exp, env)
            values = [evaluate(arg, env) for arg in args]
            return proc(*values)
        case _:
            raise SyntaxError(lispstr(exp))

class Procedure:
    "用户定义的Scheme过程。"

    def __init__(  
        self, parms: list[Symbol], body: list[Expression], env: Environment
    ):
        self.parms = parms  
        self.body = body
        self.env = env

    def __call__(self, *args: Expression) -> Any:  
        local_env = dict(zip(self.parms, args))  
        env = Environment(local_env, self.env)  
        for exp in self.body:  
            result = evaluate(exp, env)
        return result  
```
