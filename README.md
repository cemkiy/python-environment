# Real Environment

Easy to use python shell environment management

  - works with directly shell
  - autoload ".env" file

### Version
1.0

### Installation

You could install with pip or pip3.

```sh
$ pip install real_environment
$ pip3 install real_environment
```

### How To Use

```python
from real_environment import real_environment
# init func will autoload your .env file
renv = real_environment.RealEnvironment()
renv.get_env_or_default("db_url","default_value_if_empty_returns")
renv.set_a_variable_to_environment("key","value")
renv.remove_a_variable_from_environment("key")
```
