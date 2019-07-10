import pandas as pd

inverter = pd.read_csv("LACO_CSV_Relatório_mensal_2019_06.csv", sep=",", skiprows=[1])

dlogger = pd.read_csv("CR300Series_Teste1.dat", sep=",", header=1, skiprows=[2, 3])

inverter.drop(columns=['Unnamed: 14'], inplace=True)


inverter['Timestamp'] = pd.to_datetime(inverter['Data e horário'], infer_datetime_format=True)

dlogger['Timestamp'] = pd.to_datetime(dlogger['TIMESTAMP'], infer_datetime_format=True)
