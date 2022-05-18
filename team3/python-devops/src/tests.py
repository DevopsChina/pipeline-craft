import allure

try:
    from .utils import get_output
except:
    from utils import get_output


@allure.story('test')
def test_output():
    assert get_output()


