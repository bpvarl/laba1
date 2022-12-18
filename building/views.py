from django.shortcuts import render
import smtplib
from email.mime.text import MIMEText


# Create your views here.
def index(request):

    if request.POST.get("phone_number"):
        msg_get(request.POST.get("login"), str(request.POST.get("phone_number")))

    return render(request, 'building/index.html')

def msg_get(user_name, user_phone):
    email_sender = "ecece@internet.ru"
    password = "tDiU5LjWkejRskbvNavi"
    email_getter = "skrudji02@mail.ru"

    smtp_server = smtplib.SMTP("smtp.mail.ru", 587)
    smtp_server.starttls()

    msg = MIMEText('Имя:' + str(user_name) + " " + "Телефон:" + str(user_phone))
    msg["Subject"] = "Cогласовать проект"
    smtp_server.login(email_sender, password)
    smtp_server.sendmail(email_sender, email_getter, msg.as_string())