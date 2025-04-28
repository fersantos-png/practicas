import math

def solve():
    a = int(input())
    for _ in range(a):
        N = int(input("ingresa las veces que besse se a quedado dormida en la semana:  "))
        a = list(map(int, input("ingresa las horas que se a quedado dormida: ").split()))
        total = sum(a)
        
        if total == 0:
            print(0)
            continue
        
        # Encontrar todos los divisores posibles
        divisor = set()
        for i in range(1, int(math.isqrt(total)) + 1):
            if total % i == 0:
                divisor.add(i)
                divisor.add(total // i)
        
        min_op = float('inf')
        
        for d in divisor:
            suma = 0
            op = 0
            posible = True
            
            for num in a:
                suma += num
                if suma == d:
                    suma = 0
                elif suma > d:
                    posible = False
                    break
            
            if posible and suma == 0:
                # El número de operaciones es N - (total / d)
                op = N - (total // d)
                if op < min_op:
                    min_op = op
        
        print(min_op)

solve()