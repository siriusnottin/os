# OS

This is a refactor of my initial bash cli project [devserver](https://github.com/siriusnottin/devserver) , that I started two years ago.

The goal is to have one interface to manage both my personal laptop, and my development server.

## Features

**Manage machines**

1. MacOS personal machine
2. Ubuntu dev server

## Setup

### Automate setup

- Configure system settings
- Keep track of installed applications and from where they were installed
  - App Store
  - Setapp
  - Homebrew
  - Manual download
- Dotfiles: sync (install, update, backup)
- Keep track of installed packages
  - Node packages
  - Python packages
- Manage `.ssh` keys

## Maintenance

- Keep the system up to date
- Maintain backups

### Do regular cleanups

- Brew doctor, cleanup
- Remove old versions of packages
- Remove old logs
- Remove old cache
- Remove old downloads
- Remove old backups
- Remove old dotfiles
- Remove old ssh keys
- Remove old packages

## Requirements

- Python 3.12
- Pyenv

## Development

```bash
pyenv virtualenv devserver
pyenv activate devserver
pip freeze > requirements.txt
pip install -r requirements.txt
```
