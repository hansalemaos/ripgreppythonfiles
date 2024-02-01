# Search for code in your env using ripgrep  

## Tested against Windows / Python 3.11 / Anaconda

## pip install ripgreppythonfiles


A script to search for code in your env using ripgrep  https://github.com/BurntSushi/ripgrep 


Example: 

```
(mainenv) C:\ProgramData\anaconda3\envs\mainenv>rgtt import\ numpy    #SPACES MUST BE ESCAPED!!

call python -c "from ripgreppythonfiles import rfile;rfile(r'''import\ numpy''')"
C:\ProgramData\anaconda3\envs\mainenv\bstackbin.py:1:1:import numpy as np
C:\ProgramData\anaconda3\envs\mainenv\bstackbin.py-2-import regex # pip install regex
C:\ProgramData\anaconda3\envs\mainenv\bstackbin.py-3-

C:\ProgramData\anaconda3\envs\mainenv
C:\ProgramData\anaconda3\envs\mainenv\anyarray.pyx-12-from cython.parallel cimport prange
C:\ProgramData\anaconda3\envs\mainenv\anyarray.pyx-13-cimport cython
C:\ProgramData\anaconda3\envs\mainenv\anyarray.pyx:14:1:import numpy as np
C:\ProgramData\anaconda3\envs\mainenv\anyarray.pyx:15:2:cimport numpy as np
C:\ProgramData\anaconda3\envs\mainenv\anyarray.pyx-16-import cython
C:\ProgramData\anaconda3\envs\mainenv\anyarray.pyx-17-

C:\ProgramData\anaconda3\envs\mainenv
C:\ProgramData\anaconda3\envs\mainenv\cmdaxs.py-50-
C:\ProgramData\anaconda3\envs\mainenv\cmdaxs.py-51-import pymem
C:\ProgramData\anaconda3\envs\mainenv\cmdaxs.py:52:1:import numpy as np
C:\ProgramData\anaconda3\envs\mainenv\cmdaxs.py-53-from pdmemedit import Pdmemory
C:\ProgramData\anaconda3\envs\mainenv\cmdaxs.py-54-# pass either pid or filename, but not both

.... 

Output written to: C:\Users\hansc\AppData\Local\Temp\tmpbmfm5sdo.txt
```



```python
rfile(args: str):
    Runs ripgrep with the provided arguments, printing the split arguments and calling `run_ripgrep`.

    Parameters:
        - args (str): The arguments to pass to ripgrep.

    Returns:
        None

    Obs:
        Useful when using a bat file:
        Content of rgtt.bat
            call python -c "from ripgreppythonfiles import rfile;rfile(r'''%*''')"
        Calling the bat file;
            rgtt.bat import\ numpy 5 100 1 120

run_ripgrep(
    r: str = "",
    c: int | str = 2,
    m: int | str = 1,
    s: int | str = 1,
    l: int | str = 80,
    f: str = "py,pyx",
):

    Runs ripgrep with specified parameters.

    Parameters:
        - r (str): The regular expression to search for.
        - c (in,str): The number of lines of context to display.
        - m (in,str): The maximum search depth.
        - s (in,str): If 1, writes the ripgrep output to a temporary file.
        - l (in,str): The maximum number of columns to display in the output.
        - f (str): A str of file extensions to search for (e.g, py,pyx).

    Returns:
        subprocess.CompletedProcess: The result of the ripgrep subprocess.

```
