# 1 2 5 7원으로 만드는 최소 갯수

n = int(input())

dp = [0, 1, 1, 2, 2, 1, 2, 1]  # 0~7까지

# idea : 처음에는 1 2 5 7 만큼 이전으로 간것 중 제일 작은것 +1로 하려고 했다.
# 그런데 생각해보니 7로 최대한 낸 다음에 나머지 지불 대금을 내면 될 것 같았다.
# a = n // 7  # 몫
# b = n % 7  # 나머지
# print(a+dp[b])

# 틀려서 생각해보니 반례로 10이 있었다.. 하핳..
# 그럼 다시 dp로 해보자!

if n >= 8:
    for i in range(8, n+1):
        result = min(dp[i-1], dp[i-2], dp[i-5], dp[i-7]) + 1
        dp.append(result)
print(dp[n])
