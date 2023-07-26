from typing import Callable

def check_step_1(
    square: Callable[[int], int],
    numbers: list,
    numbers_old: list
) -> None:
    assert isinstance(square, type(lambda x:x)), "The function should utilise a lambda function"
    assert numbers == map(square, numbers_old), ("You need to map the lambda function square to the list numbers")

    print("\033[92m\N{heavy check mark} Well done!")
    
def check_step_2(
    cube: Callable[[int], int],
    numbers: list,
    numbers_old: list
) -> None:
    assert isinstance(cube, type(lambda x:x)), "The function should utilise a lambda function"
    assert numbers == map(cube, numbers_old), ("You need to map the lambda function cube to the list numbers")

    print("\033[92m\N{heavy check mark} Well done!")

def check_step_3(
    func: Callable[[int], int],
    numbers: list,
    numbers_old: list
) -> None:
    assert isinstance(func, type(lambda x:x)), "The function should utilise a lambda function"
    assert numbers == map(func, numbers_old), ("You need to map the lambda function func to the list numbers")

    print("\033[92m\N{heavy check mark} Well done!")