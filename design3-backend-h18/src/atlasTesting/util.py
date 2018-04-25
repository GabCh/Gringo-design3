def function_which_raises_an_exception(exception: Exception):
    """Use like this: myMock.functionToMock = lambda: function_which_raises_an_exception(MyWonkyException())"""
    raise exception
