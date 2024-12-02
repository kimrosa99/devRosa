
l = [[1, 10, 'leehojun'], 
     [20, 30, 'hojun'], 
     [10, 20, 'weniv!'], 
     [1, 2, 'hello world'], 
     [55, 11, 'sun']]



# 1. 글자 수 대로 정렬해주세요.

def sortLength(a):
    return len(a[2])

result_1 = sorted(l, key = sortLength)
print(f"1. 글자 수 대로 정렬할 때\n{result_1}")


print()



# 2. 맨 앞에 위치한 숫자대로 정렬해주세요.

def sortFirstnum(b):
    return b[0]

result_2 = sorted(l,key = sortFirstnum)
print("2. 맨 앞에 위치한 숫자대로 정렬하면 ?\n{}".format(result_2))


print()



# 3. 중앙에 위치한 값대로 정렬해주세요.

def sortMiddle(c):
    return c[1]

return_3 = sorted(l, key = sortMiddle)
print(f"3. 중앙에 위치한 값대로 정렬한다면 ? \n{return_3}")

print()














i = [[1, 10, 32], 
     [20, 30, 11], 
     [10, 20, 22], 
     [1, 2, 13], 
     [55, 11, 44]]


# 4. 3개의 전체 합이 작은 순서대로 출력해주세요.

def listSumSort(d):
    return int(d[0] + d[1] + d[2])

result_4 = sorted(i, key = listSumSort)
print(f"3 개의 요소 전체 합이 작은 순서대로 정렬하면 \n{result_4}")