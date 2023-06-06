class Group:
    def __init__(self, p):
        self.p = p
    
    def __mul__(self, other):
        new_p = []
        for item in self.p:
            p2 = other.get_permutation()
            new_p.append(p2[item - 1])
        return Group(new_p)
    
    def __str__(self):
        return str(self.p)
    
    def get_permutation(self):
        return self.p

def main():
    list_p = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    list_p = [Group(p) for p in list_p]

    for p1 in list_p:
        for p2 in list_p:
            print(p1 * p2, end=' ')
        print()

if __name__=='__main__':
    main()