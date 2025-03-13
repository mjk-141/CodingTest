## 파이썬 입력이 끝날때까지 받아오기
### 1. sys를 사용하는 방법
```
import sys
lines = sys.stdin.readlines()
for line in lines:
    a,b = map(int,input().split())
```

### 2. EOFError 예외처리
```
while True:
    try:
        a,b = map(int,input().split())
    except EOFError:
        break
```

## sep?
- 영단어 그대로, 분리하여 출력한다.
- 이때 분리할 문자를 지정하는데 이걸 구분자라고 한다.
```
print('s','q','e', sep='@')
>>> s@q@e
```

## end?
- end옵션을 사용하면 즐바꿈 안한다 무야호?

## format 옵션
- 포매팅을 통해 특정 서식에 따라 문자를 출력할 수 있다.