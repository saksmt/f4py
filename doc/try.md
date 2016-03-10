# Try

Represents result that may fail, almost same as `Either` except of semantics

`Try :: Success(a) | Failure(b)`

## Construction

```python
attempt(tryable)  # or Try.of(tryable), would be `Success` except of case when an exception raised
success(value)
failure(error)
```

## Methods

 - `succeed()` - check whether it's `Success`
 - `failed()` - check whether it's `Failure`
 - `as_either()` - convert to `either`, `Success -> Left`, `Failure -> Right`
 - `get_error()` - get maybe of `Failure` value
 - `get_result()` - get maybe of `Success` value
 - `map(mapper)` - if it's `Success` apply mapper to value inside of `attempt` and return result, otherwise does nothing
 - `flat_map(mapper)` - if it's `Success` apply mapper to value and return result, mapper should return `Try`
 - `fallback(tryable)` - does new attempt with `tryable` if was `Failure` and returns result
 - `flat_fallback(tryable)` - executes `tryable` if was `Failure` and returns result, `tryable` should return `Try`
 - `handle_error(handler)` - same as `fallback` except of that error would be passed as argument
 - `flat_handle_error(handler)` - same as `flat_fallback` except of that error would be passed as argument
 - `peek(mapper)` - if `Success` execute mapper on value and return self, otherwise does nothing
 - `on_success(mapper)` - alias to `peek`
 - `on_success_try(mapper)` - same as `on_success` except of that any exception would be silently ignored
 - `on_failure(mapper)` - same as `on_success` but for `Failure`
 - `on_failure_try(mapper)` - if `Failure` execute mapper on error and if any exception raised return failure with `CompositeException`, otherwise does nothing
 - `or_else(value)` - if `Failure` return `value` else return `result`
 - `or_throw()` - if `Failure` raise underlying error otherwise does nothing
 - `unpack()` - return underlying value, error for `Failure` or result for `Success`
