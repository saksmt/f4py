# Maybe

Represents optional value

`Maybe :: Just(a) | Nothing`

## Construction

```python
maybe(unknown_value)  # or Maybe.of(unknown_value)
just(not_none_value)
nothing()
```

## Methods

 - `is_present()` - check whether it's `Just`
 - `is_nothing()` - check whether it's 'Nothing'
 - `map(mapper)` - apply mapper to value if it's present and return new maybe
 - `flat_map(mapper)` - same as previous except of that mapper should return maybe
 - `filter(predicate)` - call predicate on value, if result is true nothing happens, otherwise return `Nothing`
 - `or_else(value)` - returns content of monad if it's present, otherwise returns `value`
 - `or_else_compute(producer)` - same as previous except of that argument should be callable returning `value`
 - `if_absent(maybe)` - if value is present does nothing, otherwise returns argument, use-case - chaining of fallback maybe's
 - `compute_if_absent(producer)` - if value is present does nothing, otherwise returns result of `producer` wrapped in maybe
 - `flat_compute_if_absent(maybe_producer)` - same as previous, except of that `producer` should return maybe
 - `get()` - get underlying value, if not present raises `NotPresentException`
 - `peek(mapper)` - if value is present executes `mapper` on value and returns self, otherwise does nothing
 - `unpack()` - get underlying value, if not present returns `None`
