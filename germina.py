import pandas
from fpdf import FPDF
import os

df_python = pandas.read_excel('teste.xlsx',
                              sheet_name='todos',
                              usecols=['Nome', 'Jantar', 'Turma','Sala', 'Dia'])

for i in range(len(df_python)):
    X = f'Nome: {df_python.iloc[i, 0]}', f'Vai Jantar? {df_python.iloc[i, 1]}', f'Turma: {df_python.iloc[i, 2]}', f'Sala: {df_python.iloc[i, 3]}', f'Dia: {df_python.iloc[i, 4]}'
    name = df_python.iloc[i, 0]
    name_format = name.replace(" ", "_")

    folder = os.path.join("C:\\Users\\marce\\Desktop\\Python\\Teste",                          name_format)

    # print('Pasta: ', folder)
    os.mkdir(folder)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=20)
    for j in range(len(X)):
        pdf.cell(300, 10, txt=str(X[j]), ln=3, align='L')
    pdf.output(f"{folder}\{name_format}.pdf")
    # print(f'O pdf {i+1} foi criado com sucesso')



   





