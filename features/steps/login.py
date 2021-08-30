from behave import given, when, then, step
from modules.po_login_page import LoginPage
from modules.po_home_page import HomePage


@given("I am in the login page")
def go_to_login_page(context):
    context.logged = False
    context.driver.get("https://email.bol.uol.com.br/")
    hp = HomePage(context.driver)
    if hp.is_logged_in(5, context.username):
        context.logged = True


@when('I login with "{condition}" credentials')
def do_login(context, condition):
    lp = LoginPage(context.driver)
    hp = HomePage(context.driver)
    if hp.is_logged_in(5, context.username):
        context.logged = True
        return

    lp.do_login(context.username, context.password)


@then("I should be redirected to the main page")
def redirect_to_main_page(context):
    hp = HomePage(context.driver)
    if context.logged:
        return
    assert hp.is_logged_in(20, context.username)


@given("if Im logged in, I should logout")
def account_logout(context):
    hp = HomePage(context.driver)
    if context.logged:
        hp.logout()
