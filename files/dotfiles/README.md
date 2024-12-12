# dotfiles

This is all my dotfiles.

Symlink dotfiles files with stow:

```bash
# in this directory
stow -t $HOME .

# or directly in the home directory
stow -d ~/os/files/dotfiles -t $HOME .
```
