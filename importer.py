import __main__ # noqa
# import the original file which imported this file.
import importlib
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def importer(module_name, *_module):
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        return logger.critical("Attempted to import module {}, Not found!".format(module_name))
    else:
        logger.info("Module {} imported successfully!".format(module_name))
        return module


__main__.__builtins__.__import__ = importer
