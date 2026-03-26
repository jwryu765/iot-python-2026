# ex02_array.py 배열 -> 리스트(List)

arr = [30, 50, 10]  # 리스트 초기화
print(arr)

arr.append(70)  # 리스트 마지막 값 추가
print(arr)

print(arr.index(50)) # 리스트 중 요소 위치 리턴

arr2 = arr.copy()  # 리스트 복사
print(arr2)

arr.insert(2, 90)  # 특정 위치에 값을 추가
print(arr2)

print(arr2.count(10)) # 리스트에 값이 몇개 있는지 확인

print(arr.pop()) # 70이 꺼내짐

arr.remove(50)  # 특정 값이 삭제
print(arr)

arr.extend(arr2) # 리스트 arr에 리스트 arr2 전부 합치기
print(arr)

arr.reverse() # 요소 순서를 역순으로 변경
print(arr)

arr.sort() # ASCending 정렬
print(arr)

arr.sort(reverse=True) # DESCending Python True/False
print(arr)

arr.append('Python')
print(arr)

arr.append([6, 7, 9])
print(arr)

arr.remove(30) # 같은 요소 하나만 삭제
print(arr)

arr.clear() # 모든 요소 삭제
print(arr)