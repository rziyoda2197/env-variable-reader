import os

def oling_environment_variable(nomi):
    qiymat = os.environ.get(nomi)
    if qiymat is None:
        raise ValueError(f"Environment variable '{nomi}' topilmadi")
    return qiymat

# Misol foydalanish:
print(oling_environment_variable('VARIABLE_NOMI'))
```

```python
import dotenv

def oling_environment_variable(nomi):
    dotenv.load_dotenv()
    qiymat = os.getenv(nomi)
    if qiymat is None:
        raise ValueError(f"Environment variable '{nomi}' topilmadi")
    return qiymat

# Misol foydalanish:
print(oling_environment_variable('VARIABLE_NOMI'))
```

```python
import environ

env = environ.Env()

def oling_environment_variable(nomi):
    qiymat = env(nomi)
    if qiymat is None:
        raise ValueError(f"Environment variable '{nomi}' topilmadi")
    return qiymat

# Misol foydalanish:
print(oling_environment_variable('VARIABLE_NOMI'))
