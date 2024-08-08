import logging
import inspect
def get_logger():
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    filehandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)
    return logger