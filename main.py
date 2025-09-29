# 소수 찾기와 소인수분해 예제
# 순수 파이썬만 사용

def is_prime(n):
    """주어진 수가 소수인지 확인하는 함수"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_factors(n):
    """주어진 수의 소인수분해 결과를 반환하는 함수"""
    factors = []

    # 2로 나누기
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # 3 이상의 홀수로 나누기
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 2

    # n이 소수인 경우
    if n > 2:
        factors.append(n)

    return factors


# 1부터 20까지의 수 중 소수 찾기
primes = []
for num in range(1, 21):
    if is_prime(num):
        primes.append(num)

print("1부터 20까지의 소수:")
print(primes)

# 여러 수의 소인수분해 결과 출력
test_numbers = [12, 15, 28, 36, 100]
print("소인수분해:")
for num in test_numbers:
    factors = prime_factors(num)
    factor_str = ' × '.join(map(str, factors))
    print(f"{num} = {factor_str}")

# 특정 범위의 소수 개수 계산
range_start = 1
range_end = 100
prime_count = sum(1 for n in range(range_start, range_end + 1) if is_prime(n))
print(f"{range_start}부터 {range_end}까지의 소수 개수: {prime_count}")
