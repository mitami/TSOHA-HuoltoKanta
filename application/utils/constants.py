import os

msg_only_admin = "Vain Admin voi suorittaa tämän toiminnon!"
msg_loc_name_legth = "Sijainnin nimen tulee olla 2 - 30 merkkiä pitkä!"
msg_loc_no_name = "Sijainnin kenttä 'Nimi' on pakollinen!"

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