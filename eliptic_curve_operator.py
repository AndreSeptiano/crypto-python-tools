from exception import NotInvertibleError

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def inverse(num, p):
    t = 0
    r = p
    newt = 1
    newr = num

    while newr != 0:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr

    if r > 1:
        raise NotInvertibleError(f'{num} is Not Invertible')
    if t < 0:
        t += p
    return t

def lambda_p(P, Q, a, p):
    xp, yp = P
    xq, yq = Q

    if P == Q:
        return ((3 * xp * xp + a) * inverse(2 * yp, p)) % p
    else:
        return ((yq - yp) * inverse(xq - xp, p)) % p

def addition(P, Q, a, p):
    if Q == 'O':
        return P

    xp, yp = P
    xq, yq = Q
    if xp == xq and yp + yq == p:
        return 'O'
    
    lmda = lambda_p(P, Q, a, p)
    xr = (lmda ** 2 - xp - xq) % p
    yr = (lmda * (xp - xr) - yp) % p

    return xr, yr
    
if __name__=='__main__':
    Gs = [(2,2)]
    a, b, p = (2,5,13)

    for i in range(2,15):
        Gs.append(addition(Gs[0], Gs[-1], a, p))
    # G28 = addition(Gs[-1],Gs[-1],a,p)
    # G31 = addition(G28,Gs[2],a,p)
    # print(G31)
    print(Gs)