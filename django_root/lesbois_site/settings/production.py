import environ

env = environ.Env()
env.read_env('.env.prod')

from .base import *

DEBUG = False
