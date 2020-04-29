from selenium import webdriver
import time
from slacker import Slacker
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()

options = webdriver.FirefoxOptions()
options.add_argument('-headless')
Slack = Slacker("xoxp-50812565809-353866277617-431940859120-eb18fea89925182f5c95c05bf696c238")

Dundas1 = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver', firefox_options=options)

print("all Firefox setup is fine")
Dundas1.get("http://www.google.com")
print("Opened firefox with google page")

time.sleep(20)
print("waited for 20 secs")

Dundas1.quit()
print("Quit firefox")