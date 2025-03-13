a, b, v = map(int, input().split())
if (v-b)%(a-b) == 0: ## 정상에 도달한경우
    print((v-b)//(a-b))
else: ## 아직 정상에 도달하지 못한 경우
    print(((v-b)//(a-b))+1)