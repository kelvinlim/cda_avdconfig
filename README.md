# test_python_avd   

Use conda/mamba for creating environments including JDK and graphviz

To create environment fc. Make it short to 
prevent running into windows long path error
```
# create with python3.13
mamba create --name fc python=3.13

# init if you haven't done this before
# When you open a new terminal, it will begin with (base)
mamba init

# activate the env fc, mamba didn't work!
conda activate fc

# to add  graphviz and jdk21
mamba install -c conda-forge openjdk=21 python-graphviz 

# to check java
java -version
# to check graphviz
dot -V

# use pip to install packages
# install fastcda
pip install fastcda 

# install ipykernel for ipynb support
pip install ipykernel

# to create portable export that supports cross-platform (windows/linux/mac)
mamba env export --from-history > environment.yaml

# to create an export for same system without build strings
mamba env export --no-builds > environment_win11.yaml

```
R:\DVBIC\venvs\fastcda\Scripts\python.exe

make a symboliclink

mklink /D venv R:\DVBIC\venvs\fastcda