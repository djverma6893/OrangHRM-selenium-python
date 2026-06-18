import logging
import os
class LogGen:
    @staticmethod
    def loggen():
        filename= ".\\Logs\\Automation.log"
        format= "%(asctime)s:  %(levelname)s: %(message)s"
        datefmt="%d-%b-%y %H:%M:%S"
        filename= os.path.abspath(filename)
        print("hey buddy \n", filename)
        logging.basicConfig(filename=filename,format=format,datefmt=datefmt, level=logging.INFO, force= True)
        logger = logging.getLogger()
        # logger.setLevel(logging.INFO)
        return logger