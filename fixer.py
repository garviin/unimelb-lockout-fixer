import subprocess

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