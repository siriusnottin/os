# Notes for later
These are my notes of important things to add in the script, and stuff that I need to make sure will be integrated in the script but not sure if they are automatically added with the current version of my software.

## Important stuff to remember

- Set fixed IP address for the machine
- Automate the install of fastfetch and start it on zsh startup

## Softwares to add

### Basic stuff

1. Raycast
6. 1Password
7. VS Code
8. Warp
9. Ghostty
10. Podman
11. Discord 

## Nerd Fonts

Install Nerd Fonts

```sh
brew install font-hack-nerd-font
```

[ryanoasis/nerd-fonts: Iconic font aggregator, collection, & patcher. 3,600+ icons, 50+ patched fonts: Hack, Source Code Pro, more. Glyph collections: Font Awesome, Material Design Icons, Octicons, & more](https://github.com/ryanoasis/nerd-fonts?tab=readme-ov-file#option-2-homebrew-fonts)

### Vim

**Install Vim:**

```sh
brew install vim
```

Configure Vim

Use this: (see: [#7](https://github.com/siriusnottin/os/issues/7))

[The Ultimate vimrc](https://github.com/amix/vimrc?tab=readme-ov-file)

Instant Markdown previews from Vim

[vim-instant-markdown](https://github.com/instant-markdown/vim-instant-markdown)

**Install Tmux**

```sh
brew install tmux
```


### Specific things

- Scroll Reverser [^1]
  - With its config if possible
- Autokbisw [^2]
- Discord Activity
  - VS Code activity for Discord
  - Figma activity for Discord
- Raycast custom plugins

## Configs to restore

- MacOS system settings
  - Keyboard shortcuts
- Raycast settings
  - Sync snippets
- VS Code
  - Profiles
  - Configs
  - Extensions
    - Projects

- SSH keys
- GPG keys
- Dotfiles

## Terminal

- Warp
  - Push all local stuff in Warp Drive

## Packages to install

- Homebrew
- Node (nvm)
- Python (pyenv)
- VirtualBox

## Dev

### Xcode

I can't install the latest version of Xcode because I can only upgrade my OS up to Sonoma (14.7). I need to find a way to install the latest version of Xcode that is compatible with my OS.

1. This site seems to have a list of all the Xcode versions and their compatibility with the different versions of MacOS:
    
    [Xcode Releases | xcodereleases.com](https://xcodereleases.com/?scope=release)


2. Here is the site where Apple has all the Xcode versions available for download:

    [More - Downloads - Apple Developer](https://developer.apple.com/download/all/?q=xcode%2015)

#### Steps to install Xcode

Here's the steps to install Xcode, according to Perplexity.ai:

1. Visit the Apple Developer website (https://developer.apple.com/download/all/).
2. Sign in with your Apple ID. You don't need a paid developer account; a free Apple ID is sufficient.
3. Once logged in, search for "Xcode" in the search bar.
4. Look for the most recent version of Xcode that is compatible with macOS 13.7. This will likely be Xcode 15.0 or 15.1.
5. Download the Xcode .xip file for the compatible version.
6. Once the download is complete, double-click the .xip file to extract it
7. After extraction, drag the Xcode application to your Applications folder
8. Open Xcode from your Applications folder. You may need to right-click and select "Open" the first time to bypass Gatekeeper security
9. Xcode will likely prompt you to install additional components. Follow the on-screen instructions to complete the setup.

[^1]: To have the scroll behavior to be separated between the trackpad and the mouse. [Official Website](https://pilotmoon.com/scrollreverser/)
[^2]: To have the keyboard layout switcher to be automatic.[Official Website](https://github.com/ohueter/autokbisw)

## Stow

```sh
brew install stow
```
