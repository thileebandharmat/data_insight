import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

students = [('jack', 34, 'Sydeny'),
('Riti', 30, 'Delhi'),
('Aadi', 16, 'New York'),
('Riti', 30, 'Delhi'),
('Riti', 30, 'Delhi'),
('Riti', 30, 'Mumbai'),
('Aadi', 40, 'London'),
('Sachin', 30, 'Delhi')
]
# Create a DataFrame object
source = pd.read_csv('F:\Thileeban\python\\\Data_2.csv')
print(source.head())

root_path = 'F:\Thileeban\python\\'
folder = 'Visuals'
output_path = os.path.join(root_path, folder)
os.mkdir(output_path)
for col in list(source.columns):
    if len(source[col].unique()) < 21:
        filename = 'Count_plot_'+col+'.png'
        file_full_name = os.path.join(output_path, filename)
        sns_plot = sns.countplot(x=col, data=source)
        fig = sns_plot.get_figure()
        fig.savefig(file_full_name)
    elif (len(source[col].unique()) > 21) & (source[col].dtypes in ['int64', 'float64']):
        filename = 'Dist_plot_' + col + '.png'
        file_full_name = os.path.join(output_path, filename)
        sns_plot = sns.distplot(source[col], hist=True, bins=50)
        #sns_plot = sns.distplot(source[col])
        fig = sns_plot.get_figure()
        fig.savefig(file_full_name)



'''
sns_plot = sns.pairplot(data=source)
sns_plot.savefig('F:\Thileeban\python\\pair_plot.png')
plt.show()'''

#sns.countplot(x='pk_1', data=source)