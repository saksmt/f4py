# Either

Represents tuple with one element omitted

`Either :: Left(a) | Right(b)`

## Construction

```python
left(value)  # or Either.left(value)
right(value)  # or Either.right(value)
either(tuple_with_one_element_omitted)  # or Either.of(tuple_with_one_element_omitted)
```

## Methods

 - `is_left()` - check whether value is left
 - `is_right()` - check whether value is right
 - `get_left()` - get `maybe` of left
 - `get_right()` - get `maybe` of right
 - `map(mapper)` - apply mapper to value and return `either` of same side, e.g. `Left -> Left` and `Right -> Right`
 - `bimap(left_mapper, right_mapper)` - apply mapper according to side and return `either` of same side, e.g. `Left(a) -> Left(left_mapper(a))` and so on
 - `flat_map(mapper)` - apply mapper to value and return result, mapper should return `either`
 - `flat_bimap(left_mapper, right_mapper)` - apply mapper according to side and return result, mapper should return `either`, e.g. `Left(a) -> left_mapper(a)`
 - `unpack()` - get underlying value
 - `peek(mapper)` - apply mapper according to side and return self, e.g. `Left(a) -> Left(a)`
 - `flip()` - flip either, if was `Left` would be `Right` and so on, e.g. `Left(a) -> Right(a)` and `Right(b) -> Left(b)`
