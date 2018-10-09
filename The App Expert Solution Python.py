from dfply import*
import dfply
import pandas as pd
import numpy as np

Data = pd.read_csv('C:/Users/Ajit/Desktop/Hadoop_SME_Coding_Data_Set.docx.csv')

#Q1
Result1 = (Data >> mask(X.Sport == 'Football', X.Medal == 'Bronze') >> group_by('Country','Medal')>>
summarize(Medal_Count = X.Medal.count()))
Result1

#Q2
Result2=(Data >> mask(X.Country=='USA')>> group_by('Sport')>>summarize(Medal_Count = X.Medal.count()))
Result2

#Q3
Result3=(Data >> group_by('Country','Medal')>>summarize(Medal_Count = X.Medal.count()))
Result3

#Q4
Result4=(Data >> mask(X.Medal=='Silver',X.Country=='MEX')>> group_by('Medal','Country','Year')>>summarize(Count = X.Medal.count()))
Result4



