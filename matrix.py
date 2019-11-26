import math


def print_matrix(result):
    for r in result:
         print(r)

def multiply(X, Y):
    # iterate through rows of X
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

#a
a_um = 0
a_dois = 1 
a_tres = 1 

#deslocamento
d_um = 200
d_dois = 1 
d_tres = 1 

#alfa
alfa_um = 0 
alfa_dois = 1
alfa_tres = 1 

#teta
teta_um = 0
teta_dois = 1
teta_tres = 1 
#matriz_transfromacao(a , d , alfa, teta

A0_1 = matriz_transfromacao(a_um ,d_um ,alfa_um,teta_um)
print_matrix(A0_1)
A1_2 = matriz_transfromacao(a_dois ,d_dois ,alfa_dois,teta_dois)
A2_3 = matriz_transfromacao(a_tres ,d_tres, alfa_tres, teta_tres)

# Program to multiply two matrices using nested loops

# result is 4x4
result = [[0,0,0,0],
    [0 ,0,0,0],
    [0 ,0,0,0 ],
    [0 ,0,0,0 ]]



A0_2 = multiply( A0_1, A1_2)
#A0_3 = multiply(A1_2, A2_3)


   