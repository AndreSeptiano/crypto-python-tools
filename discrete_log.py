def dlog(alpha=15, p=19, b=17):
    mult = 1
    for i in range(p - 1):
        if b == mult:
            return i
        mult = (mult * alpha) % p
    return -1

if __name__=='__main__':
    print(dlog(alpha=6, p=79, b=71))
    