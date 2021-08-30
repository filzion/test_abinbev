Feature: Send Email

Background:
    Given I am in the login page
    When I login with "correct" credentials
    Then I should be redirected to the main page

Scenario: email should be sent if destination email is valid
    Given I am in the main page
    When I click to compose an Email
    And I set a "valid" destination Email
    And I set a subject for the Email
    And I type the body of the email
    And I send the Email
    Then the notification should be: "succeess"


Scenario: email should not be sent if destination email is invalid
    Given I am in the main page
    When I click to compose an Email
    And I set a "invalid" destination Email
    And I set a subject for the Email
    And I type the body of the email
    And I send the Email
    Then the notification should be: "failure"
    