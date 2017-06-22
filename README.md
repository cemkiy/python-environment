# Python-Environment

Easy to use python shell environment management

  - works with directly shell
  - autoload ".env" file

### Version
1.0

### Installation

You could install via pip.

```sh
$ pip install python_environment
```

### How To Use

```python
# init func will autoload your .env file
env = Environment()
env.get_env_or_default("db_url","")
env.set_a_variable_to_environment("key","value")
```
