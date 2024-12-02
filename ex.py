'''
l = [[1, 10, 'leehojun'], 
     [20, 30, 'hojun'], 
     [10, 20, 'weniv!'], 
     [1, 2, 'hello world'], 
     [55, 11, 'sun']]

# 1. 글자 수 대로 정렬해주세요.

# 2. 맨 앞에 위치한 숫자대로 정렬해주세요.

# 3. 중앙에 위치한 값대로 정렬해주세요.
'''

l = [[1, 10, 'leehojun'], 
     [20, 30, 'hojun'], 
     [10, 20, 'weniv!'], 
     [1, 2, 'hello world'], 
     [55, 11, 'sun']]

# 1. 글자 수 대로 정렬해주세요.

def sortLength(p):
    return len(p[2])

result_1 = sorted(l, key = sortLength)
print("1. 글자 수 대로 정렬 : ")
print(result_1)


print()

# 2. 맨 앞에 위치한 숫자대로 정렬해주세요.

def sortFirst(u):
    return u[0]

result_2 = sorted(l, key = sortFirst)
print("2. 맨 앞에 위치한 숫자대로 정렬 : ")
print(result_2)


print()

# 3. 중앙에 위치한 값대로 정렬해주세요.

def sortMiddle(n):
    return n[1]

result_3 = sorted(l, key = sortMiddle)

print("3. 중앙에 위치한 값대로 정렬 : ")
print(result_3)



print()


i = [[1, 10, 32], 
     [20, 30, 11], 
     [10, 20, 22], 
     [1, 2, 13], 
     [55, 11, 44]]


# 4. 3개의 전체 합이 작은 순서대로 출력해주세요.

def listSumFunction(s):
    return sum(s)

print("3개의 요소 전체 합이 작은 순서대로 정렬 : ", sorted(i, key = listSumFunction))