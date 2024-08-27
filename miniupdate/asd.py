import database
import alertsys
password="xx"

if password=="xxx":
    print("noway")
else: 
    username="whiteved"
    mail=database.usermail(username)
    alertsys.alert(mail)
    print("failure ocuured")