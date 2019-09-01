import smtplib
smtpObj =smtplib.SMTP('smtp.gmail.com',587)
smtpObj.ehlo()
smtpObj.starttls()
#SenderEmail=input("Please Enter your Email Address\n")
password=input("Please Enter your Password\n")
#RecipientEmail=input("Please Enter the Recipient's Email" )
smtpObj.login('ajaykhalsa.ak@gmail.com',password)
smtpObj.sendmail('ajaykhalsa.ak@gmail.com','2018.ajay.khalsa@ves.ac.in',
                'Subject:Test on Sublime .\n Hi ')
smtpObj.quit()
