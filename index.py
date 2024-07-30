import pandas as pd
from scipy.stats import ttest_ind

file_path = 'assesment_dataset.tsv'
data = pd.read_csv(file_path, sep='\t')

#filtreleme işlemi

filtered_data = data[(data['mock_rep1'] > 0) | (data['mock_rep2'] > 0) | (data['mock_rep3'] > 0) |
                     (data['sars_cov_rep1'] > 0) | (data['sars_cov_rep2'] > 0) | (data['sars_cov_rep3'] > 0)]

print(filtered_data.head())

filtered_file_path = 'filtered_assesment_dataset.tsv'
filtered_data.to_csv(filtered_file_path, sep='\t', index=False)

print(f"Filtrelenmiş veri seti kaydedildi: {filtered_file_path}")

#diferansiyel ifade analizi
file_path = 'filtered_assesment_dataset.tsv'
data = pd.read_csv(file_path, sep='\t')

mock_cols = ['mock_rep1', 'mock_rep2', 'mock_rep3']
sars_cols = ['sars_cov_rep1', 'sars_cov_rep2', 'sars_cov_rep3']

p_values = []

for index, row in data.iterrows():
    mock_values = row[mock_cols].values.astype(float)
    sars_values = row[sars_cols].values.astype(float)
    t_stat, p_value = ttest_ind(mock_values, sars_values, equal_var=False)  # Welch's t-test
    p_values.append(p_value)

data['p_value'] = p_values

significant_genes = data[data['p_value'] < 0.05]

significant_file_path = 'significant_genes_pvalue.tsv'
significant_genes.to_csv(significant_file_path, sep='\t', index=False)


#Galaxy bioinformatics de kullanmak için csv formatına çevirdim
tsv_file_path = 'significant_genes_pvalue.tsv'
csv_file_path = 'significant.csv'

df = pd.read_csv(tsv_file_path, sep='\t')
df.to_csv(csv_file_path, index=False)

print(f"TSV dosyası başarıyla {csv_file_path} olarak kaydedildi.")



