
def create_matrix(size: int, fill: int = 0) -> list[list[int]]:
    matrix = []
    sub_matrix = []
    for i in range(size):
        sub_matrix = []
        for j in range(size):
            sub_matrix.append(fill)
        matrix.append(sub_matrix)
    return matrix

def create_bool_matrix(size: int, fill: bool = False) -> list[list[bool]]:
    matrix = []
    sub_matrix = []
    for i in range(size):
        sub_matrix = []
        for j in range(size):
            sub_matrix.append(fill)
        matrix.append(sub_matrix)
    return matrix

def in_bounds(size: int, x: int, y: int) -> bool:
    return x <= size >= y 

def count_remaining_ships(ships: list[list[int]], shots: list[list[bool]]) -> int:
    n = len(ships)
    for i in range(n):
        for j in range(n):
            pass