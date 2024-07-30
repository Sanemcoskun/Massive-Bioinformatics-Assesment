# Massive Bioinformatics Assesment

This project aims to identify genetic and biological differences between SARS-CoV-2 infected and control groups using transcription data. Below are the project details and usage instructions.

## Project Structure

The following steps were carried out in this project:
1. **Filtering**: Genes that did not show expression (read count) in any condition were removed from the dataset.
2. **Differential Expression Analysis**: Genes that showed significant changes between the two conditions were identified.
3. **Enrichment Analysis**: The list of significantly altered genes was subjected to enrichment analysis using gProfiler.

![image](https://github.com/user-attachments/assets/164184c3-9e98-4153-b156-36d4574d16e3)

4. **Gene ID Conversion**: The Ensembl IDs of the significantly changed genes were converted to Entrez IDs.For the conversion from Ensembl ID to Entrez ID, I utilized the Galaxy Informatics site. Upon conversion, I observed an increase in the number of Entrez IDs. After filtering and examining, I found that some Ensembl IDs had multiple Entrez IDs for different subtypes.

For example, the Ensembl ID ENSG00000288905 has two different Entrez IDs.

![image](https://github.com/user-attachments/assets/fb69769a-c12b-4762-8905-097fefc9da2f)

5. **Pathway Analysis**: Related pathways obtained from the enrichment analysis were listed.

For example:

![image](https://github.com/user-attachments/assets/f0b364cd-2f0b-47d9-8fcc-38c877bdecd9)

6. **Results Interpretation**: The obtained results were interpreted and reported.

For more detailed information, you can review the PDF file in the GitHub repository. If there are any deficiencies, please do not forget to let me know.


