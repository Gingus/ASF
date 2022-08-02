from pytest_bdd import scenario, given, when, then

from CodeTest.cucumbers import CucumberBasket


@scenario('C:\\Users\\gingu\\PycharmProjects\\asf\\CodeTest\\tests\\features\\cucumbers.feature',
          'Add cucumbers to a basket')
def test_add():
    pass


@given("the basket has 2 cucumbers")
def basket():
    return CucumberBasket(initial_count=2)
    raise NotImplementedError(u'STEP: Given the basket has 2 cucumbers')


@when("4 cucumbers are added to the basket")
def add_cucumbers(basket):
    basket.add(4)
    raise NotImplementedError(u'STEP: When 4 cucumbers are added to the basket')


@then("the basket contains 6 cucumbers")
def basket_has_total(basket):
    assert basket.count == 6
    raise NotImplementedError(u'STEP: Then the basket contains 6 cucumbers')