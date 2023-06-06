def is_elliptic_curve(x, y, a=4, b=4, p=5):
    lhs = (y ** 2) % p
    rhs = (x ** 3 + a * x + b) % p
    return lhs == rhs

def main():
    abp_triple = [
        (2,5,13),
    ]

    res = {(a,b,p):
            ['O'] +                                     # Titik O pasti termasuk kurva eliptik
            [(x, y) for x in range(p)                   # Brute force O(p^2)
                    for y in range(p)                   
                    if is_elliptic_curve(x,y,a,b,p)]
           for a,b,p in abp_triple}                     # Hashmap<Triple,List of xy pair>
            
    for triple, points in res.items():
        print(f'{triple}: {points}')

if __name__=='__main__':
    main()