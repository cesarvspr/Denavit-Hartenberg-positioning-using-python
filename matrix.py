import math


def print_matrix(result):
    for r in result:
         print(r)

def multiply(X, Y):
    # iterate through rows of X

    result = [[0,0,0,0],
    [0 ,0,0,0],
    [0 ,0,0,0 ],
    [0 ,0,0,0 ]]
    # result is 4x4

    for i in range(len(X)):
    # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

def matriz_transfromacao(a , d , alfa, teta):
    M = [[math.cos(teta),-math.sin(teta)*math.cos(alfa), math.sin(teta)*math.sin(alfa), a*math.cos(teta)],

    [math.sin(teta) , math.cos(teta)*math.cos(alfa), -math.cos(teta)*math.sin(alfa), a*math.sin(teta)],

    [0 , math.sin(alfa), math.cos(alfa), d ],
    
    [0,0,0,1]]
    return M

#insira os parametros 

#1
a_um = 0
d_um = 200
teta_um = 0
alfa_um = 0

#2  
a_dois = 1 
d_dois = 1
alfa_dois = -90
teta_dois = 1

#3
a_tres = 1 
d_tres = 1 
alfa_tres = 1 
teta_tres = 1


#matriz_transfromacao(a , d , alfa, teta)

A0_1 = matriz_transfromacao(a_um ,d_um ,alfa_um,teta_um)
A1_2 = matriz_transfromacao(a_dois ,d_dois ,alfa_dois,teta_dois)
A2_3 = matriz_transfromacao(a_tres ,d_tres, alfa_tres, teta_tres)

#resultados
print('')
print("PARA A0_1 TEMOS: ")
A0_1 = A0_1
print_matrix(A0_1)
print('')

print("PARA A0_2 TEMOS: ")
A0_2 = multiply( A0_1, A1_2)
print_matrix(A0_2)
print('')

print("PARA A0_3 TEMOS: ")
A0_3 = multiply(multiply(A0_1, A1_2), A2_3)
print_matrix(A0_3)
print('')


   