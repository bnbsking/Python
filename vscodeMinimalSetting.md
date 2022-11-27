+ pips:
    |                            | python path                                 | pip path         |
    | -                          | -                                           | -                |
    | python installed by apt    | /usr/bin/python3                            | same dir as left |
    | python installed by conda  | /home/james/.local/bin                      | same dir as left |
    | python installed by conda  | /home/james/miniconda3/bin/python           | same dir as left |
    | conda create -n            | /home/james/miniconda3/envs/test/bin/python | same dir as left |
    | python installed by vscode | /bin/python3                                | same dir as left |
    + which pip
    + conda install -n <env> <package>

+ Download VsCode (~96MB) and install

+ Create an empty folder and open it by VSCode

[Minimal]

+ Create new .ipynb and edit:
    + "ctrl+`" to open terminal
    + conda activate <correct_environemnt>
    + which pip: to get correct package path, otherwise reset PATH
    + ipython xxx.ipynb (pip install ipython first)
    
+ Create new .py and edit:
    + same as above but python xxx.py at last step

[Code runner and Hints while editing]
+ Install python from vs code first
+ "ctrl+shift+P" and type "Python: Select Intepreter" to choose conda kernel
