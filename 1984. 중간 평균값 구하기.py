#1984. 중간 평균값 구하기

T = int(input())
arr=[]

for t in range(1, T+1):
  arr = list(map(int,input().split()))
  arr.remove(min(arr))
  arr.remove(max(arr))
  avg = sum(arr)/len(arr)

  print("#{} {:.0f}".format(t,avg))
