# TEST QA ABINBEV

## Automation of BOL email provider

### Requirements
* python3
* Google Chrome
* chromedriver

### Setting up your environment

1. First I advise to create a python virtual environment to install the python libraries used in this project:
```
python3 -m venv .venv
```
and to activate the virtual env:
```
source .venv/bin/activate
```

2. After that, you will need to install the requirements:
```
pip install -r requirements.txt
```

3. If you nerver used selenium with Chrome before, you will need to download de chromedriver
https://chromedriver.chromium.org/downloads

4. After the download, you'll need the chromedriver to be in your System's PATH.
To add chromedriver to PATH follow the instructions on this link: https://www.studytonight.com/post/how-to-set-path-environment-variable

5. BOL email provider has a Captcha when the user logs in to try to avoid automations. To bypass this problem , you will need to open Google Chrome in the terminal (or cmd) with the following command on Mac:

```
'Google Chrome' --remote-debugging-port=9222 --user-data-dir="~/any/path/ChromeProfile"
```
on Linux:

```
'google-chrome --remote-debugging-port=9222 --user-data-dir="~/any/path/ChromeProfile"
```
<br>
* `--remote-debugging-port=9222` This will open the browser on port 9222, where the webdriver will be listening and be able to take control of the session when the test runs.
<br>
* `--user-data-dir="~/any/path/ChromeProfile"` this will create a new ChromeProfile in the path provided. This is needed so Chrome will open as if it was the first time it is being used.

By opening Google Chrome this way the browser won't know it is beeing controlled by a computer when selenium takes over the session and the captcha will not show up.

To be able to run the tests you will also need to configure your @bol username and password and the destination email in the behave.ini file. Example:
```
username = myusername
password = mypassword
destination_email = test@test.com
```

### Runing the tests
To run all the scenarios for every feature just type `behave` when in the root of the project

### Reports
After runing the tests, a folder called reports will be created with the reports of the tests separated by feature
