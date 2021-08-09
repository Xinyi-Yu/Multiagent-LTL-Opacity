# Multi-agent LTL opacity

We propose a framework which synthesizes a plan of multi-agent team for LTL tasks and opacity security constraints.

## Security-Preserving Multi-Agent Coordination for Complex Temporal Logic Tasks

PDF | [Code](https://github.com/Xinyi-Yu/Multiagent-LTL-Opacity/tree/main/codes) | Video

#### Instructions
Take Case Study 3 in the paper as an example, we upload the corresponding codes and you can try `main.py` in the [codes](https://github.com/Xinyi-Yu/Multiagent-LTL-Opacity/tree/main/codes) folder to obtain the final result.
It costs about 1h and the results are shown in `result.txt`.
To run other cases in the paper or self-defined scenarios, you only need to change the corresponding information in `Init.py`.

Moreover, the construction details of GTS, labeling-GTS, multiple-labeling-GTS, automata and product system in the paper are corresponding to `GTS.py`, `labelingGTS.py`, `MulLabelingGTS.py`, `buchi.py` and `ProductSystem.py` in this project respectively.


#### Dependencies
- The packages needed for running the code are [NetworkX](https://networkx.org/) and [PLY](http://www.dabeaz.com/ply/).
- `ltl2ba` in the [codes](https://github.com/Xinyi-Yu/Multiagent-LTL-Opacity/tree/main/codes) folder is an executable file complied under OS X or linux. For other systems, please follow [Install_ltl2ba/README.md](https://github.com/Xinyi-Yu/Multiagent-LTL-Opacity/blob/main/Install_ltl2ba/README.txt).

#### Acknowledgement
Thanks for [MengGuo's project](https://github.com/MengGuo/P_MAS_TG)'s great help when I learned this field.
