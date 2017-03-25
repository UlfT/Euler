"""" Test class for the utility function timer_decorator"""
import unittest
import src.tools.timer_decorator

class TestTimer(unittest.TestCase):
    """" Test class for the utility function timer_decorator"""
    def test_return_value(self):
        """ Tests that the correct return value is still returned"""
        wrapped_function = src.tools.timer_decorator.wrap(lambda: 42)
        self.assertEqual(wrapped_function(), 42)

    def test_timing(self):
        """ Waits for wait_seconds seconds and checks that the correct time is reported """
        import time
        import io
        from contextlib import redirect_stdout
        wait_seconds = 2
        wrapped_function = src.tools.timer_decorator.wrap(time.sleep)

        file_handle = io.StringIO()
        with redirect_stdout(file_handle):
            wrapped_function(wait_seconds)
        caught_message = file_handle.getvalue()

        is_correct_message = caught_message.startswith(
            "Total running time was {0}.0".format(wait_seconds))
        self.assertTrue(is_correct_message, "Incorrect message, got {0}".format(caught_message))


if __name__ == '__main__':
    unittest.main() # pragma: no cover
