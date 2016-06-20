# getFolder
Get folder paths using user-defined keywords. Can be used to cd and ls in terminal.

## Setup
- Create a config file like the example included in this repo (config.txt). The config file lists keywords and associated paths. One keyword/path per line, separated by a comma.
- Set the variable `keyword_paths` to be the full path to the config file (line 15 in gf.py).
- Add the following alias (`gf`) and functions (`cdd` and `lss`) to your .bash_profile or .bashrc.

```bash
alias gf="python path/to/gf.py"
function cdd()
{
    cd "$(gf "$@")"
}
function lss()
{
    ls "$(gf "$@")"
}
```

## Usage
`gf [keyword] folders`

## Input
`keyword` = A keyword defined in the config file.  
`folders` = Names of folders and subfolders to add to the output.

## Examples
`gf path to dir` returns `path/to/dir`  
`gf keyword then dirs` returns `path/defined/in/config/file/then/dirs`

