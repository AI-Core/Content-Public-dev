from typing import Callable

def check_step_1(
    data: list
) -> None:
    assert all(type(i)==tuple for i in data), ("The list should only contain tuples")
    assert all(len(i)==2 for i in data), ("The tuples should all contain 2 values")
    assert all(type(i[0])==str for i in data), ("The first element of each tuple should be a string")
    assert all(type(i[1])==int for i in data), ("The second element of each tuple should be an integer")

    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You initialised the data correctly.")
    
def check_step_2(
    data: list
) -> None:
    sort_num = lambda x : x[1]
    assert data==sorted(data, key=sort_num), ("The data isn't sorted correctly")

    print("\033[92m\N{heavy check mark} Well done!")

def check_step_3(
    data: list
) -> None:
    sort_name = lambda x : x[0]
    assert data==sorted(data, key=sort_name), ("The data isn't sorted correctly")

    print("\033[92m\N{heavy check mark} Well done!")

def check_step_4(
    data: list
) -> None:
    sort_name_len = lambda x : len(x[0])
    assert data==sorted(data, key=sort_name_len), ("The data isn't sorted correctly")

    print("\033[92m\N{heavy check mark} Well done!")

def check_step_5(
    data: list
) -> None:
    sort_name_len = lambda x : len(x[0])
    assert data==sorted(data, key=sort_name_len)[::-1], ("The data isn't sorted correctly")

    print("\033[92m\N{heavy check mark} Well done!")