# Source shared configurations
source ~/os/zsh-config/aliases.zsh
source ~/os/zsh-config/functions.zsh

# Source OS-specific configurations
if [[ "$OSTYPE" == darwin* ]]; then
  source ~/os/zsh-config/macos.zsh
elif [[ "$OSTYPE" == linux* ]]; then
  source ~/os/zsh-config/linux.zsh
fi
