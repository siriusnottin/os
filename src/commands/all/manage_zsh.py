import os


def create_zsh_config(location: str) -> None:
    """
    Create symlinks for Zsh configuration files in the user's home directory.

    This function creates symbolic links for the Zsh configuration files
    (.zshrc and .zshenv) from the specified location to the user's home
    directory. This allows the user to maintain a single set of configuration
    files across multiple machines.

    Args:
        location (str): The directory where the Zsh configuration files are
                        located. Defaults to the user's home directory.

    Returns:
        None
    """
    # Symlink Configuration Files
    # Create symlinks in your home directory on both machines:

    os.system(f"ln -s {location}/zsh-config/.zshrc ~/.zshrc")
    os.system(f"ln -s {location}/zsh-config/.zshenv ~/.zshenv")

    return None


if __name__ == "__main__":
    create_zsh_config()
