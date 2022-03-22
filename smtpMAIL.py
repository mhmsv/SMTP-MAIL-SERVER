import smtplib
message = """\
Subject: Ain't nothing but respect
 :)))
MAKE EMAILS GREAT AGAIN
This message is sent from Python."""

smtpObj = smtplib.SMTP('smtp.mail.yahoo.com', 587)
print(type(smtpObj))

res=smtpObj.ehlo()
if(250 in res):
    print("Sending the SMTP “Hello” Message")

res=smtpObj.starttls()
print("Starting TLS Encryption")
if(220 in res):
    print("sucseed")
password = input("Type your password and press enter: ")

try:
    res=smtpObj.login('mh_msv@yahoo.com',password)
    if (235 in res):
        print("Logging in to the SMTP Server")
except smtplib.SMTPAuthenticationError:
		print( bcolors.FAIL + '''Your Username or Password is incorrect, please try again using the correct credentials
		Or you need to enable less secure apps
		On Yahoo: https://login.yahoo.com/account/security?.scrumb=Tiby8TXUvJt#less-secure-apps
		''') + bcolors.ENDC
		sys.exit()

smtpObj.sendmail(' mh_msv@yahoo.com', ' amirali.mnj@gmail.com ',message)
print("email has been sent")

#fggsfliauyvghdco

smtpObj.quit()

