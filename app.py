import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

# colocando nome na aplicação
st.write('# Análise de desempenho de estudantes')

# suindo e tratando os dados
df = pd.read_csv('StudentsPerformance.csv', sep=';')

# trazendo infos ja trabalhadas no notebook (criando a coluna de média)
df['total score'] = df['math score'] + df['reading score'] + df['writing score']
df['média score'] =  df['total score'] / 3

df_visualizar = pd.DataFrame(df)
#st.dataframe(df_visualizar, use_container_width=True)

# criando abas para visualização (layout da aplicação)
tab0, tab1, tab2, tab3, tab4 = st.tabs(['Geral', 'Etnia', 'Gênero', 'Desempenho Notas', 'Desempenho Matérias'])

with tab0:
    st.write('## Visão geral de desempenho de estudantes')
    plt.rcParams['figure.figsize'] = (30, 12)

# Create a subplot with five pie charts side by side
    plt.subplot(1, 5, 1)
    size = df['gender'].value_counts()
    labels = 'Female', 'Male'
    color = ['red', 'orange']

    plt.pie(size, colors=color, labels=labels, autopct='%.2f%%')
    plt.title('Gender', fontsize=20)
    plt.axis('off')

    plt.subplot(1, 5, 2)
    size = df['race/ethnicity'].value_counts()
    labels = 'Group C', 'Group D', 'Group B', 'Group E', 'Group A'
    color = ['red', 'green', 'blue', 'cyan', 'orange']

    plt.pie(size, colors=color, labels=labels, autopct='%.2f%%')
    plt.title('Race/Ethnicity', fontsize=20)
    plt.axis('off')

    plt.subplot(1, 5, 3)
    size = df['lunch'].value_counts()
    labels = 'Standard', 'Free'
    color = ['red', 'orange']

    plt.pie(size, colors=color, labels=labels, autopct='%.2f%%')
    plt.title('Lunch', fontsize=20)
    plt.axis('off')

    plt.subplot(1, 5, 4)
    size = df['test preparation course'].value_counts()
    labels = 'None', 'Completed'
    color = ['red', 'orange']

    plt.pie(size, colors=color, labels=labels, autopct='%.2f%%')
    plt.title('Test Course', fontsize=20)
    plt.axis('off')

    plt.subplot(1, 5, 5)
    size = df['parental level of education'].value_counts()
    labels = 'Some College', "Associate's Degree", 'High School', 'Some High School', "Bachelor's Degree", "Master's Degree"
    color = ['red', 'green', 'blue', 'cyan', 'orange', 'grey']

    plt.pie(size, colors=color, labels=labels, autopct='%.2f%%')
    plt.title('Parental Education', fontsize=20)
    plt.axis('off')

    plt.grid()
# ao inves de utilizar plt.show(), aqui utiliza-se o st.pyplot() para mostrar o código no streamlit
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

with tab1:
    st.write('## Total de estudantes por etnia')

    f, ax = plt.subplots(1, 2, figsize=(20, 10))

    sns.countplot(x=df['race/ethnicity'], data=df, palette='bright', ax=ax[0], saturation=0.95)
    for container in ax[0].containers:
        ax[0].bar_label(container, color='black', size=20)

    plt.pie(x=df['race/ethnicity'].value_counts(), labels=df['race/ethnicity'].value_counts().index,
            explode=[0.1, 0, 0, 0, 0], autopct='%1.1f%%', shadow=True)
    plt.title('Race/Ethnicity Distribution', fontsize=20)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    '''
    Analisando gráficos (o texto aparece no streamlit)

    '''

with tab2:

    st.write('## Análise de estudantes por gênero')
     
    f, ax = plt.subplots(1, 2, figsize=(20, 10))

    sns.countplot(x=df['gender'], data=df, palette='bright', ax=ax[0], saturation=0.95)
    for container in ax[0].containers:
        ax[0].bar_label(container, color='black', size=20)

    plt.pie(x=df['gender'].value_counts(), labels=['Female', 'Male'], explode=[0, 0.1],
            autopct='%1.1f%%', shadow=True, colors=['#2C27FC', '#ff8000'])
    plt.title('Gender Distribution', fontsize=20)

    st.write('escreve a análise aqui antes do gráfico')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(f)
    st.write('escreve a análise aqui depois do gráfico')
    st.write('ex.: O gênero feminino é predominante na base de dados')

with tab3:

    st.write('## Análise de desempenho em notas')

    fig, ax = plt.subplots(1,2, figsize=(15,7))
    plt.subplot(121)
    sns.histplot(data=df, x='média score', bins=30, kde=True, color='g')
    plt.subplot(122)
    sns.histplot(data=df, x='média score', kde=True, hue='gender')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(fig)

    df_female = df[df['gender'] == 'female']
    df_male = df[df['gender'] == 'male']

    st.write('Estatísticas básicas do grupo de estudantes do gênero feminino:')
    df_female.describe().T

    st.write('Estatísticas básicas do grupo de estudantes do gênero masculino:')
    df_male.describe().T

    media = round(df_female['média score'].mean(),2)
    st.write(f'Analisando as estatísticas do grupo de estudantes do gênero feminino teve desempenho superior ao grupo de estudantes do gênero masculino, obtendo uma média igual a {media}.')

with tab4:

    st.write('## Análise de desempenho de notas por disciplina')

    #se quiser demonstrar o código python que foi utilizado
    codigo_python ='''
        plt.subplots(1,4,figsize=(16,5))
        plt.subplot(141)
        sns.boxplot(df['math score'],color='blue')
        plt.subplot(142)
        sns.boxplot(df['reading score'],color='red')
        plt.subplot(143)
        sns.boxplot(df['writing score'],color='yellow')
        plt.subplot(144)
        sns.boxplot(df['média score'],color='orange')
        plt.show() '''

    st.code(codigo_python, language='python')
    

    plt.subplots(1,4,figsize=(16,5))
    plt.subplot(141)
    sns.boxplot(df['math score'],color='blue')
    plt.subplot(142)
    sns.boxplot(df['reading score'],color='red')
    plt.subplot(143)
    sns.boxplot(df['writing score'],color='yellow')
    plt.subplot(144)
    sns.boxplot(df['média score'],color='orange')
    
    
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()