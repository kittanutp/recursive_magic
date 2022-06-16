def hanoi_tower(n):
    a = list(range(n))
    b = list()
    c = list()
    return a,b,c

def move(f,h,t):
    t.insert(0,f[0])
    f.remove(f[0])
    print(f,h,t)


def ht_solver(n,f,h,t):
    if n > 0:
        ht_solver(n-1,f,t,h)
        move(f,h,t)
        ht_solver(n-1,h,f,t)
    else:
        return

a,b,c, = hanoi_tower(4)
print(a,b,c,)
ht_solver(len(a),a,b,c,)

