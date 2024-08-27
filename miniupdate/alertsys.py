import smtplib
def alert(mail):
    server =smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login('sfacechecker@gmail.com',"wdrbvzdidynsmrgi")
    server.sendmail("sfacechecker@gmail.com",mail,"email is from facesupport invalid authorisation has occured")
    print("mailsend")
