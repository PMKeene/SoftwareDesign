"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""

class Time(object):
    """Represents the time of day.
       
    attributes: hour, minute, second
    """
#oh, apparently its a formatting sequence about interger length and zeros...
def print_time(t):
    print '%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second)


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def time_to_int(time):
    """Computes the number of seconds since midnight.

    time: Time object.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def add_times(t1, t2):
    """Adds two time objects."""
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def valid_time(time):
    """Checks whether a Time object satisfies the invariants."""
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def main():
    # if a movie starts at noon...
    noon_time = Time()
    noon_time.hour = 12
    noon_time.minute = 0
    noon_time.second = 0

    print 'Starts at',
    print_time(noon_time)

    # and the run time of the movie is 109 minutes...
    movie_minutes = 109
    run_time = int_to_time(movie_minutes * 60)
    print 'Run time',
    print_time(run_time)

    # what time does the movie end?
    end_time = add_times(noon_time, run_time)
    print 'Ends at',
    print_time(end_time)

if __name__ == '__main__':
    main()
