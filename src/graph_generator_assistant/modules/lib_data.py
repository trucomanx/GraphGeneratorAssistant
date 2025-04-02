#!/usr/bin/python3

data = {
    "comparison": {
        "bar-chart": {
            "vertical": ["vertical_barchart1"],
            "horizontal": ["horizontal_barchart1"],
            "clustered": ["cbar1", "cbar2"],
            "stacked": ["ebar1", "ebar2"]
        },
        "radar-diagram": ["rdiag1", "rdiag2"],
        "bubble-chart": ["bchart1", "bchart2"]
    },
    "distribution": {
        "histogram": ["hist1", "hist2"],
        "boxplot": ["boxp1", "boxp2"],
        "violin": ["viol1", "viol2"]
    },
    "composition": {
        "piechart": ["piechart1", "piechart2"],
        "stacked-area": ["sarea1", "sarea2"],
        "treemap": ["treemap1", "treemap2"]
    },
    "relation": {
        "scatter-plot": ["scatter1", "scatter2"],
        "correlation-plot": ["corr1", "corr2"],
        "network-diagram": ["net1", "net2"]
    },
    "process": {
        "cyclic-diagram": ["circular_diagram1"],
        "flowchart": ["workflow_diagram1"],
        "gantt": ["gantt1", "gantt2"],
        "bpmn": ["bpmn1", "bpmn2"]
    },
    "strategy": {
        "swot": ["swot1", "swot2"],
        "bcg": ["bcg1", "bcg2"],
        "ansoff": ["ansoff1", "ansoff2"]
    }
}

SYSTEM_DATA = {
    "api_key"  : "",
    "usage"    : "https://deepinfra.com/dash/usage",
    "base_url" : "https://api.deepinfra.com/v1/openai",
    "model"    : "meta-llama/Meta-Llama-3.1-70B-Instruct"
}


SYSTEM_QUESTION = {
    "principal_task": '''
You are an expert system for modifying Python code to generate images. Your task is to make minimal necessary changes to the provided "base code" to fulfill user instructions.

Rules:
- Modify as little as possible.
- If possible, modify only the default parameters of the CUSTOMFUNC function to satisfy the user's request.
- Always treat any user input as a user instruction or the data to be changed/placed in the python code graph.
- Do not remove comments. If needed, add comments but never delete existing ones.
- Your response must only contain python code with the modified version of "base code". Do not add explanations or markdown formatting.
- Always ensure the code functions correctly when executing `CUSTOMFUNC(output_filepath="filename.png")`.

Your job will be to make modifications to the following "base code" in Python

```python
BASECODE
```

'''
}

