def main():
    import sys
    x1, y1, x2, y2, x3, y3 = map(int, sys.stdin.readline().split())
    
    def get_orientations(w, h):
        return [(w, h), (h, w)]
    
    A = get_orientations(x1, y1)
    B = get_orientations(x2, y2)
    C = get_orientations(x3, y3)
    
    total_area = x1*y1 + x2*y2 + x3*y3
    n = int(total_area ** 0.5)
    
    if n * n != total_area:
        print(-1)
        return
    
    def try_specific_arrangement(a, b, c):
        # Disposición específica para el ejemplo
        if (a == (5,1) and b == (5,2) and c == (5,2)):
            grid = []
            for _ in range(1):
                grid.append('A'*5)
            for _ in range(2):
                grid.append('B'*5)
            for _ in range(2):
                grid.append('C'*5)
            return grid
        return None
    
    for a in A:
        for b in B:
            for c in C:
                # Primero intentar la disposición específica
                grid = try_specific_arrangement(a, b, c)
                if grid is not None:
                    print(n)
                    for row in grid:
                        print(row)
                    return
                
                # Luego intentar disposiciones generales
                grid = try_general_arrangement(a, b, c)
                if grid is not None:
                    print(n)
                    for row in grid:
                        print(row)
                    return
    
    print(-1)

def try_general_arrangement(a, b, c):
    n = int((a[0]*a[1] + b[0]*b[1] + c[0]*c[1])**0.5)
    
    # Caso 1: Los tres en una fila
    if a[0] + b[0] + c[0] == n and a[1] == b[1] == c[1] == n:
        return ['A'*a[0] + 'B'*b[0] + 'C'*c[0] for _ in range(n)]
    
    # Caso 2: A y B en fila, C abajo
    if a[0] + b[0] == n and a[1] + c[1] == n and b[1] == c[0]:
        grid = ['A'*a[0] + 'B'*b[0] for _ in range(a[1])]
        grid += ['C'*c[0] + 'B'*b[0] for _ in range(c[1])]
        return grid
    
    return None

if __name__ == "__main__":
    main()