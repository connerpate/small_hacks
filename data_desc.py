import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def data_desc(data):
    cols = data.columns
    desc = pd.DataFrame()
    for x in cols:
        if (data[x].dtype == 'float64') | (data[x].dtype == 'int64'):
            desc[x] = data[x].describe()
    print("Summary of Numerical Columns:")
    return desc


def order_magnitude_sorting(x):
  return(
      round(np.log10(x),0)
  )


#This function creates box plots for all numerical data within a df, sorted by their order of magnitude
def description_box_plot_data(df):
  #create mask to grab all numerical columns
  num_cols = (df.dtypes == "float64") | (df.dtypes == "int64")
  
  #create a numerical-only DataFrame using the mask
  num_df = df.copy()
  num_df = num_df.loc[:,num_cols] 
  num_df['class'] = num_df.describe().loc['max'].apply(order_magnitude_sorting)

  #create numerical-only subset masks based on order of magnitude, for easier plotting later
  num_df0_cols =  num_df.describe().loc['max'].between(0,1,inclusive="both")
  num_df1_cols =  num_df.describe().loc['max'].between(1,10,inclusive="right")
  num_df2_cols =  num_df.describe().loc['max'].between(10,100,inclusive="right")
  num_df3_cols =  num_df.describe().loc['max'] > 100

  #create the subset DataFrames based on the subset masks
  num_df0 = num_df.copy()
  num_df0 = num_df.loc[:,num_df0_cols]

  num_df1 = num_df.copy()
  num_df1 = num_df.loc[:,num_df1_cols]

  num_df2 = num_df.copy()
  num_df2 = num_df.loc[:,num_df2_cols]

  num_df3 = num_df.copy()
  num_df3 = num_df.loc[:,num_df3_cols]

  #create figures 
  global desc_fig
  desc_fig = go.Figure()
  global desc_fig0
  desc_fig0 = go.Figure()
  global desc_fig1
  desc_fig1 = go.Figure()
  global desc_fig2
  desc_fig2 = go.Figure()
  global desc_fig3
  desc_fig3 = go.Figure()

  #populate figures with the data from each subset DataFrame
  for x in num_df:
    num_df['label'] = x
    desc_fig.add_trace(
        go.Box(
            x=num_df['label'],
            y=num_df[x],
            # facet_col = num_df['class']
        )
    )

 
  for x in num_df0:
    num_df0['label'] = x
    desc_fig0.add_trace(
        go.Box(
            x=num_df0['label'],
            y=num_df0[x]
        )
    )

  for x in num_df1:
    num_df1['label'] = x
    desc_fig1.add_trace(
        go.Box(
            x=num_df1['label'],
            y=num_df1[x]
        )
    )

  for x in num_df2:
    num_df2['label'] = x
    desc_fig2.add_trace(
        go.Box(
            x=num_df2['label'],
            y=num_df2[x]
        )
    )

  for x in num_df3:
    num_df3['label'] = x
    desc_fig3.add_trace(
        go.Box(
            x=num_df3['label'],
            y=num_df3[x]
        )
    )