# Galois Field 2^4
def mult(A, B, mx_func=0b1000011, maximum=2**6):
    B = [int(i) for i in bin(B)[2:]]
    lst = []

    for i in B[::-1]:
        lst.append(A)
        A <<= 1
        if A >= maximum:
            A ^= mx_func
    
    res = 0
    lst.reverse()
    for i in range(len(B)):
        if B[i]:
            res ^= lst[i]
    return res

def mult_inv(A, mx_func=0b10011, maximum=2**4):
    for i in range(maximum):
        temp = mult(A, i, mx_func, maximum)
        if temp == 1:
            return i

def main():
    with open('output.txt', 'w') as output:
        for i in range(64):
            for j in range(64):
                s = f'{mult(i, j):>2} '
                if i == 43 and mult(i,j) == 1:
                    print(j)
                output.write(s)
            output.write('\n')

    # no_1 = mult(0x8a, 0x95, mx_func=0b100011011, maximum=0b100000000)
    # # print(hex(no_1))
    # print(mult_inv(0x2a, mx_func=0b100011011, maximum=2**8))
    # print(mult(0x2a, 152, mx_func=0b100011011, maximum=2**8))

if __name__=='__main__':
    # main()
    print(mult_inv(0x20, mx_func=0b100011011, maximum=0b100000000))