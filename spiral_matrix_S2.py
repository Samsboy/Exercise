matrix = [[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12]]

ans=[]
row = len(matrix)
col = len(matrix[0])
ans.append(matrix[0])

if row >1:
  for i in range(1,row):
    ans.append(matrix[i][col-1])
  for j in range(col-2, -1 ,-1):
    ans.append(matrix[row-1][j])
  if col>1:
    for i in range(row-2,0,-1):
      ans.append(matrix[i][0])
   
M =[]

for k in range(1,row-1):
  t = matrix[k][1:-1]
  M.append(t)

res = ans + M
res
