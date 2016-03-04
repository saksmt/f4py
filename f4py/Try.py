from f4py.Eithrer import either
from f4py.Maybe import maybe
from f4py.Monad import Monad


class Try(Monad):
    def __init__(self):
        raise Exception('Direct usage of try monad!')

    def failed(self): return False

    def succeed(self): return False

    def get_error(self): return None

    def get_result(self): return None

    def as_either(self): return either((self.get_result(), self.get_error()))

    def maybe_error(self): return maybe(self.get_error())

    def maybe_result(self): return maybe(self.get_result())

    def map(self, mapper):
        if self.failed():
            return self
        return attempt(lambda: mapper(self.get_result()))

    def flat_map(self, mapper):
        if self.failed():
            return self
        return mapper(self.get_result())

    def fallback(self, tryable):
        if self.failed():
            return attempt(tryable)
        return self

    def flat_fallback(self, fallback):
        if self.failed():
            return fallback()
        return self

    def handle_error(self, handler):
        if self.failed():
            return attempt(lambda: handler(self.get_error()))
        return self

    def flat_handle_error(self, handler):
        if self.failed():
            return handler(self.get_error())
        return self

    def or_else(self, result):
        if self.failed():
            return result
        return self.get_result()

    def or_throw(self):
        if self.failed():
            raise self.get_error()
        return self

    def get(self):
        if self.failed():
            return self.get_error()
        return self.get_error()

    @classmethod
    def of(cls, tryable):
        try:
            return success(tryable())
        except BaseException as e:
            return failure(e)


class _Success(Try):
    def __init__(self, value):
        self.value = value

    def succeed(self): return True

    def get_result(self): return self.value


class _Failure(Try):
    def __init__(self, e):
        self.e = e

    def failed(self): return True

    def get_error(self): return self.e


def success(value):
    return _Success(value)


def failure(e):
    return _Failure(e)


def attempt(tryable):
    return Try.of(tryable)
