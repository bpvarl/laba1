from django.shortcuts import render
import smtplib
from email.mime.text import MIMEText


# Create your views here.
def msg_get(user_name, user_phone):
    email_sender = "ecece@internet.ru"
    password = "tDiU5LjWkejRskbvNavi"
    email_getter = "rozovipavlin@mail.ru"

    smtp_server = smtplib.SMTP("smtp.mail.ru", 587)
    smtp_server.starttls()

    msg = MIMEText('Имя:' + str(user_name) + " " + "Телефон:" + str(user_phone))
    msg["Subject"] = "Консультация по предмету"
    smtp_server.login(email_sender, password)
    smtp_server.sendmail(email_sender, email_getter, msg.as_string())

def index(request):
    return render(request, 'building/index.html')

def lesson(request):
    return render(request, 'building/predmet.html')

def contact(request):
    if request.POST.get("phone_number"):
        msg_get(request.POST.get("login"), str(request.POST.get("phone_number")))
    return render(request, 'building/obr.html')

def chemical(request):
    return render(request, 'building/chem.html')

def english(request):
    return render(request, 'building/eng.html')

def math(request):
    return render(request, 'building/math.html')

def physics(request):
    return render(request, 'building/fis.html')

def biology(request):
    return render(request, 'building/bio.html')

def rus_language(request):
    return render(request, 'building/rus.html')
