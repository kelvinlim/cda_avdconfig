# cda_avdconfig

This project shows how to create a python environment for running cda analyses
with fastcda.

We use conda/mamba for creating environments that also include
the installation of JDK and graphviz.  All this can be done without admin
privileges!

To create the environment named **fc**. Make it short to 
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
