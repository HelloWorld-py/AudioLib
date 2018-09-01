error = None

try:
    from .Stream import Stream
    from .Errors import FormatError
except ImportError as e:
    error = e  # str(e.args[0])

if error:
    raise ImportError(error)
