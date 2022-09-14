import os
import environ


env = environ.Env(
    DEBUG=(bool, True)
)
BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

print(BASE_DIR)
