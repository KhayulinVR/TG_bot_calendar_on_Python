#TG_bot_calendar_on_Python    #by Hay_VR

def separate_callback_data(data):
    """ Separate the callback data"""
    return data.split(";")


def reformat_persian_date(date: str) -> str:
    """
        Replcae full space between words with half space (persian writing rules related)
    """
    return date