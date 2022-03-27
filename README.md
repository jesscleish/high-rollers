# high-rollers
Dice rolling game created in python (pygame) for SOFE 3980U: Software Quality

## How to Run
1. `pip install pygame`
2. `pip install -U matplotlib`
3. Run hrDriver.py through an IDE, or through command line with `python hrDriver.py`. If you are having issues with the command line, try an IDE.
4. Play game :)  (ensure volume is on!)

<br>
Ensure all game files, assets, and sounds are stored within the same directory, otherwise they will not load correctly.
<br><br>

For running the test suite: `pip install -U pytest`. 
Then, `pytest testsuite.py` from within the game’s directory.

## Operating the Program Slicer
1. On line 4, specify the filename to analyze. This is preset to the highrollers.txt source code document. This document must be in the project root folder.
2. Run programslicer.py through an IDE, or through command line with `python programslicer.py`
3. Enter variable to slice on.
4. Slice will be output to terminal.

### Program Slicer Limitations
- Case sensitive
- Includes logic structures not directly relevant to the variable
- No support for multi-line if/else structures
- No support for the use of different names for the same variables (requiring it to be rewritten prior to use with the slicer) 
- Comments must be removed,
- Lack of structure and clarity for where each snippet in the slice comes from (function declarations not always included)
- Lines that contain the variable as part of another word will also be included even if not related
- Output format of the slices contains all indentation from the source program


## Performing Dynamic Analysis
The dynamic analysis version of the source code is contained within [this folder](https://github.com/jessica-leishman/high-rollers/tree/f880993377f5c29a2ba2c379136e5dcae66aee1f/analysis_dynamic). 

Ensure the above ["How to Run"](https://github.com/jessica-leishman/high-rollers/blob/main/README.md#how-to-run) instructions have been done.  
To run the analysis version, run hrDDriver or through command line with `python hrDDriver.py`.
