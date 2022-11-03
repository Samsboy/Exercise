def spiralOrder(matrix: list[list[int]]) -> list[int]:
        res = []
        while matrix:
            res.extend(matrix.pop(0))  # pop 移除列表中[某個數值] 使 matrix 剩下沒pop的數值
            matrix[:] = list(zip(*matrix))[::-1]   
            # *matrix 可理解为解壓，返回二维矩阵式
            #matrix = list(zip(*matrix))[::-1]#AC
        #print(res)
        return res



a = [[1,2,3],
     [4,5,6],
    [7,8,10]]
 
    # Function call
print(spiralOrder(a))
