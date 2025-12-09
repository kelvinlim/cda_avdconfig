# %% [markdown]
# Code to demonstrate basic FastCDA capabilities in a Jupyter notebook.

# %%
from fastcda import FastCDA
from dgraph_flex import DgraphFlex
import semopy
import pprint as pp

# create  an instance of FastCDA
fc = FastCDA()

# %% [markdown]
# ###  *Reading in data*
# 
# For this demo, we are going to use a sample ema dataset that is built into
# the fastcda package.
# 
# To read in your own csv data file "mydata.csv" you would
# use the pandas package, a very powerful package for working 
# with dataframes.
# 
# Here is the code:
# ```
# import pandas as pd
# 
# df = pd.read_csv("mydata.csv")
# 
# ```

# %%
# read in the sample ema dataset and view it
df = fc.getEMAData()

df

# %%
# add the lags, with a suffix of '_lag'
lag_stub = '_lag'
df_lag = fc.add_lag_columns(df, lag_stub=lag_stub)
df_lag

# %%
# standardize the data
df_lag_std = fc.standardize_df_cols(df_lag)
df_lag_std

# %%
# lets get the dataframe col names
cols = df.columns
cols

# %%
# Create the knowledge prior content for temporal
# order. The lag variables can only be parents of the non
# lag variables

knowledge = {'addtemporal': {
                            0: [col + lag_stub for col in cols],
                            1: [col for col in cols]
                            }
            }
knowledge

# %%
# run model with run_model_search
result, graph = fc.run_model_search(df_lag_std, 
                             model = 'gfci',
                             score={'sem_bic': {'penalty_discount': 1.0}},
                             test={"fisher_z": {"alpha": .01}},
                             knowledge=knowledge
                             )


# %%
graph.save_graph('test_plot')


