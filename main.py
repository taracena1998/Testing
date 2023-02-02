from math import floor
def str_to_int(string, round_down=True):
    """
    Parses a string number into an integer, optionally converting to a float
    and rounding down.
    """
    error_msg = "Unable to convert to integer: '%s'"% str(string)
    try:
        integer = float(string.replace(',', '.'))
    except AttributeError:
        # this might be a integer already, so try to use it, otherwise raise
        # the original exception
        if isinstance(string, (int, float)):
            integer = string
        else:
            raise RuntimeError(error_msg)
    except (TypeError, ValueError):
        logger.exception(error_msg)
    if round_down:
        integer = floor(integer)
    else:
        integer = round(integer)
    return int(integer)