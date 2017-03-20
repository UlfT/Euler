""" Functions to decorate/wrap a function and add a timer to it"""
import time
def wrap(func):
    """ Decorate func, return a new function that adds timing printouts"""
    def timed(*args, **kwargs):
        """ Add a timer and print what the total running time was when run"""
        start = time.time()
        ret = func(*args, **kwargs)
        stop = time.time()
        print("Total running time was {0} seconds".format(stop - start))
        print("Return value was {0}".format(ret))
        return ret
    return timed
