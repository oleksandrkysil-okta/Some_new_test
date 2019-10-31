import logging
import time

from global_helpers.constants import TIMEOUTS

LOGGER = logging.getLogger('logger')


def retry_on_exception(exception_name, retry_attempts=1, timeout=TIMEOUTS['nano']):
    """
    Handle exception in function and repeat function execution
    :param exception_name:
    :param retry_attempts:
    :param timeout:
    :return:
    """
    def wrap_creater(func):
        def wrapper(*args, **kwargs):
            for attempt in range(retry_attempts):
                try:
                    return func(*args, **kwargs)
                except exception_name as ex:
                    LOGGER.info("Receved %s exception, try again", ex.__class__.__name__)

        return wrapper
    return wrap_creater


def refresh_on_exception(exception_name, retry_attempts=1, timeout=TIMEOUTS['medium']):
    """
    Handle exception and refresh browser page and tries to repeat function steps
    :param exception_name:
    :param retry_attempts:
    :param timeout:
    :return:
    """
    def wrapper_creater(func):
        def wrapper(*args, **kwargs):
            for attempt in range(retry_attempts):
                try:
                    return func(*args, **kwargs)
                except exception_name as ex:
                    all_args = args + tuple(kwargs.values())
                    webdriver = next(filter(lambda drver: drver.__class__.__name__ == 'WebDriver', all_args), None)
                    LOGGER.info("Receved %s exception, try again", ex.__class__.__name__)
                    webdriver.refresh()
                    time.sleep(timeout)

        return wrapper
    return wrapper_creater
