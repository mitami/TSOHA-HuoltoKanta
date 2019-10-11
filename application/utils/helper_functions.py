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
        return ['string_agg',
                '::character varying',
                ' GROUP BY action.id, target.id, location.id']
    return ['group_concat',
            '',
            '']