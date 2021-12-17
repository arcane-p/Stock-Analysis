import logging


class PL():

    def __init__(self, print_level: int = 2, log_filename: str = "logfile"):
        # Debug - 0 - Detailed information, typically of interest only when diagnosing problems.
        # Info - 1 - Confirmation that things are working as expected.
        # WARNING - 2 - An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
        # ERROR - 3 - Due to a more serious problem, the software has not been able to perform some function.
        # CRITICAL - 4 - A serious error, indicating that the program itself may be unable to continue running.

        if log_filename[-4:] != ".log":
            log_filename += ".log"

        logging.basicConfig(filename=log_filename, encoding='utf-8', level=logging.DEBUG, format='%(asctime)s | %(levelname)s | %(message)s')
        logging.debug("FILE CREATED")

        try:  # may not be needed if :int only allows interger input
            self.print_level = int(print_level)
        except ValueError:
            return False

        if int(self.print_level) > 4 or int(self.print_level) < 0:
            return False

    def print(self, message: str, significance: int):
        """[summary]

        Args:
            message (str): [description]
            significance (int): 0 - Debug, 1 - Info, 2 - Warn, 3 - Error, 4 - Fatal
        """
        self.message = message

        if significance == 0:
            logging.debug(self.message)
        if significance == 1:
            logging.info(self.message)
        if significance == 2:
            logging.warning(self.message)
        if significance == 3:
            logging.error(self.message)
        if significance == 4:
            logging.critical(self.message)

        if significance >= self.print_level:
            print(self.message)


# # Debug
# sig = int(input("sig: "))
# PL = Print_Log(sig)
# for i in range(0,5):
#     PL.print(f"test ({i})", i)
