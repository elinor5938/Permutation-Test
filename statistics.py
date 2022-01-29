################ imports ###################################################
import pandas as pd 
from scipy.stats import describe
import numpy as np
from itertools import combinations
import random
from scipy import stats
from scipy.stats import ks_2samp
#from scipy.stats import cramervonmises_2samp
import numpy as np
################ parameters #################################################
# <editor-fold desc="reading the simulations csv">
params={}
params["loose_df"]=pd.read_csv("C:/Users/Elinor/Desktop/תואר שני/thesis_codes/Random_wallk_files/ Simulation Analysis/second function/AEVTQHGSY.csv")
params["middle_df"]=pd.read_csv("C:/Users/Elinor/Desktop/תואר שני/thesis_codes/Random_wallk_files/ Simulation Analysis/third function - middle function/AEVTQHGSY.csv")
params["strict_df"] =pd.read_csv("C:/Users/Elinor/Desktop/תואר שני/thesis_codes/Random_wallk_files/ Simulation Analysis/first function/AEVTQHGSY.csv")

for df in params: # filtering the accepted steps for each df
    params[df] = params[df][params[df]["probabilty_res_MCMC"] == "True"]
# </editor-fold>

def calculate_disrubution_properties(data,data_name,col="total_binders",given_name=""):
    """

    :param data: data that we want to analysis
    :param data_name: data name
    :param given_name: data given name after calculating it's descriptive statistics
    :param col :the column we want to analyze
    :return: series of all the data with it's descriptive statistics
    """
    if type(data)==pd.DataFrame:
        data=data[col]
    if given_name!="":
        index=data_name+"_"+given_name
    index = data_name
    series_vals=data.describe()
    series_vals["skew"]=data.skew()
    series_vals["kurtosis"]=data.kurtosis()
    series_vals["variance"]=data.var()
    series_vals["median"]=data.median()
    series_vals["Interquartile_range"]=series_vals["75%"]-series_vals["25%"]
    series_vals.name=index
    series_vals.rename({series_vals.name:index},inplace=True)

    return series_vals


def permutation_test(df1,df2,col,df1_name,df2_name):
    """
    gets two df and perform permutation test between their columns
    :param df1:
    :param df2:
    :param col:
    :param df1_name:
    :param df2_name:
    :return:
    """

    main_df=pd.DataFrame()
    sub_df=calculate_disrubution_properties(df1,df1_name)
    sub_df2=calculate_disrubution_properties(df2,df2_name)

    main_df=main_df.append(sub_df)
    main_df=main_df.append(sub_df2)
    main_df= main_df.T
    main_df["obs_diff"]=abs(main_df[df1_name]-main_df[df2_name])

    # shuffle all the data
    all_total_binders=df1[col].tolist()
    all_total_binders.extend(df1[col].tolist())
    all_total_binders.extend(df2[col].tolist())

    for i in range(1,10000):
        series_name1="random_{name}_{number}".format(name=df1_name,number=str(i))
        series_vals1=pd.Series(random.sample(all_total_binders, 500))
        main_df[series_name1]=calculate_disrubution_properties(series_vals1,series_name1)
        series_name2="random_{name}_{number}".format(name=df2_name,number=str(i))
        series_vals2=pd.Series(random.sample(all_total_binders, 500))
        main_df[series_name2]=calculate_disrubution_properties(series_vals2,series_name2)
        main_df["diff_{}".format(i)] = abs(main_df[series_name1] - main_df[series_name2])

    main_df = main_df.reindex(sorted(main_df.columns), axis=1)




    main_df["count"]=main_df.iloc[:, 0:9999].ge(main_df.loc[:,"obs_diff"], axis=0).sum(axis=1)
    main_df["pvalue"]=main_df["count"]/10000

    return main_df




main=permutation_test(params["middle_df"],params["strict_df"],"total_binders","middle_df","strict_df")

main["count"]
ks_2samp(params["middle_df"]["total_binders"].tolist(), params["strict_df"]["total_binders"].tolist())
main=main.T
main.to_csv("intermediate_VS_strict.csv")
# stats.cramervonmises_2samp(params["loose_df"]["total_binders"].tolist(), params["strict_df"]["total_binders"].tolist())
#
# scipy.stats.cramervonmises_2samp(x, y, method='auto')
#     all_random_vec[series_name]=series_vals
#
#     all_random_vec["random_middle{}".format(str(i))] = random.sample(all_total_bindes, 500)
