from typing import Callable

def check_step_1(
    data: list
) -> None:
    assert all(type(i)==string for i in data), ("The list should only contain strings")

    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You initialised the data correctly.")

def check_step_2(
    length_check: Callable[[str], bool],
    data: list,
    data_old: list
) -> None:
    
    assert isinstance(length_check, type(lambda x:x)), ("The function should utilise a lambda function")
    assert length_check('hello') == False, ("Lambda should evaluate for longer than 5 characters, not longer than or equal to 5 characters")
    assert data == list(filter(length_check, data)), ("You need to use the filter function on the data")

    print("\033[92m\N{heavy check mark} Well done!")

def check_step_3(
    length_vowel_check: Callable[[str], bool],
    data: list,
    data_old: list
) -> None:
    
    assert isinstance(length_vowel_check, type(lambda x:x)), ("The function should utilise a lambda function")
    assert length_vowel_check('hello') == False, ("Lambda should evaluate 'True' for strings longer than 5 characters, not longer than or equal to 5 characters")
    assert length_vowel_check('bananas') == False, ("Lambda should evaluate 'True' for strings longer than 5 characters that begin with a vowel")
    assert length_vowel_check('apple') == False, ("Lambda should evaluate 'False' for strings less than 5 characters that begin with a vowel")
    assert data == list(filter(length_vowel_check, data)), ("You need to use the filter function on the data")

    print("\033[92m\N{heavy check mark} Well done!")