PROJECT AUTOMATA. OR HOW I LEARNT TO LOVE SELENIUM

In the context of my journey as a tester, I needed to learn how to use Selenium.

I decided that a practical application of the framework would do wonders for the development of my skills. 

This is just an exemplificative and experimentative project, trying to see what works, what doesn't and what could be better.

As per requirements, the language is going to be Python and python-related libraries. You can find the complete list of them in the file "requirements.txt"

The framework read from a .env file in order to get to the website's URL and list the credentials available. The .env would read as follows:

 BASE_URL = https://www.saucedemo.com

    APP_USERNAME_VALID = standard_user
    APP_USERNAME_LOCKED_OUT = locked_out_user
    APP_USERNAME_PROBLEM = problem_user
    APP_USERNAME_GLITCH = performance_glitch_user
    APP_USERNAME_ERROR = error_user
    APP_USERNAME_VISUAL = visual_user

    PASSKEY = secret_sauce