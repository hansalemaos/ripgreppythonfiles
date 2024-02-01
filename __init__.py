import os
import tempfile
from touchtouch import touch
import shutil
import sys
import subprocess
import shlex

rgpath = shutil.which("rg.exe")
if not rgpath:
    input(
        "ripgrep not found! Please install ripgrep https://github.com/BurntSushi/ripgrep , put it in your path and restart the script"
    )
    sys.exit(1)


def get_tmpfile(suffix=".bin"):
    tfp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    filename = tfp.name
    filename = os.path.normpath(filename)
    tfp.close()
    touch(filename)
    return filename


def rfile(args: str):
    """
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
    """
    spliargs = shlex.split(args)
    run_ripgrep(*spliargs)


def run_ripgrep(
    r: str = "",
    c: int | str = 2,
    m: int | str = 1,
    s: int | str = 1,
    l: int | str = 80,
    f: str = "py,pyx",
):
    r"""
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
    """
    if not r:
        sys.exit(1)
    r = r.replace(" ", r"\s")
    cwd = os.getcwd()
    p = subprocess.run(
        [
            rgpath,
            "--regexp",
            r,
            "-i",
            "-S",
            "-U",
            "-L",
            "-C",
            str(c),
            "--vimgrep",
            "--with-filename",
            "--pretty",
            "--no-messages",
            "--max-depth",
            str(m),
            "--binary",
            "-g",
            f"*.{{{f}}}",
            "--max-columns",
            str(l),
            "--max-columns-preview",
        ],
        capture_output=True,
        env=os.environ.copy(),
        cwd=cwd,
    )
    completeoutput = []
    li = p.stdout.decode("utf-8", "backslashreplace").splitlines()
    for l in li:
        if l == "--":
            completeoutput.append(f"\n{cwd}")
            continue
        completeoutput.append(f"{cwd}{os.sep}{l}")
    completeoutputstr = "\n".join(completeoutput)
    print(completeoutputstr)
    if s:
        regexinputmp = get_tmpfile(suffix=".txt")
        with open(regexinputmp, mode="w", encoding="utf-8") as f:
            f.write(completeoutputstr)
        print(f"Output written to: {regexinputmp}")
    return completeoutputstr
