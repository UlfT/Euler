"""" Test class for the utility function timer_decorator"""
from nose2.tools import such
import nose2
from src.tools import timer_decorator

with such.A('TOOLS - Timer decorator') as it:
    @it.should('return the correct value even though it is wrapped')
    def test_return_value():
        """ Tests that the correct return value is still returned"""
        wrapped_function = timer_decorator.wrap(lambda: 42)
        assert wrapped_function() == 42
    @it.should('Report the correct time the call took')
    def test_timing():
        """ Waits for wait_seconds seconds and checks that the correct time is reported """
        import time
        import io
        from contextlib import redirect_stdout
        wait_seconds = 2
        wrapped_function = timer_decorator.wrap(time.sleep)

        file_handle = io.StringIO()
        with redirect_stdout(file_handle):
            wrapped_function(wait_seconds)
        caught_message = file_handle.getvalue()
        is_correct_message = caught_message.startswith(
            "Total running time was {0}.0".format(wait_seconds))
        assert is_correct_message, "Incorrect message, got {0}".format(caught_message)

it.createTests(globals())

if __name__ == '__main__':
    nose2.main() # pragma: no cover
