#Open lincense, code made by César Sampaio 


import math

#This prinTs the matrix
def print_matrix(result):
    for r in result:
         print(r)

#Multiply the matrix
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


#This returns the transformation matrix

def matriz_transfromacao(a , d , alfa, teta):
    M = [[math.cos(math.radians(teta)),-math.sin(math.radians(teta))*math.cos(math.radians(alfa)), math.sin(math.radians(teta))*math.sin(math.radians(alfa)), a*math.cos(math.radians(teta))],

    [math.sin(math.radians(teta)) , math.cos(math.radians(teta))*math.cos(math.radians(alfa)), -math.cos(math.radians(teta))*math.sin(math.radians(alfa)), a*math.sin(math.radians(teta))],

    [0 , math.sin(math.radians(alfa)), math.cos(math.radians(alfa)), d ],
    
    [0,0,0,1]]
    return M
    #PAY ATTENTION, THIS FUNCTIONS RETURNS SMALL NUMBERS THAT YOUR CAN CONSIDER ZERO DENPENDIG THE CONTEXT. 

#Parameters inserting
#Insira os parametros 

#1
a_um = 200
d_um = 0
teta_um = 135
alfa_um = 0

#2  
a_dois = 300
d_dois = 0
alfa_dois = 0
teta_dois = -90

#3
a_tres = 0
d_tres = 0 
alfa_tres = 0 
teta_tres = 0


#Matriz_transfromacao(a , d , alfa, teta)
#Transformation matrix(a, d, alfa, theta)

A0_1 = matriz_transfromacao(a_um ,d_um ,alfa_um,teta_um)
A1_2 = matriz_transfromacao(a_dois ,d_dois ,alfa_dois,teta_dois)
A2_3 = matriz_transfromacao(a_tres ,d_tres, alfa_tres, teta_tres)

#Results
#Resultados

print('')
print("PARA A0_1 TEMOS: ")
print_matrix(A0_1)
print('')



print("PARA A1_2 TEMOS: ")
print_matrix(A1_2)
print('')

print("PARA A0_2 TEMOS: ")
A0_2 = multiply( A0_1, A1_2)
print_matrix(A0_2)
print('')





