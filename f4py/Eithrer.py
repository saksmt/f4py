from f4py.Maybe import maybe
from f4py.Monad import Monad


class Either(Monad):
    def __init__(self):
        raise Exception('Direct usage of either monad!')

    def is_left(self): return False

    def is_right(self): return False

    def get_left(self): return maybe(self._get_left())

    def get_right(self): return maybe(self._get_right())

    def map(self, mapper):
        if self.is_left():
            return Left(mapper(self._get_left()))
        return Right(mapper(self._get_right()))

    def bimap(self, left_mapper, right_mapper):
        return self.map(left_mapper if self.is_left() else right_mapper)

    def flat_map(self, mapper):
        return mapper(self._get_right() if self.is_left() else self._get_right())

    def flat_bimap(self, left_mapper, right_mapper):
        return self.flat_map(left_mapper if self.is_left() else right_mapper)

    def get(self):
        if self.is_left():
            return self._get_left()
        return self._get_right()

    def flip(self):
        if self.is_left():
            return right(self._get_left())
        return left(self._get_right())

    @classmethod
    def left(cls, value):
        return Left(value)

    @classmethod
    def right(cls, value):
        return Right(value)

    @classmethod
    def of(cls, pair):
        assert isinstance(pair, tuple)
        if pair[0] is not None:
            return left(pair[0])
        return right(pair[1])

    def _get_left(self): return None

    def _get_right(self): return None


class Left(Either):
    def __init__(self, value):
        self.value = value

    def is_left(self): return True

    def _get_left(self): return self.value


class Right(Either):

    def __init__(self, value):
        self.value = value

    def is_right(self): return True

    def _get_right(self): return self.value


def left(value): return Either.left(value)


def right(value): return Either.right(value)


def either(pair): return Either.of(pair)
