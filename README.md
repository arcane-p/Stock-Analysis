# Stock-Analysis

This is a flegdling project, created as a chance for me to explore financial analysis via Python.

The idea is to eventually create a CLI which can run a variety of configurable financial analysis on every stock listed in the S&P 500, returning to the user stocks that the program determines as positive potential.

To do this, the project is highly modulised, allowing the program to import only the modules it requires. Additionally, logging and various (configurable) levels of debug output are used throughout.

### Current modules
- [X] Long-term EMA/SMA compared with short-term EMA/SMA
- [ ] Choose whether to simply output or display graphically stocks with potential
