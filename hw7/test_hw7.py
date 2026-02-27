"""
CMSC 14100
Winter 2026

Test code for Homework #7
"""
import pytest
import helpers
import sys
import os
import hw7

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw7"

def attribute_error_message(attr, expected, actual):
    return (f"The actual and expected value of the {attr} attribute of the object do not match\n"
            f"  Expected: {expected}\n"
            f"  Actual: {actual}")

@pytest.mark.parametrize("name",
                         [
                            ("cs141"),
                            ("engl158")
                         ])
def test_directory_constructor(name):
    steps = [f"d = hw7.Directory(\"{name}\")"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw7.Directory(name)

        if actual.name != name:
            steps = steps + ["d.name"]
            err_msg = attribute_error_message("name", name, actual.name)

            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

@pytest.mark.parametrize("name, contents, size",
                        [
                            ("hw1.py", "", 0),
                            ("exam.pdf", "", 0),
                            ("hw1.py", "print('Hello, world!')", 22),
                            ("homework1.c", "using namespace std;", 20)
                        ])
def test_file_constructor(name, contents, size):

    steps = [f"f = hw7.File(\"{name}\", \"{contents}\")"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    err_msg = None

    try:
        actual = hw7.File(name, contents)

        if actual.name != name:
            steps = steps + ["f.name"]
            err_msg = attribute_error_message("name", name, actual.name)

        elif actual.is_open:
            steps = steps + ["f.is_open"]
            err_msg = attribute_error_message("is_open", False, actual.is_open)

        elif actual.size != size:
            steps = steps + ["f.size"]
            err_msg = attribute_error_message("size", size, actual.size)

        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("name, contents",
                        [
                            ("hw1.py", ""),
                            ("exam.pdf", ""),
                            ("hw1.py", "print('Hello, world!')"),
                            ("homework1.c", "using namespace std;"),
                            ("homework1.c", "#include <stdio.h> using namespace std;")
                        ])
def test_cat(name, contents):
    steps = [f"f = hw7.File(\"{name}\", \"{contents}\")",
             "f.cat()"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        f = hw7.File(name, contents)
        actual = f.cat()
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, contents)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

@pytest.mark.parametrize("name, contents",
                        [
                            ("hw1.py", ""),
                            ("exam.pdf", ""),
                            ("hw1.py", "print('Hello, world!')"),
                            ("homework1.c", "using namespace std;"),
                            ("homework1.c", "#include <stdio.h>")
                        ])
def test_open_file_from_close(name, contents):
    steps = [f"f = hw7.File(\"{name}\", \"{contents}\")",
             "f.open_file()",
             "f.is_open"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    err_msg = None

    try:
        actual = hw7.File(name, contents)
        actual.open_file()

        if not actual.is_open:
            err_msg = attribute_error_message("is_open", True, actual.is_open)
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

@pytest.mark.parametrize("name, contents",
                        [
                            ("hw1.py", ""),
                            ("exam.pdf", ""),
                            ("hw1.py", "print('Hello, world!')"),
                            ("homework1.c", "using namespace std;"),
                            ("homework1.c", "#include <stdio.h>")
                        ])
def test_open_file_from_open(name, contents):
    steps = [f"f = hw7.File(\"{name}\", \"{contents}\")",
             "f.is_open = True"
             "f.open_file()",
             "f.is_open"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    err_msg = None

    try:
        actual = hw7.File(name, contents)
        actual.open_file()

        if not actual.is_open:
            err_msg = attribute_error_message("is_open", True, actual.is_open)
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

@pytest.mark.parametrize("name, contents",
                        [
                            ("hw1.py", ""),
                            ("exam.pdf", ""),
                            ("hw1.py", "print('Hello, world!')"),
                            ("homework1.c", "using namespace std;"),
                            ("homework1.c", "#include <stdio.h>")
                        ])
def test_close_file_from_open(name, contents):
    steps = [f"f = hw7.File(\"{name}\", \"{contents}\")",
             "f.is_open = True",
             "f.close_file()",
             "f.is_open"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    err_msg = None

    try:
        actual = hw7.File(name, contents)
        actual.is_open = True
        actual.close_file()

        if actual.is_open:
            err_msg = attribute_error_message("is_open", False, actual.is_open)
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

@pytest.mark.parametrize("name, contents",
                        [
                            ("hw1.py", ""),
                            ("exam.pdf", ""),
                            ("hw1.py", "print('Hello, world!')"),
                            ("homework1.c", "using namespace std;"),
                            ("homework1.c", "#include <stdio.h>")
                        ])
def test_close_file_from_close(name, contents):
    steps = [f"f = hw7.File(\"{name}\", \"{contents}\")",
             "f.close_file()",
             "f.is_open"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    err_msg = None

    try:
        actual = hw7.File(name, contents)
        actual.close_file()

        if actual.is_open:
            err_msg = attribute_error_message("is_open", False, actual.is_open)
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("name, contents, to_add",
                        [
                            ("hw1.py", "", ""),
                            ("exam.pdf", "", "Write your name:"),
                            ("hw1.py", "print('Hello, world!')", " x = 42"),
                            ("homework1.c", "using namespace std;", "int main()"),
                            ("homework1.c", "#include <stdio.h> using namespace std;", "int main()")
                        ])
def test_redirect_successes(name, contents, to_add):
    steps = [f"f = hw7.File(\"{name}\", \"{contents}\")",
             "f.open_file()",
             f"f.redirect(\"{to_add}\")"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    err_msg = None

    try:
        actual = hw7.File(name, contents)
        actual.open_file()
        result = actual.redirect(to_add)

        if actual.cat() != contents + to_add:
            err_msg = attribute_error_message("__contents", contents + to_add, actual.cat())

        elif actual.size != len(contents + to_add):
            err_msg = attribute_error_message("size", len(contents + to_add), actual.size)

        elif not result:
            err_msg = helpers.check_result(result, True)

        if err_msg is not None:
                pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("name, contents, to_add",
                        [
                            ("homework1.c", "using namespace std;", "int main()"),
                            ("hw1.py", "", ""),
                            ("exam.pdf", "", "Write your name:"),
                            ("hw1.py", "print('Hello, world!')", "x = 42"),
                            ("homework1.c", "using namespace std;", "int main()"),
                            ("homework1.c", "#include <stdio.h> using namespace std;", "int main()")
                        ])
def test_redirect_failures(name, contents, to_add):
    steps = [f"f = hw7.File(\"{name}\", \"{contents}\")",
             f"f.redirect(\"{to_add}\")"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    err_msg = None

    try:
        actual = hw7.File(name, contents)
        result = actual.redirect(to_add)

        if actual.cat() != contents:
            err_msg = attribute_error_message("__contents", contents, actual.cat())

        elif result:
            err_msg = helpers.check_result(result, False)

        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

@pytest.mark.parametrize("name1, name2, contents1, contents2, expected",
                        [
                            ("hw1.py", "hw2.py", "", "", ""),
                            ("hw1.py", "hw2.py", "print()", "print()", "print()"),
                            ("hw1.py", "hw2.py", "Print", "print()", "-rint--"),
                            ("notes.txt", "hw2.py", "PRINT()", "print()", "-----()"),
                            ("notes.txt", "hw2.py", "print", "print()", "print--"),
                            ("notes.txt", "hw2.py", "PRINT()", "print", "-------"),
                            ("hw1.py", "Lab1.pdf", "PRINT!!", "print()", "-------"),
                            ("hw1.py", "Lab1.pdf", "print()    ", "print()", "print()----"),
                            ("hw1.py", "Lab1.pdf", "print ()", "print()", "print---")
                        ])
def test_diff(name1, name2, contents1, contents2, expected):
    steps = [f"f1 = hw7.File(\"{name1}\", \"{contents1}\")",
             f"f2 = hw7.File(\"{name2}\", \"{contents2}\")",
             "f1.diff(f2)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        f1 = hw7.File(name1, contents1)
        f2 = hw7.File(name2, contents2)
        actual = f1.diff(f2)

        err_msg = helpers.check_result(actual, expected)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

def test_ls0():

    try:
        fs, steps = fs1()
        steps = steps + ["fs.ls()"]
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

        actual = fs.ls()
        expected = []

        if actual != expected:
            err_msg = helpers.check_result(actual, expected)
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

def test_ls1():

    try:
        fs, steps = fs1()
        steps = steps + ["fs.ls()"]
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

        actual = fs.ls()
        expected = []

        if actual != expected:
            err_msg = helpers.check_result(actual, expected)
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

def test_ls2():

    try:
        fs, steps = fs2()
        steps = steps + ["fs.ls()"]
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

        actual = fs.ls()
        expected = ["cs141/notes.txt"]

        if actual != expected:
            err_msg = helpers.check_result(actual, expected)
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

def test_ls3():

    try:
        fs, steps = fs3()
        steps = steps + ["fs.ls()"]
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

        actual = fs.ls()
        expected = ["cs141/hw1.py", "cs141/notes.txt"]

        if actual != expected:
            err_msg = helpers.check_result(actual, expected)
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

def test_ls4():

    try:
        fs, steps = fs4()
        steps = steps + ["fs.ls()"]
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

        actual = fs.ls()
        expected = ["chem101/Lab1.pdf", "cs141/notes.txt"]

        if actual != expected:
            err_msg = helpers.check_result(actual, expected)
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

def test_ls5():

    try:
        fs, steps = fs5()
        steps = steps + ["fs.ls()"]
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

        actual = fs.ls()
        expected = ["chem101/Lab1.pdf", "cs141/hw1.py", "cs141/notes.txt"]

        if actual != expected:
            err_msg = helpers.check_result(actual, expected)
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

def test_ls6():

    try:
        fs, steps = fs6()
        steps = steps + ["fs.ls()"]
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

        actual = fs.ls()
        expected = ["chem101/Lab1.pdf", "chem101/Lab2.pdf", "cs141/hw7.py", "cs141/notes.txt", "math151/notes.txt"]

        if actual != expected:
            err_msg = helpers.check_result(actual, expected)
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

def check_file(actual_file, expected_name, expected_contents):
    if actual_file.name != expected_name:
        return attribute_error_message("name", expected_name, actual_file.name)

    if actual_file.cat() != expected_contents:
        return attribute_error_message("__contents", expected_contents, actual_file.cat())

    return None

def test_touch1():

    try:
        d = hw7.Directory("cs141")
        result = d.touch("hw7.py", "# Classes/objects", True)

        steps = ["d = hw7.Directory(\"cs141\")",
                 "d.touch(\"hw7.py\", \"# Classes/objects\", True)"]
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

        err_msg = None

        if len(d.files) != 1:
            err_msg = "New file not found"

        elif "hw7.py" not in d.files:
            err_msg = "\"hw7.py\" file not found"

        elif not result:
            err_msg = helpers.check_result(result, True)

        else:
            f = d.files["hw7.py"]
            err_msg = check_file(f, "hw7.py", "# Classes/objects")

        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

def test_touch2():

    try:
        d = hw7.Directory("cs141")
        result = d.touch("hw7.py", "# Classes/objects", False)

        steps = ["d = hw7.Directory(\"cs141\")",
                 "d.touch(\"hw7.py\", \"# Classes/objects\", False)"]
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

        err_msg = None

        if len(d.files) != 1:
            err_msg = "New file not found"

        elif "hw7.py" not in d.files:
            err_msg = "\"hw7.py\" file not found"

        elif not result:
            err_msg = helpers.check_result(result, True)

        else:
            f = d.files["hw7.py"]
            err_msg = check_file(f, "hw7.py", "# Classes/objects")

        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

def test_touch3():

    try:
        d = hw7.Directory("cs141")
        d.add_file(hw7.File("hw7.py", "print(42)"))
        result = d.touch("hw7.py", "# Classes/objects", True)

        steps = ["d = hw7.Directory(\"cs141\")",
                 "d.add_file(hw7.File(\"hw7.py\", \"print(42)\"))",
                 "d.touch(\"hw7.py\", \"# Classes/objects\", True)"]
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

        err_msg = None

        if len(d.files) != 1:
            err_msg = "New file not found"

        elif "hw7.py" not in d.files:
            err_msg = "\"hw7.py\" file not found"

        elif not result:
            err_msg = helpers.check_result(result, True)

        else:
            f = d.files["hw7.py"]
            err_msg = check_file(f, "hw7.py", "# Classes/objects")

        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

def test_touch4():

    try:
        d = hw7.Directory("cs141")
        d.add_file(hw7.File("hw7.py", "print(42)"))
        result = d.touch("hw7.py", "# Classes/objects", False)

        steps = ["d = hw7.Directory(\"cs141\")",
                 "d.add_file(hw7.File(\"hw7.py\", \"print(42)\"))",
                 "d.touch(\"hw7.py\", \"# Classes/objects\", False)"]
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

        err_msg = None

        if len(d.files) != 1:
            err_msg = "New file not found"

        elif "hw7.py" not in d.files:
            err_msg = "\"hw7.py\" file not found"

        elif result:
            err_msg = helpers.check_result(result, False)

        else:
            f = d.files["hw7.py"]
            err_msg = check_file(f, "hw7.py", "print(42)")

        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

def test_touch5():

    try:
        d = hw7.Directory("cs141")
        d.add_file(hw7.File("hw7.py", "print(42)"))
        result = d.touch("hw8.py", "# Recursion", True)

        steps = ["d = hw7.Directory(\"cs141\")",
                 "d.add_file(hw7.File(\"hw7.py\", \"print(42)\"))",
                 "d.touch(\"hw8.py\", \"# Recursion\", True)"]
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

        err_msg = None

        if len(d.files) != 2:
            err_msg = "New file not found"

        elif "hw7.py" not in d.files:
            err_msg = "\"hw7.py\" file not found"

        elif "hw8.py" not in d.files:
            err_msg = "\"hw8.py\" file not found"

        elif not result:
            err_msg = helpers.check_result(result, True)

        else:
            f = d.files["hw7.py"]
            err_msg = check_file(f, "hw7.py", "print(42)")

        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

def test_touch6():

    try:
        d = hw7.Directory("cs141")
        d.add_file(hw7.File("hw7.py", "print(42)"))
        result = d.touch("hw8.py", "# Recursion", False)

        steps = ["d = hw7.Directory(\"cs141\")",
                 "d.add_file(hw7.File(\"hw7.py\", \"print(42)\"))",
                 "d.touch(\"hw8.py\", \"# Recursion\", False)"]
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

        err_msg = None

        if len(d.files) != 2:
            err_msg = "New file not found"

        elif "hw7.py" not in d.files:
            err_msg = "\"hw7.py\" file not found"

        elif "hw8.py" not in d.files:
            err_msg = "\"hw8.py\" file not found"

        elif not result:
            err_msg = helpers.check_result(result, True)

        else:
            f = d.files["hw7.py"]
            err_msg = check_file(f, "hw7.py", "print(42)")

        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

def test_cp1():

    try:
        fs, steps = fs1()

        steps = steps + ["fs.cp(\"notes.txt\", \"cs141\", \"cs142\")"]
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

        err_msg = None

        result = fs.cp("notes.txt", "cs141", "cs142")

        if result:
            err_msg = helpers.check_result(result, False)
            err_msg += "No directory named \"cs141\""

        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

def test_cp2():

    try:
        fs, steps = fs6()

        steps = steps + ["fs.cp(\"notes.txt\", \"cs141\", \"cs142\")"]
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

        err_msg = None

        result = fs.cp("notes.txt", "cs141", "cs142")

        if result:
            err_msg = helpers.check_result(result, False)
            err_msg += "No directory named \"cs142\""

        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

def test_cp3():

    try:
        fs, steps = fs6()

        steps = steps + ["fs.cp(\"notes.txt\", \"cs142\", \"cs141\")"]
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

        err_msg = None

        result = fs.cp("notes.txt", "cs142", "cs141")

        if result:
            err_msg = helpers.check_result(result, False)
            err_msg += "No directory named \"cs142\""

        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

def test_cp4():

    try:
        fs, steps = fs6()

        steps = steps + ["fs.cp(\"notes.txt\", \"cs142\", \"cs141\")"]
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

        err_msg = None

        result = fs.cp("notes.txt", "cs142", "cs141")

        if result:
            err_msg = helpers.check_result(result, False)
            err_msg += "No directory named \"cs142\""

        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

def test_cp5():

    try:
        fs, steps = fs6()

        steps = steps + ["fs.cp(\"my_notes.txt\", \"cs141\", \"chem101\")"]
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

        err_msg = None

        result = fs.cp("my_notes.txt", "cs141", "chem101")

        if result:
            err_msg = helpers.check_result(result, False)
            err_msg += "No file named \"my_notes.txt\" in \"cs141\""

        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_cp6():

    try:
        fs, steps = fs6()

        steps = steps + ["fs.cp(\"notes.txt\", \"cs141\", \"chem101\")"]
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

        err_msg = None

        result = fs.cp("notes.txt", "cs141", "chem101")

        if not result:
            err_msg = helpers.check_result(result, True)

        elif "notes.txt" not in fs.dirs["chem101"].files:
            err_msg = "New file not found in \"chem101\""

        elif "notes.txt" not in fs.dirs["cs141"].files:
            err_msg = "\"notes.txt\" not found in \"cs141\""

        else:
            f = fs.dirs["chem101"].files["notes.txt"]
            err_msg = check_file(f, "notes.txt", "CS 141 notes")

        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_cp7():

    try:
        fs, steps = fs6()

        steps = steps + ["fs.cp(\"notes.txt\", \"cs141\", \"math151\")"]
        recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

        err_msg = None

        result = fs.cp("notes.txt", "cs141", "math151")

        if not result:
            err_msg = helpers.check_result(result, True)

        elif "notes.txt" not in fs.dirs["math151"].files:
            err_msg = "New file not found in \"math151\""

        elif "notes.txt" not in fs.dirs["cs141"].files:
            err_msg = "\"notes.txt\" not found in \"cs141\""

        elif "notes.txt" in fs.dirs["chem101"].files:
            err_msg = "Extra \"notes.txt\" not found in \"chem101\""

        else:
            f = fs.dirs["math151"].files["notes.txt"]
            err_msg = check_file(f, "notes.txt", "CS 141 notes")

        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

# No directories, no files
def fs0():
    fs = hw7.FileSystem()
    steps = ["fs = hw7.FileSystem()"]

    return fs, steps

# One directory, no files
def fs1():
    fs = hw7.FileSystem()
    d = hw7.Directory("cs141")
    fs.add_directory(d)

    steps = ["fs = hw7.FileSystem()",
             "d = hw7.Directory(\"cs141\")",
             "fs.add_directory(d)"]

    return fs, steps

# One directory, one file
def fs2():
    fs = hw7.FileSystem()
    d = hw7.Directory("cs141")
    f = hw7.File("notes.txt", "Classes/objects")
    d.add_file(f)
    fs.add_directory(d)

    steps = ["fs = hw7.FileSystem()",
             "d = hw7.Directory(\"cs141\")",
             "f = hw7.File(\"notes.txt\", \"Classes/objects\")",
             "d.add_file(f)",
             "fs.add_directory(d)",]

    return fs, steps

# One directory, two files
def fs3():
    fs = hw7.FileSystem()
    d = hw7.Directory("cs141")
    f1 = hw7.File("notes.txt", "Classes/objects")
    f2 = hw7.File("hw1.py", "print()")
    d.add_file(f1)
    d.add_file(f2)
    fs.add_directory(d)

    steps = ["fs = hw7.FileSystem()",
             "d = hw7.Directory(\"cs141\")",
             "f1 = hw7.File(\"notes.txt\", \"Classes/objects\")",
             "f2 = hw7.File(\"hw1.py\", \"print()\")",
             "d.add_file(f1)",
             "d.add_file(f2)",
             "fs.add_directory(d)"]

    return fs, steps

# Two directories, one file each
def fs4():
    fs = hw7.FileSystem()

    d1 = hw7.Directory("cs141")
    f1 = hw7.File("notes.txt", "Classes/objects")
    d1.add_file(f1)
    fs.add_directory(d1)

    d2 = hw7.Directory("chem101")
    f2 = hw7.File("Lab1.pdf", "Displacement")
    d2.add_file(f2)
    fs.add_directory(d2)

    steps = ["fs = hw7.FileSystem()\n",
             "d1 = hw7.Directory(\"cs141\")",
             "f1 = hw7.File(\"notes.txt\", \"Classes/objects\")",
             "d1.add_file(f1)",
             "fs.add_directory(d1)\n",
             "d2 = hw7.Directory(\"chem101\")",
             "f2 = hw7.File(\"Lab1.pdf\", \"Displacement\")",
             "d2.add_file(f2)",
             "fs.add_directory(d2)"]

    return fs, steps

# Two directories, one has one file, the other has two
def fs5():
    fs = hw7.FileSystem()

    d1 = hw7.Directory("cs141")
    f1 = hw7.File("notes.txt", "Classes/objects")
    f2 = hw7.File("hw1.py", "print()")
    d1.add_file(f1)
    d1.add_file(f2)
    fs.add_directory(d1)

    d2 = hw7.Directory("chem101")
    f3 = hw7.File("Lab1.pdf", "Displacement")
    d2.add_file(f3)
    fs.add_directory(d2)

    steps = ["fs = hw7.FileSystem()\n",

             "d1 = hw7.Directory(\"cs141\")",
             "f1 = hw7.File(\"notes.txt\", \"Classes/objects\")",
             "f2 = hw7.File(\"hw1.py\", \"print()\")",
             "d1.add_file(f1)",
             "d1.add_file(f2)",
             "fs.add_directory(d1)\n",

             "d2 = hw7.Directory(\"chem101\")",
             "f3 = hw7.File(\"Lab1.pdf\", \"Displacement\")",
             "d2.add_file(f3)",
             "fs.add_directory(d2)"]

    return fs, steps

def fs6():

    d1 = hw7.Directory("cs141")
    f1 = hw7.File("notes.txt", "CS 141 notes")
    f2 = hw7.File("hw7.py", "import hw7")

    d1.add_file(f1)
    d1.add_file(f2)
    d2 = hw7.Directory("math151")
    f3 = hw7.File("notes.txt", "Calc 1")
    d2.add_file(f3)

    d3 = hw7.Directory("chem101")
    f4 = hw7.File("Lab1.pdf", "Lab 1: Displacement")
    f5 = hw7.File("Lab2.pdf", "Lab 2: Bunsen Burners")
    d3.add_file(f4)
    d3.add_file(f5)

    fs = hw7.FileSystem()
    fs.add_directory(d1)
    fs.add_directory(d2)
    fs.add_directory(d3)

    steps = ["from example import fs"]

    return fs, steps
