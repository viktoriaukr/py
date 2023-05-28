def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    lst2 = []
    for i in lst:
        if(bool(i)):
            lst2.append(i)
    return lst2