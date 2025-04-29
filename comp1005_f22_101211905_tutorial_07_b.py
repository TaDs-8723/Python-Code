#Trae Smith 101211905
def adding_matrix(matrix1:list,matrix2:list)->list:
    added_matrix=[]
    if len(matrix1)==len(matrix2):
        double_check=True
        for j in range(len(matrix1)):
            if len(matrix1[j])!=len(matrix2[j]):
                double_check=False
        if double_check==True:
            for i in range(len(matrix1)):
                added_matrix.append(0)
                added_matrix[i]=[]
                for j in range(len(matrix2[i])):
                    adding=matrix1[i][j]+matrix2[i][j]
                    added_matrix[i].append(adding)

    return added_matrix
