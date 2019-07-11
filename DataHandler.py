import pandas as pd

inverter = pd.read_csv("LACO_CSV_Relatório_mensal_2019_06.csv", sep=",", skiprows=[1])

dlogger = pd.read_csv("CR300Series_Teste1.dat", sep=",", header=1, skiprows=[2, 3])

inverter.drop(columns=['Unnamed: 14'], inplace=True)

inverter['Timestamp'] = pd.to_datetime(inverter['Data e horário'], format='%d.%m.%Y %H:%M', infer_datetime_format=True)

dlogger['Timestamp'] = pd.to_datetime(dlogger['TIMESTAMP'], infer_datetime_format=True)

print(dlogger['Velocidade_Avg'].min())
print(dlogger['Velocidade_Avg'].head(10))

dlogger['Tc1'] = dlogger['Temp_M1_Avg'].rolling(5).mean()

dlogger['Tc2'] = dlogger['Temp_M2_Avg'].rolling(5).mean()

dlogger['v'] = dlogger['Velocidade_Avg'].rolling(5).mean()

dlogger['d'] = dlogger['Direcao_Avg'].rolling(5).mean()

dlogger['G'] = dlogger['Irradiacao_Avg'].rolling(5).mean()

print(dlogger['v'].head(10))
