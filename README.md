# minimapreduce

A simple framework for MapReduce processing on a single machine.

## Usage

```bash
cd sample
cat corpus.txt | python map.py | sort | python reduce.py
```

## Mapper

```python
def mapper(stream, map_function, emit=emit_console)
```

### Arguments

| Argument | Description |
|---|---|
| stream | Input stream. Must be iterable. |
| map_function | Function called to map each input stream entry. |
| emit | Function called to output map_function result. Default emit_console outputs to console. |

#### map_function Function

```python
def map_function(line, emit)
```

##### Arguments

| Argument | Description |
|---|---|
| line | Line to process. |
| emit | Function called to output result. |

#### emit Function

```python
def emit(key, value=None)
```

##### Arguments

| Argument | Description |
|---|---|
| key | Key. |
| value | Value associated to key. |

## Reducer

```python
def reducer(stream, reduce_function, emit=emit_console)
```

### Arguments

| Argument | Description |
|---|---|
| stream | Input stream. Must be iterable. |
| reduce_function | Function called to reduce each input stream entry. |
| emit | Function called to output reduce_function result. |

#### reduce_function Function

```python
def reduce(key, values)
```

##### Arguments

| Argument | Description |
|---|---|
| key | Key. |
| value | Array of values associated to key. |
