import timeout_decorator
import io
from contextlib import redirect_stdout

@timeout_decorator.timeout(5, timeout_exception=TimeoutError)
def check_step_1(
    users_code: str,
) -> None:
    assert "for" in users_code, \
        ("You should use a for loop with the range function to loop through the numbers from 1 to 100. "
         "Please, try again.")
    assert "if" in users_code, \
        ("You should use an if statement to check if the number is divisible by 3 and 5. "
         "Please, try again.")
    assert "print" in users_code, \
        ("You should use the print function to print 'Fizz', 'Buzz', 'FizzBuzz' or the number. "
         "Please, try again.")
    try:
        f = io.StringIO()
        with redirect_stdout(f):
            exec(users_code)
        output = f.getvalue()
        assert '0' not in output, \
            ("You should not print 0. "
             "The loop should start from 1. "
             "Please, try again.")
        assert '101' not in output, \
            ("You should not print 101. "
             "The loop should end at 100. "
             "Please, try again.")
        output = output.strip()
        output = output.split('\n')
        for line in output:
            assert line[0] == '1', "The first number your code should print is 1. Please, try again."
            assert line[1] == '2', "The second number your code should print is 2. Please, try again."
            assert line[2] == 'Fizz', "The third number your code should print is 'Fizz'. Please, try again."
            assert line[3] == '4', "The fourth number your code should print is 4. Please, try again."
            assert line[4] == 'Buzz', "The fifth number your code should print is 'Buzz'. Please, try again."
            assert line[5] == 'Fizz', "The sixth number your code should print is 'Fizz'. Please, try again."
            assert line[14] == 'FizzBuzz', \
                "The fifteenth number your code should print is 'FizzBuzz'. Please, try again."
            assert line[29] == 'FizzBuzz', \
                "The thirtieth number your code should print is 'FizzBuzz'. Please, try again."
            assert line[99] == 'Buzz', "The hundredth number your code should print is 'Buzz'. Please, try again."

    except TimeoutError:
        raise TimeoutError("Your code is taking too long to run. "
                           "Make sure that you are using a for loop with the "
                           "range function to loop through the numbers from 1 to 100. "
                           "Please, try again.")
    except Exception as e:
        raise Exception("Your code is not working. "
                        "Before testing it, make sure you can run it without any errors. "
                        "Please, try again.") from e
    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "You successfully completed the FizzBuzz challenge"
        )
