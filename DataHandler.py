import pandas as pd

inverter = pd.read_csv("LACO_CSV_Relatório_mensal_2019_06.csv", sep=",", skiprows=[1])

dlogger = pd.read_csv("CR300Series_Teste1.dat", sep=",", header=1, skiprows=[2, 3])

inverter.drop(columns=['Unnamed: 14'], inplace=True)

inverter['Timestamp'] = pd.to_datetime(inverter['Data e horário'], format='%d.%m.%Y %H:%M', infer_datetime_format=True)

dlogger['Timestamp'] = pd.to_datetime(dlogger['TIMESTAMP'], infer_datetime_format=True)

dlogger['Velocidade_Avg'] -= dlogger['Velocidade_Avg'].min()

dlogger['Tc1'] = dlogger['Temp_M1_Avg'].rolling(5).mean()

dlogger['Tc2'] = dlogger['Temp_M2_Avg'].rolling(5).mean()

dlogger['v'] = dlogger['Velocidade_Avg'].rolling(5).mean()

dlogger['d'] = dlogger['Direcao_Avg'].rolling(5).mean()

dlogger['G'] = dlogger['Irradiacao_Avg'].rolling(5).mean()

dataframe = pd.merge(inverter, dlogger, on='Timestamp')

dataframe = dataframe.rename(index=str, columns={'Corrente CA L1|Primo 3.0-1 (# 1)': 'Iac3',
                                                 'Corrente CC MPP1|Primo 3.0-1 (# 1)': 'Icc1',
                                                 'Corrente CC MPP2|Primo 3.0-1 (# 1)': 'Icc2',
                                                 'Energia|Primo 3.0-1 (# 1)': 'Ect',
                                                 'Energia MPP1|Primo 3.0-1 (# 1)': 'Et1',
                                                 'Energia MPP2|Primo 3.0-1 (# 1)': 'Et2',
                                                 'Voltagem CA L1|Primo 3.0-1 (# 1)': 'Vac3',
                                                 'Voltagem CC MPP1|Primo 3.0-1 (# 1)': 'Vcc1',
                                                 'Voltagem CC MPP2|Primo 3.0-1 (# 1)': 'Vcc2'})

dataframe['Pcc1'] = dataframe['Vcc1']*dataframe['Icc1']
dataframe['Pcc2'] = dataframe['Vcc2']*dataframe['Icc2']
