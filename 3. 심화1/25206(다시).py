score_list = [("A+",4.5),("A0",4.0),("B+",3.5),("B0",3.0),("C+",2.5),("C0",2.0),("D+",1.5),("D0",1.0),("F",0.0)]
all_score = 0
avg_score = 0
for i in range(20):
    subject, score, grade = map(input().split())
    if grade == 'P':
        pass
    else:
        all_score+= score
        for score_list_grade, score_list_score in score_list:
            if grade == score_list_grade:
                avg_score+=(score * score_list_score)
                break
print({})
