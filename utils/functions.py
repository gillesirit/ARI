############# UTILITIES
#def xor(x,y): 
#    return (not(x) and y) or (x and not(y))  

def xor(x,y): 
    if (x==0 and y!=0) or (x!=0 and y==0):
        return 1
    return 0

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False;
    return True

def binary_2_decimal(binary): #binary is a list of digits
    decimal=0
    for i in binary:
        decimal = 2*decimal + i 
    return(decimal) 
#############
############# 8 FUNCTIONS TO BE TESTED - DIMENSION 10     
def g1_array(arr):
    if (arr[0]!=0) and ((arr[1]!=0) or (arr[2]!=0)):
        return 1
    return 0
    

def g2(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    if (not(x1) and x2) or (x1 and not(x2)) :
        return 1
    return 0

def g2_array(arr):
    if ((arr[0]==0) and (arr[1]!=0)) or ((arr[0]!=0) and (arr[1]==0)) :
        return 1
    return 0
    

def g3(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    if xor(xor(x1,x2),x3):
        return 1
    return 0

def g3_array(arr):
    return xor(xor(arr[0],arr[1]),arr[2])
      
    
def g4(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    if (x1+x2+x3+x4+x5+x6+x7+x8+x9+x10==3):
        return 1
    return 0

def g4_array(arr):
    if sum(arr)==3:
        return 1
    return 0

def g5(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    if (x1 or x2 or x3) and (x4 or not(x5) or x6):
        return 1
    return 0

def g5_array(arr):
    if ((arr[0]!=0) or (arr[1]!=0) or (arr[2]!=0)) and ((arr[3]!=0) or (arr[4]==0) or (arr[5]!=0)):
        return 1
    return 0

def g6(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    if (x1 and (x2 or not (x3))):
        return 1
    return 0

def g6_array(arr):
    if (arr[0]!=0) and ((arr[1]!=0 or (arr[2]==0))):
        return 1
    return 0

def g7(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    if (x1 + x2 + x3 == 2):
        return 1
    return 0

def g7_array(arr):
    if (arr[0] + arr[1] + arr[2] == 2):
        return 1
    return 0

def g8(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10): #no obvious relevant features
    if (is_prime(binary_2_decimal([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]))):
        return 1
    return 0

def g8_array(arr):
    if (is_prime(binary_2_decimal(arr))):
        return 1
    return 0