import io
from contextlib import redirect_stdout


class Helper(object):
    @staticmethod
    def get_print_output(funkcja):
        """
        Przechwytuje wydruk z funkcji uzwajacej print()
        :param funkcja:
        :return:
        """
        memory_buffer = io.StringIO()
        with redirect_stdout(memory_buffer):
            funkcja()
            return memory_buffer.getvalue()
