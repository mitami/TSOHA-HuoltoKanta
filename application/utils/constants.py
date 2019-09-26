import os

msg_only_admin = "Vain Admin voi suorittaa tämän toiminnon!"

def boolean_converter(value):
    if os.environ.get("HEROKU"):
        if value:
            return "TRUE"
        else:
            return "FALSE"
    else:
        if value:
            return 1
        else:
            return 0