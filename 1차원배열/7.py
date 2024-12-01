## Set 사용
# 모든 학생의 출석번호를 집합으로 초기화
all_students = set(range(1, 31))

# 제출한 학생들의 출석번호를 입력받아 집합에 추가
submitted_students = {int(input()) for _ in range(28)}

# 제출하지 않은 학생들의 출석번호 계산
missing_students = sorted(all_students - submitted_students)

# 결과 출력
print(missing_students[0])
print(missing_students[1])