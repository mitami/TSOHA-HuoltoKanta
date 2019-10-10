import os

msg_only_admin = "Vain Admin voi suorittaa tämän toiminnon!"

msg_executor_name_length = "Käyttäjän nimen tulee olla 2-20 merkkiä pitkä!"
msg_executor_title_length = "Käyttäjän tittelin tulee olla enintään 30 merkkiä pitkä!"
msg_password_match = "Salasanojen on täsmättävä!"
msg_password_length = "Salasanan on oltava 4-20 merkkiä pitkä!"

msg_loc_name_length = "Sijainnin nimen tulee olla 2 - 30 merkkiä pitkä!"
msg_loc_no_name = "Sijainnin kenttä 'Nimi' on pakollinen!"

msg_target_name_length = "Kohteen nimen tulee olla 2 - 20 merkkiä pitkä!"
msg_target_no_name = "Kohteen kenttä 'Nimi' on pakollinen!"
msg_target_no_loc = "Kohteelle on annettava Sijainti!"

msg_action_name_length = "Tehtävän nimen tulee olla <= 20 merkkiä pitkä!"
msg_action_desc_length = "Tehtävän kuvauksen tulee olla <= 255 merkkiä pitkä! "

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