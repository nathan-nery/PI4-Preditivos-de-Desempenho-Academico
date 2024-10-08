import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport

# pd.set_option('future.no_silent_downcasting', True)

base = pd.read_csv("./BD/student_performance_prediction.csv")

base_limpa = base.dropna().copy()

conversao_yes_no = {
    'Yes': 1,
    'No': 0}

conversao_educacao = {
    'High School': 1,
    'Associate': 2,
    'Bachelor': 3,
    'Master': 4,
    'Doctorate': 5
}

base_limpa.loc[:, 'Passed'] = base_limpa['Passed'].map(conversao_yes_no)
base_limpa.loc[:, 'Participation in Extracurricular Activities'] = base_limpa['Participation in Extracurricular Activities'].map(conversao_yes_no)
base_limpa.loc[:, 'Parent Education Level'] = base_limpa['Parent Education Level'].map(conversao_educacao)
base_limpa.loc[:, 'Parent Education Level'] = pd.Categorical(base_limpa['Parent Education Level'],
                                                            categories=[1, 2, 3, 4, 5],
                                                            ordered=True)

base_limpa = base_limpa[base_limpa['Study Hours per Week'] >= 0]
base_limpa = base_limpa[base_limpa['Attendance Rate'] <= 100]
base_limpa = base_limpa[base_limpa['Previous Grades'] >= 0]
base_limpa = base_limpa[base_limpa['Previous Grades'] <= 100]

base_limpa = base_limpa.drop(columns=['Student ID'])

print(base_limpa.head())

analise = ProfileReport(base_limpa, title="Analise de Dados")

analise.to_file("Analise de Dados.html")


# print(base_limpa.corr())acao = base_limpa.corr()

correlacao = base_limpa.corr()
correlacao.to_csv("correlacao.csv")
