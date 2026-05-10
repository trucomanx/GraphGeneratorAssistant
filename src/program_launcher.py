#!/usr/bin/python3

'''
## ubuntu ##
python3 -m venv venv-temporal
source venv-temporal/bin/activate
pip install --upgrade pip

## windows ##
python -m venv venv-temporal
venv-temporal\Scripts\activate
python -m pip install --upgrade pip

pip install pyinstaller pyinstaller-hooks-contrib
pip install -r requirements.txt
cd src

## ubuntu ##
python3 -m PyInstaller --onefile --windowed --name graph_generator_assistant --add-data "graph_generator_assistant/images:images" --add-data "graph_generator_assistant/templates:templates" --add-data "graph_generator_assistant/icons:icons" --collect-all PyQt5 --collect-all matplotlib --collect-all networkx --collect-all scikit-learn --collect-all pillow --collect-all scipy --collect-all squarify program_launcher.py


## windows ##
python -m PyInstaller --onefile --windowed --name graph_generator_assistant --add-data "graph_generator_assistant/images;images" --add-data "graph_generator_assistant/templates;templates" --add-data "graph_generator_assistant/icons;icons" --collect-all PyQt5 --collect-all matplotlib --collect-all networkx --collect-all scikit-learn --collect-all pillow --collect-all scipy --collect-all squarify program_launcher.py

'''

import os
from PyQt5.QtCore import QLibraryInfo

os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = QLibraryInfo.location(
    QLibraryInfo.PluginsPath
)


from graph_generator_assistant.program import main

if __name__ == "__main__":
    main()

