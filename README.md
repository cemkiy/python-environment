# Python-Environment

Easy to use python environment management

  - works with dict objects
  - autoload ".env" file

### Version
0.0.1

### Installation

You can install via pip.

```sh
$ (sudo) pip install python_environment
```

### How To Use

```python
# init func will autoload your .env file
your_env = env()
print(your_env.enviroment_dict)
dict_obj = {}
dict_obj["X"] = 5
dict_obj["Y"] = "MALATYA"
dict_obj["Z"] = ["1", "2", "3"]
your_env.set_dict_to_env(dict_obj) # if dict_obj is none, default is your_env.enviroment_dict
print(your_env.enviroment_dict)
your_env.set_variable_to_env("T", "8")
print(your_env.enviroment_dict)
```
