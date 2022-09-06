import pandas

from fpdf import FPDF
import os

df_python = pandas.read_excel('aaa.xlsx',
                              sheet_name='Todos',
                              usecols=['Nome', 'Jantar', 'Sala', 'Dia'])

for i in range(len(df_python)):
    X = df_python.iloc[i, 0], df_python.iloc[i, 1], df_python.iloc[i, 2], df_python.iloc[i, 3]
    name = df_python.iloc[i, 0]
    name_format = name.replace(" ", "_")

    folder = os.path.join("C:\\", "Users", "alunotemp", "OneDrive - Instituto Germinare", "Documentos", "GerminaTech's"     ,
                          name_format)

    print('Pasta: ', folder)
    os.mkdir(folder)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=20)
    pdf.cell(300, 10, txt=str(X), ln=3, align='L')
    pdf.output(f"{name_format}.pdf")
    print(f'O pdf {i} foi criado com sucesso')





