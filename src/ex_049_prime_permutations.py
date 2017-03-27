"""
Prime permutations
Problem 49
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

def solve():
    from src.tools import primes_helper
    from itertools import takewhile, dropwhile
    primes = primes_helper.primes()
    candidates = {}
    for candidate in takewhile(lambda x: x < 10000, dropwhile(lambda x: x < 1000, primes)):
        key = ''.join(sorted(str(candidate)))
        if key != "1478": #hard coded exclude based on the exercise
            candidates.setdefault(key, []).append(candidate)

    for ans in candidates:
        if len(candidates[ans]) < 3:
             continue
        else:
            work_set = candidates[ans]
            for potential_answer in work_set:
                if potential_answer + 3330 in work_set and potential_answer + 2* 3330 in work_set:
                    ansstr = "{}{}{}".format(potential_answer, potential_answer+3330,
                                                        potential_answer+ 2 * 3330)
                    print("The answer is {}".format(ansstr))
                    return int(ansstr)

def run_main():
    """ Run the exercise as stated on the Euler website and wrapped in a timer"""
    from src.tools import timer_decorator
    wrapped_function = timer_decorator.wrap(solve)
    return wrapped_function()

if __name__ == "__main__":
    run_main()  # pragma: no cover