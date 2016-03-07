# f4py

Functional (algebraic) data types for python

## Classes

 - `f4py.Maybe`
 - `f4py.Either`
 - `f4py.Try`
 - `f4py.Monad`
 - `f4py.exception.NotPresentException`

## Usage

```python

from f4py import \
    maybe,\
    just,\
    nothing,\
    either,\
    left,\
    right,\
    attempt,\
    success,\
    failure

my_value = maybe(receive())
nonable_value = maybe(get_from_somewhere())
result = nonable_value\
    .map(extract_something)\
    .filter(out_something)\
    .if_absent(my_value)\
    .flat_compute_if_absent(my_maybe_producer)\
    .or_else(5)

computed_result = attempt(do_some_work)\
    .map(convert_to_something)
    .fallback(do_some_other_work)
    .handle_error(error_handler)
    .or_else(result)

one_or_other = either(get_tuple())\
    .map(side_independent_converter)
    .bimap(left_mapper, right_mapper)

any_result = one_or_other.unpack()

if one_or_other.is_left():
    print('It was left!')
else:
    print('It was right!')

r_value = one_or_other.get_right().if_absent(just(5))
l_value = one_or_other.get_left().or_else_compute(lambda: 10)
```

That's it. For more use `Ctrl` + `Space` :)

## License

Library is licensed under MIT license.
