# py_utils

## rd via loop
```
cat tst.txt | python3 rd_loop2.py '^123'

cat tst.txt | python3 rd_loop3.py '(?:(\d+)[^\d]*)+

cat tst.txt | python3 rd_loop3.py '(\d+)[^\d]*'

```

## git alias sample

```
[alias]
#lg1 = log --graph --abbrev-commit --decorate --date=relative --format=format:'%C(blue)%h%C(reset) - %C(dim green)(%ar)%C(reset) %C(dim blue)%s%C(reset) %C(dim cyan)- %an%C(reset)%C(dim red)%d%C(reset)' --all
        # lg1 = log --graph --abbrev-commit --decorate --date=short --format=format:'%C(dim blue)%h%C(reset) \t- %C(dim red)%d%C(reset) %C(dim blue)%s%C(reset) %C(dim cyan)- %an%C(reset) %C(dim green)(%ad)%C(reset) ' --all
        lg1 = log --graph --abbrev-commit --decorate --date=short --format=format:'%C(white)%h%C(reset) \t- %C(green)%d%C(reset) %C(white)%s%C(reset) %C(cyan)- %an%C(reset) %C(green)(%ad)%C(reset) ' --all
        lg2 = log --graph --abbrev-commit --decorate --format=format:'%C(dim blue)%h%C(reset) - %C(dim green)%aD%C(reset) %C(dim green)(%ar)%C(reset)%C(dim red)%d%C(reset)%n'' %C(dim blue)%s%C(reset) %C(dim cyan)- %an%C(reset)' --all
        lg1s = log --graph --stat --abbrev-commit --decorate --date=short --format=format:'%C(dim blue)%h%C(reset) \t- %C(dim red)%d%C(reset) %C(dim blue)%s%C(reset) %C(dim cyan)- %an%C(reset) %C(dim green)(%ad)%C(reset) ' --all
        l = !git lg1
        s = status
        b = branch -av
        r = remote -v
        c = config --global --edit
        d = difftool
```