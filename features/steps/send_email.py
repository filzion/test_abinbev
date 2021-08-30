from behave import given, when, then, step
from modules.po_login_page import LoginPage
from modules.po_home_page import HomePage

@when(u"I click to compose an Email")
def compose_email(context):
    hp = HomePage(context.driver)
    element = hp.return_compose_email_element()
    context.driver.execute_script("arguments[0].click();", element)


@when(u'I set a "{condition}" destination Email')
def type_email_destination(context, condition):
    hp = HomePage(context.driver)
    if condition == "valid":
        hp.set_email_destination(context.destination_email)
    elif condition == "invalid":
        hp.set_email_destination("test123testcom")

   
@when(u"I set a subject for the Email")
def set_subject(context):
    hp = HomePage(context.driver)
    hp.set_email_subject("Subject")


@when(u"I type the body of the email")
def type_body(context):
    hp = HomePage(context.driver)
    hp.type_email_body("Hi, testing, testing")


@when(u"I send the Email")
def click_send(context):
    hp = HomePage(context.driver)
    hp.send_email()


@then(u'the notification should be: "{condition}"')
def check_notification(context, condition):
    hp = HomePage(context.driver)
    notification = hp.get_notification()
    if condition == "success":
        assert notification == "Seu e-mail foi enviado"
    elif condition == "failure":
        assert "Atenção Destinatários inválidos" in notification


@given("I am in the main page")
def go_to_main_page(context):
    hp = HomePage(context.driver)
    assert hp.is_logged_in(1, context.username)
