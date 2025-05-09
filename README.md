# OS

The `os` repository is a CLI tool designed to help manage and automate the setup and configuration of your operating system. It includes scripts, dotfiles, and utilities to streamline the process of setting up a new machine or maintaining an existing one.

## Features

- **Dotfiles Management**: Easily manage and symlink your dotfiles using GNU Stow.
- **Zsh Configuration**: Preconfigured Zsh setup with plugins and custom scripts.
- **Vim Configuration**: Includes a preconfigured Vim setup for productivity.
- **macOS Utilities**: Scripts to list installed macOS applications and manage Homebrew packages.
- **Automation**: Automates repetitive tasks like creating symlinks, setting up configurations, and more.

## Structure

```plaintext
os/
├── dotfiles/          # Contains all configuration files for Zsh, Vim, Tmux, Git, etc.
├── src/               # Source code for CLI commands and utilities.
│   ├── commands/      # Specific commands for macOS and general utilities.
│   └── all/           # Shared commands across platforms.
├── output/            # Output files generated by the scripts.
├── logs/              # Log files for debugging and tracking.
├── setup.sh           # Script to set up the repository and CLI tool.
├── Makefile           # Automates symlink creation and other tasks.
└── README.md          # Documentation for the repository.
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/siriusnottin/os.git ~/os
   ```

2. Run the setup script:
   ```bash
   bash ~/os/setup.sh
   ```

3. Use the `os` command to manage your system:
   ```bash
   os
   ```

## Usage

### Dotfiles Management

The `dotfiles` directory contains configurations for various tools like Zsh, Vim, Tmux, and Git. Use the `Makefile` to manage symlinks:

- Create symlinks for all dotfiles:
  ```bash
  make stow-all
  ```

- Remove all symlinks:
  ```bash
  make clean
  ```

- Manage specific dotfiles:
  ```bash
  make stow-<directory>
  ```

### macOS Utilities

- List installed macOS applications:
  ```bash
  python3 src/commands/macos/get_macos_apps.py
  ```

- Manage Homebrew packages:
  ```bash
  python3 src/commands/macos/get_brew_casks_formulae.py
  ```

### Zsh Configuration

The Zsh configuration is modular and includes plugins managed by [Znap](https://github.com/marlonrichert/zsh-snap). To customize, edit the files in `dotfiles/zsh/`.

### Vim Configuration

The Vim configuration is based on [amix/vimrc](https://github.com/amix/vimrc). To customize, edit the `.vimrc` file in `dotfiles/vim/`.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the repository.
