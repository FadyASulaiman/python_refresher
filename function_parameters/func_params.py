# positional and Keyword arguments

def func(pos_only, /, pos_or_kwd, *, kwd_only):
    pass

func(1, 2, kwd_only=3)        # Valid
func(1, pos_or_kwd=2, kwd_only=3)  # Valid
func(pos_only=1, pos_or_kwd=2, kwd_only=3)  # ERROR



# ***args and kwargs

# *args captures excess positional arguments as a tuple
# **kwargs captures excess keyword arguments as a dictionary