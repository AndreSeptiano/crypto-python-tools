from exception import IncompatibleFieldError, NotInvertibleError

class GaloisField:
    def __init__(self, num, p=7):
        self.num = num
        self.p = p

    def __mul__(self, other):
        if self.p == other.p:
            res = (self.num * other.num) % self.p
            return GaloisField(res, p=self.p)
        else:
            raise IncompatibleFieldError('Incompatible number!')
    
    def __add__(self, other):
        if self.p == other.p:
            res = (self.num + other.num) % self.p
            return GaloisField(res, p=self.p)
        else:
            raise IncompatibleFieldError('Incompatible number!')
    
    def __sub__(self, other):
        if self.p == other.p:
            res = (self.num - other.num) % self.p
            return GaloisField(res, p=self.p)
        else:
            raise IncompatibleFieldError('Incompatible number!')
    
    def __pow__(self, other):
        exp = 0
        res = 0
        if type(other) == type(self):
            exp = other.num
        else:
            exp = int(other)

        if exp >= 0:
            res = pow(self.num, exp, self.p)
        else:
            res = pow(self.inverse().num, -exp, self.p)
        return GaloisField(res, p=self.p)
    
    def inverse(self):
        t = 0
        r = self.p
        newt = 1
        newr = self.num

        while newr != 0:
            q = int(r / newr)
            t, newt = newt, t - q * newt
            r, newr = newr, r - q * newr
        
        if r > 1:
            raise NotInvertibleError(f'{self.num} is Not Invertible')
        if t < 0:
            t += self.p
        return GaloisField(t, p=self.p)

    def __truediv__(self, other):
        if self.p == other.p:
            inv = other.inverse()
            res = (self.num * inv.num) % self.p
            return GaloisField(res, p=self.p)
        else:
            raise IncompatibleFieldError('Incompatible number!')

    def __str__(self):
        return str(self.num)
    
def main():
    gf = [GaloisField(i) for i in range(7)]
    print('Galois Field Addition')
    for i in gf:
        for j in gf:
            print(i + j, end=' ')
        print()

    print()
    print('Galois Field Multiplication')
    for i in gf:
        for j in gf:
            print(i * j, end=' ')
        print()

    print()
    print('Galois Field Inverse')
    for i in gf:
        try:
            print(f'{i}:{i.inverse()}')
        except NotInvertibleError:
            print(f'{i} is not invertible.')

    print()
    print('Galois Field Division')
    for i in gf:
        for j in gf:
            try:
                print(i / j, end=' ')
            except NotInvertibleError:
                print('N', end=' ')
        print()

    print()
    print('-------------------------------------')
    print()

    gf17 = [GaloisField(i,17) for i in range(17)]
    for i in gf17:
        try:
            print(f'{i}:{i.inverse()}')
        except NotInvertibleError:
            print(f'{i} is not invertible.')

    gf2 = [GaloisField(i,2) for i in range(2)]
    for i in gf2:
        try:
            print(f'{i}:{i.inverse()}')
        except NotInvertibleError:
            print(f'{i} is not invertible.')

if __name__=='__main__':
    main()