import subprocess
import json
from getpass import getpass
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time

def __auth_cisco_vpn__(username, pin, domain):
    # Assign cmd
    symantec_otp = input("Input Symantec OTP")

    credentials = "printf '" + username + "\\n" + pin + "\\n" + symantec_otp + "\\ny'"
    vpn_cmd = "/opt/cisco/anyconnect/bin/vpn -s connect '" + domain + "'"
    cmd = credentials + " | " + vpn_cmd

    # Command Execution
    print("Executing Command: \n" + cmd)
    subprocess.Popen(cmd,
                     shell=True,
                     executable="/bin/bash",
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE).communicate()

def ise_login(username, password, link):
    opts = Options()
    opts.headless = False
    browser = Firefox(options=opts)
    browser.get(link)
    time.sleep(2)

    username = browser.find_element_by_id("dijit_form_TextBox_0")
    password = browser.find_element_by_id("dijit_form_TextBox_1")
    submit   = browser.find_element_by_id("loginPage_loginSubmit")

    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)
    submit.click()

    time.sleep(13)

    browser.find_element_by_id("carousel-next").click()