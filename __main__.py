import os

from src.commands import create_zsh_config

user_home: str = os.path.expanduser("~")
create_zsh_config(user_home)
