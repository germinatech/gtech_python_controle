import pandas
import qrcode

df_python = pandas.read_excel('teste.xlsx',
                              sheet_name='todos',
                              usecols=['Nome', 'Jantar', 'Sala', 'Dia'])

for i in range(len(df_python)):
    link = f'https://germinatech.github.io/gtech_python_controle/{df_python.iloc[i, 0].replace(" ", "_")}/{df_python.iloc[i, 0].replace(" ", "_")}.pdf'
    qrimg = qrcode.make(link)
    qrimg.save(f'{df_python.iloc[i, 0].replace(" ", "_")}.png')

