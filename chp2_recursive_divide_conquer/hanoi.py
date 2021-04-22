n = int(input('Input the Hanoi tower\'s level: '))
tower_a = list(reversed(range(1, n+1)))
tower_b = list()
tower_c = list()
COUNT = 0


def hanoi(n, a, b, c):
    global COUNT
    global tower_a
    global tower_b
    global tower_c
    if n > 0:
        hanoi(n-1, a, c, b)
        b.append(a.pop())
        COUNT += 1
        print(COUNT)
        print(f'a: {tower_a}')
        print(f'b: {tower_b}')
        print(f'c: {tower_c}')
        hanoi(n-1, c, b, a)


hanoi(n, tower_a, tower_b, tower_c)
print(f'Need move {COUNT} times')

# If you want to know how the price moved, just debug and watching the var of 
# tower_a,b,c. Attention: dont watching the var a,b,c.
