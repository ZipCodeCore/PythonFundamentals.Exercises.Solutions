import logging


def single_handler():
    try:
        10 / 0
    except ZeroDivisionError as error:
        logging.error(error)


def all_is_well():
    try:
        pass
    except Exception as error:
        logging.error(error)
    else:
        logging.warning("No issues were encountered.")


def all_ends_well():
    try:
        pass
    except Exception as error:
        logging.error(error)
    finally:
        logging.warning("Issues may or may not have been encountered. Either way, they will be handled here.")


def multi_handler():
    try:
        raise PermissionError()
    except FileNotFoundError as error:
        logging.error(error)
    except PermissionError as error:
        logging.error(error)
    except Exception as error:
        logging.error(error)


def base_handler():
    try:
        raise FileNotFoundError()
    except OSError as error:
        logging.error(error)


def tuple_handler():
    try:
        raise FileNotFoundError
    except (FileNotFoundError, PermissionError) as error:
        logging.info(error)


