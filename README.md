# panda-pytest-assertions

Complex assertions that can be used when writing test with pytest.

## `assert_context`

This context manager ensures that a `with` block behaves according to expectations. It verifies whether an exception of a specific type was raised within the block and whether the result of the block (settable by the user) is equal to the expected value.

### Parameters

The context manager defines three optional keyword parameters: `exception`, `result`, and `behaviour`. The parameter pair (`exception`, `result`) is mutually exclusive with the `behaviour` parameter. If `behaviour` is set, the other parameters must remain unset.

#### `exception` parameter

* If the `exception` parameter is set, the `with` block is expected to raise an exception of the provided type.
* If the `exception` parameter is NOT set, the `with` block is expected NOT to raise any exceptions.

##### Code not raising any exceptions

```python
with assert_context():
    ...

with assert_context(exception=ValueError):
    raise ValueError
```

##### Code raising `ValueError`

```python
with assert_context():
    raise ValueError


with assert_context(exception=TypeError):
    raise ValueError
```

##### Code calling `pytest.fail` (as `pytest.raises(ValueError)` would)

```python
with assert_context(exception=ValueError):
    ...
```

#### `result` parameter

* If the `result` parameter is set, its value is expected to be equal to the result of the `with` block.
* The `with` block result is set using the `set` method of an object yielded by the context manager.
* The comparison is performed using the `==` operator, with the `result` argument on the left side.
* If the `result` parameter is NOT set, the `set` method of the yielded object is expected not to be called at all.

##### Code not raising any exceptions

```python
with assert_context() as context:
    ...

with assert_context(result='something') as context:
    context.set('something')
```

##### Code raising `AssertionError`

```python
with assert_context() as context:
    context.set('else')

with assert_context(result='something') as context:
    context.set('else')

with assert_context(result='something') as context:
    ...
```

#### Combining `exception` and `result` parameters

* Both `exception` and `result` parameters can be set simultaneously to check more complex code.

##### Code not raising any exceptions

```python
with assert_context(exception=ValueError, result='something') as context:
    context.set('something')
    raise ValueError
```

#### `behaviour` parameter

* If `behaviour` is set to an exception type, it is equivalent to setting `exception` to the same value, and leaving `result` unset.
* If `behaviour` is set to any other value, it is treated as the value of `result`, and the `exception` parameter remains unset.

##### Code not raising any exceptions

```python
with assert_context(behaviour=ValueError) as context:
    raise ValueError

with assert_context(result='something') as context:
    context.set('something')
```

##### Code raising exceptions

```python
with assert_context(behaviour=ValueError) as context:
    context.set('else')

with assert_context(result='something') as context:
    raise ValueError
```

## Additional documentation

[Development documentation](README-DEV.md)

[Changelog](CHANGELOG.md)
