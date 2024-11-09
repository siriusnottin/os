# Source shared configurations
source ~/os/files/dotfiles/zsh-config/aliases.zsh
source ~/os/files/dotfiles/zsh-config/functions.zsh

# Source OS-specific configurations
if [[ "$OSTYPE" == darwin* ]]; then
  source ~/os/files/dotfiles/zsh-config/macos.zsh
elif [[ "$OSTYPE" == linux* ]]; then
  source ~/os/files/dotfiles/zsh-config/linux.zsh
fi

# detect on which system we are running on (ubuntu or macos)
# if [[ -f /etc/os-release ]]; then
#   source /etc/os-release
#   OS=$ID # ubuntu
# elif [[ -f /usr/bin/sw_vers ]]; then
#   OS="macos"
# fi

git config --global init.templatedir "~/os/files/dotfiles/git-templates"
