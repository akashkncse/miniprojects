import pandas as pd

# dataframe
# a dataframe is nothing but data loaded into our python program

# relative path => path that is relative to your working directory
# ./dataset/application_train.csv
# we are creating a name called df for dataframe using pandas (alias name is pd), we are using a library function
# called read_csv and we're passing the location of the csv file and we're just overall printng the dataset df so it's just
# showing the overall info about the dataset   
df = pd.read_csv("./dataset/application_train.csv")
print(df[["SK_ID_CURR", "CNT_FAM_MEMBERS"]])
