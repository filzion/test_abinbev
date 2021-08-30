from page_objects import PageElement, PageObject
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class HomePage(PageObject):
    input_to = PageElement(css='#fake_input__field-to')
    input_subject = PageElement(id_='field-subject')
    email_body = PageElement(id_='message-body')
    failure_notification = PageElement(xpath='//*[@id="notifications"]/div')
    btn_compose_email = PageElement(
        xpath='//*[@id="fc-side_menu-toggle"]/div/menu[1]'
    )
    btn_send_email = PageElement(
        xpath='/html/body/div[3]/div/div[1]/div[1]/form/div[4]/menu[1]'
    )
    btn_logout = PageElement(
        xpath='/html/body/div[3]/div/section[2]/div/div[1]/div[1]/div[2]/div/ul/li[4]/span'
    )

    input_to_css = '#fake_input__field-to'
    iframe_xpath = '//*[@id="cke_1_contents"]/iframe'
    failure_notification_xpath = '//*[@id="notifications"]/div'
    btn_compose_email_xpath = '//*[@id="fc-side_menu-toggle"]/div/menu[1]'
    btn_send_email_xpath = (
        "/html/body/div[3]/div/div[1]/div[1]/form/div[4]/menu[1]"
    )
    btn_logout_xpath = '/html/body/div[3]/div/section[2]/div/div[1]/div[1]/div[2]/div/ul/li[4]/span'
    title = 'Entrada - <username>@bol.com.br - BOL Mail'

    def return_compose_email_element(self):
        """
        Returns the element corresponding to the button to compose email.
        """
        wait = WebDriverWait(self.w, 10)
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, self.btn_compose_email_xpath)
            )
        )

        return self.btn_compose_email

    def set_email_destination(self, email):
        """
        Types the email destination in the "to" field
        """
        wait = WebDriverWait(self.w, 10)
        wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, self.input_to_css)
            )
        )
        self.input_to.send_keys(email)

    def set_email_subject(self, subject):
        """
        Types the email subject in the "subject" field
        """
        self.input_subject.send_keys(subject)

    def type_email_body(self, body):
        """
        Types the email subject in the "subject" field
        """        
        wait = WebDriverWait(self.w, 20)
        wait.until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.XPATH, self.iframe_xpath)
            )
        )
        self.email_body.send_keys(body)
        self.w.switch_to.default_content()

    def send_email(self):
        """
        Clicks on the "send email" button
        """
        wait = WebDriverWait(self.w, 10)
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.btn_send_email_xpath)
            )
        )
        self.btn_send_email.click()

    def is_logged_in(self, maximum_wait_time, username):
        """
        Checks if the user is logged in by looking at the title of the page
        """
        title = self.title.replace("<username>", username)
        wait = WebDriverWait(self.w, maximum_wait_time)
        try:
            wait.until(EC.title_is(title))
        except TimeoutException as exception:
            return False
        return True

    def get_notification(self):
        """
        Returns the alert/notification on the page
        """
        wait = WebDriverWait(self.w, 10)
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.failure_notification_xpath)
            )
        )

        return self.failure_notification.text

    def logout(self):
        """
        Clicks on the Logout button
        """
        wait = WebDriverWait(self.w, 10)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, self.btn_logout_xpath))
        )
        self.btn_logout.click()
