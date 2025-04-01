# graph-generator-assistant

Program that translate text

## Testar indicator

```bash
cd src
python3 -m graph_generator_assistant.indicator
```

## Upload to PYPI

```bash
cd src
python setup.py sdist bdist_wheel
twine upload dist/*
```

## Install from PYPI

The homepage in pipy is https://pypi.org/project/graph-generator-assistant/

```bash
pip install --upgrade graph-generator-assistant
```

Using:

```bash
graph-generator-assistant-indicator
```

## Install from source
Installing `graph-generator-assistant` program

```bash
git clone https://github.com/trucomanx/GraphGeneratorAssistant.git
cd GraphGeneratorAssistant
pip install -r requirements.txt
cd src
python3 setup.py sdist
pip install dist/graph_generator_assistant-*.tar.gz
```
Using:

```bash
graph-generator-assistant-indicator
```

## Uninstall

```bash
pip uninstall graph_generator_assistant
```
