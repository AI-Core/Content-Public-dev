from typing import Callable

def check_step_1(
    data: list
) -> None:
    assert all(type(i)==tuple for i in data), ("The list should only contain tuples")
    assert all(len(i)==2 for i in data), ("The tuples should all contain 2 values")

    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You initialised the data correctly.")
    
def check_step_2(
    data: list, 
    sort_num: Callable[[tuple], str]
) -> None:
    assert data==sorted(data, key=sort_num), ("The list should be sorted using the sort_num lambda as a key")

    print("\033[92m\N{heavy check mark} Well done!")

def check_step_3(
    data: list, 
    sort_name: Callable[[tuple], str]
) -> None:
    assert data==sorted(data, key=sort_name), ("The list should be sorted using the sort_name lambda as a key")

    print("\033[92m\N{heavy check mark} Well done!")

def check_step_4(
    data: list, 
    sort_name_len: Callable[[tuple], int]
) -> None:
    assert data==sorted(data, key=sort_name_len), ("The list should be sorted using the sort_name_len lambda as a key")

    print("\033[92m\N{heavy check mark} Well done!")

def check_step_5(
    data: list, 
    sort_name_len: Callable[[tuple], int]
) -> None:
    assert data==sorted(data, key=sort_name_len, reversed=True), ("The list should be sorted backwards using the sort_name_len lambda as a key")

    print("\033[92m\N{heavy check mark} Well done!")