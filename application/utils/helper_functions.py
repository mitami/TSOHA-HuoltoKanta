import os

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

#siivoa
def determine_array_or_group(*argv):
    if os.environ.get("HEROKU"):

        groupby = ' GROUP BY'
        #Lisätään annetut sarakkeet GROUP BY lauseeseen
        for arg in argv:
            groupby = groupby + " " + arg + ","
        groupby = groupby[:-1]

        return ['string_agg',
                '::character varying',
                groupby]

    return ['group_concat',
            '',
            '']