import pandas as pd

# Import csv files
inverter = pd.read_csv("LACO_CSV_Relatório_mensal_2019_06.csv", sep=",", skiprows=[1])

dlogger = pd.read_csv("CR300Series_Teste1.dat", sep=",", header=1, skiprows=[2, 3])

# Drop unuseful column
inverter.drop(columns=['Unnamed: 14'], inplace=True)

# Change timestamps on both dataframes to match
inverter['Timestamp'] = pd.to_datetime(inverter['Data e horário'], format='%d.%m.%Y %H:%M', infer_datetime_format=True)

dlogger['Timestamp'] = pd.to_datetime(dlogger['TIMESTAMP'], infer_datetime_format=True)

# Find minimum wind speed (offset)
dlogger['Velocidade_Avg'] -= dlogger['Velocidade_Avg'].min()

# Calculate rolling mean to obtain values for every 5 minutes
dlogger['Tc1'] = dlogger['Temp_M1_Avg'].rolling(5).mean()

dlogger['Tc2'] = dlogger['Temp_M2_Avg'].rolling(5).mean()

dlogger['v'] = dlogger['Velocidade_Avg'].rolling(5).mean()

dlogger['d'] = dlogger['Direcao_Avg'].rolling(5).mean()

dlogger['G'] = dlogger['Irradiacao_Avg'].rolling(5).mean()

# Merge dataframes
dataframe = pd.merge(inverter, dlogger, on='Timestamp')

# Rename labels
dataframe.rename(index=str, columns={'Corrente CA L1|Primo 3.0-1 (# 1)': 'Iac3',
                                     'Corrente CC MPP1|Primo 3.0-1 (# 1)': 'Icc1',
                                     'Corrente CC MPP2|Primo 3.0-1 (# 1)': 'Icc2',
                                     'Energia|Primo 3.0-1 (# 1)': 'Ect',
                                     'Energia MPP1|Primo 3.0-1 (# 1)': 'Ec1',
                                     'Energia MPP2|Primo 3.0-1 (# 1)': 'Ec2',
                                     'Voltagem CA L1|Primo 3.0-1 (# 1)': 'Vac3',
                                     'Voltagem CC MPP1|Primo 3.0-1 (# 1)': 'Vcc1',
                                     'Voltagem CC MPP2|Primo 3.0-1 (# 1)': 'Vcc2'}, inplace=True)

# Calculate power on MPPT's
dataframe['Pcc1'] = dataframe['Vcc1']*dataframe['Icc1']
dataframe['Pcc2'] = dataframe['Vcc2']*dataframe['Icc2']

# Replace NaN with zero
dataframe.fillna(0, inplace=True)

# Write data to csv file
dataframe.to_csv('PVData.csv', mode='w',
                 columns=['Timestamp', 'Tc1', 'Tc2', 'v', 'd', 'G', 'Icc1', 'Icc2', 'Vcc1', 'Vcc2', 'Pcc1', 'Pcc2',
                          'Iac3', 'Vac3', 'Ec1', 'Ec2', 'Ect'],
                 index=False)
