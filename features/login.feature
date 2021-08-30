Feature: Login

Background:
Given I am in the login page
And if Im logged in, I should logout

Scenario: after login with correct credentials should be redirected to main page
Given I am in the login page
When I login with "correct" credentials
Then I should be redirected to the main page


