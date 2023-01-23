import solution as sol

def test_test01():
    result = sol.question01()
    result = result.lower().strip()
    if result[-1] == '.':
        result = result[:-1]
    expected = "knowing python is required for this course"
    assert expected == result

def test_test02():
    result = sol.question02()
    expected = "Nick Ivanov"
    assert expected == result

def test_test03():
    result = sol.question01()
    result = result.lower().strip()
    assert len(result) == 42 or len(result) == 43

def test_test04():
    result = sol.question01()
    expected_option1 = "Knowing Python is required for this course."
    expected_option2 = "Knowing Python is required for this course"
    assert expected_option1 == result or expected_option2 == result

def test_test05():
    result = sol.question02()
    expected_option1 = "Nick Ivanov"
    expected_option2 = "Nick Ivanov."
    assert expected_option1 == result or expected_option2 == result