# getFolder
A python script that returns a path using keywords. Can be used to cd and ls.

## Usage
gf [keyword] folders

## Input
`keyword` = A keyword defined in the config file.
`folders` = Names of folders and subfolders to add to the output.

## Examples
`gf path to dir` returns `path/to/dir`
`gf keyword then dirs` returns `path/defined/in/config/file/then/dirs`

## Setup
Set the full path to the config file on line 15 in gf.py (variable 'keyword_paths'. The config file lists keywords and associated paths. One keyword/path per line, separated by a comma.

Add the following alias (gf) and functions (cdd and lss) to your .bash_profile or .bashrc.

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