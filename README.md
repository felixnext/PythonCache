# PythonCache

Simple Library to do Python Caching

## Getting Started

The library is easy to use, just load a cache and provide it some data.

```python
import pandas as pd
from pycache import PandaFileCache

cache = PandaFileCache("./cache_folder")
df = pd.read_csv("test.csv")

cache["my_cool_data"] = df

# ... somewhere later (even after restart) ...

df_new = cache["my_cool_data"]
```

This allows you to quickly buffer data to files and restore them later on.