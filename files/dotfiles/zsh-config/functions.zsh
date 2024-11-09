# Create a folder and move into it in one command
function mkcd() { mkdir -p "$@" && cd "$_"; }

# create a folder, move into it, initialize git and create a README.md and open it in vscode
# TODO: Create simple cli to improve new project creation (os new project --name "My Super Project", --type "app|labs|learn|hesias course b1"  --git-plateform "GitHub|Gitlab|Gitea")
# TODO: Implement addtion of git workflow
function mkcdg() {
  mkcd "$@"
  git init
  touch README.md
}

# fd - cd to selected directory
fd() {
  local dir
  dir=$(find ${1:-.} -path '*/\.*' -prune \
    -o -type d -print 2>/dev/null | fzf +m) &&
    cd "$dir"
}

# fh - search in your command history and execute selected command
# TODO: test this
fh() {
  eval $( ([ -n "$ZSH_NAME" ] && fc -l 1 || history) | fzf +s --tac | sed 's/ *[0-9]* *//')
}

# TODO: Test this fn
function forget() {
  history -d $(history | awk 'END{print $1-1}')
}
