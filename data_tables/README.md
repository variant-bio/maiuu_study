# Supplementary Data Tables

Tab-delimited text versions of the Supplementary Data tables from Pascart *et al.*, *Genetic and multi-omic insights into inflammation and metabolism in a French Polynesian cohort*. Each file matches one sheet of the Supplementary Data workbook that accompanies the manuscript.

## Format

- Files are UTF-8, tab-delimited, and have a single header row.
- Empty fields are missing values.
- Allele frequencies and effect sizes refer to the alternative (ALT) allele unless a table says otherwise.
- Variant keys use the format `chr_position_ref_alt` (GRCh38).
- **Table 2 (Cohort Characteristics)** was reshaped from its display layout: each row is one characteristic, subgroup rows carry their section as a prefix (for example `Self-reported Conditions: Gout (N, %)`), and the column headers include the group sizes. Quantitative traits are shown as mean (SD) and conditions as N (%).
- **Table 4 (HLA Allele Frequencies)**: the `HLA gene` column is filled in on every row. The workbook lists it only on the first row of each gene.

## Index

| # | File | Table | Rows |
|---|------|-------|-----:|
| 1 | [`supplementary_data_01_study_participants.txt`](supplementary_data_01_study_participants.txt) | Study Participants | 9 |
| 2 | [`supplementary_data_02_cohort_characteristics.txt`](supplementary_data_02_cohort_characteristics.txt) | Cohort Characteristics | 33 |
| 3 | [`supplementary_data_03_functional_alleles.txt`](supplementary_data_03_functional_alleles.txt) | Functional Alleles | 79 |
| 4 | [`supplementary_data_04_hla_allele_frequencies.txt`](supplementary_data_04_hla_allele_frequencies.txt) | HLA Allele Frequencies | 22 |
| 5 | [`supplementary_data_05_metabolomics_qc.txt`](supplementary_data_05_metabolomics_qc.txt) | Metabolomics QC | 1,020 |
| 6 | [`supplementary_data_06_metabolite_dq_results.txt`](supplementary_data_06_metabolite_dq_results.txt) | Metabolite DQ Results | 1,093 |
| 7 | [`supplementary_data_07_mgwas_results.txt`](supplementary_data_07_mgwas_results.txt) | mGWAS Results | 534 |
| 8 | [`supplementary_data_08_mgwas_gnomad_rare.txt`](supplementary_data_08_mgwas_gnomad_rare.txt) | mGWAS gnomAD Rare | 1,608 |
| 9 | [`supplementary_data_09_cell_type_disease.txt`](supplementary_data_09_cell_type_disease.txt) | Cell Type Disease | 200 |
| 10 | [`supplementary_data_10_crp_de_results.txt`](supplementary_data_10_crp_de_results.txt) | CRP DE Results | 14,799 |
| 11 | [`supplementary_data_11_cis_eqtl_results.txt`](supplementary_data_11_cis_eqtl_results.txt) | cis-eQTL Results | 16,949 |
| 12 | [`supplementary_data_12_evariant_annotations.txt`](supplementary_data_12_evariant_annotations.txt) | eVariant Annotations | 8,893 |
| 13 | [`supplementary_data_13_cis_sqtl_results.txt`](supplementary_data_13_cis_sqtl_results.txt) | cis-sQTL Results | 10,976 |
| 14 | [`supplementary_data_14_svariant_annotations.txt`](supplementary_data_14_svariant_annotations.txt) | sVariant Annotations | 2,037 |
| 15 | [`supplementary_data_15_independent_cis_eqtls.txt`](supplementary_data_15_independent_cis_eqtls.txt) | Independent cis-eQTLs | 9,062 |
| 16 | [`supplementary_data_16_independent_evariant.txt`](supplementary_data_16_independent_evariant.txt) | Independent eVariant | 16,598 |
| 17 | [`supplementary_data_17_gwas_summary.txt`](supplementary_data_17_gwas_summary.txt) | GWAS Summary | 30 |
| 18 | [`supplementary_data_18_gwas_results.txt`](supplementary_data_18_gwas_results.txt) | GWAS Results | 31 |
| 19 | [`supplementary_data_19_gwas_replication.txt`](supplementary_data_19_gwas_replication.txt) | GWAS Replication | 16 |
| 20 | [`supplementary_data_20_colocalization_results.txt`](supplementary_data_20_colocalization_results.txt) | Colocalization Results | 117 |
| 21 | [`supplementary_data_21_alpha_globin_variant_mgwas.txt`](supplementary_data_21_alpha_globin_variant_mgwas.txt) | Alpha Globin Variant mGWAS | 29 |
| 22 | [`supplementary_data_22_metabolite_pcs.txt`](supplementary_data_22_metabolite_pcs.txt) | Metabolite PCs | 50 |
| 23 | [`supplementary_data_23_qtl_summary.txt`](supplementary_data_23_qtl_summary.txt) | QTL Summary | 4 |
| 24 | [`supplementary_data_24_detailed_colocalizations.txt`](supplementary_data_24_detailed_colocalizations.txt) | Detailed Colocalizations | 26 |

## Descriptions

### 1. Study Participants

File: [`supplementary_data_01_study_participants.txt`](supplementary_data_01_study_participants.txt)

Study Participants. Sample size, median age, number of males and females, and number of individuals included in each downstream analysis stratified by recruitment site.

### 2. Cohort Characteristics

File: [`supplementary_data_02_cohort_characteristics.txt`](supplementary_data_02_cohort_characteristics.txt)

Cohort Characteristics. Means of quantitative traits and percentages of self-reported conditions across all study participants and stratified by sex and gout status.

### 3. Functional Alleles

File: [`supplementary_data_03_functional_alleles.txt`](supplementary_data_03_functional_alleles.txt)

Functional Alleles. Annotated variants that are predicted to have high functional impact (CADD > 30), present at MAF > 1% on the Polynesian-ancestry background in the cohort and unobserved in non-Polynesian ancestry groups. Variants were queried in ClinVar by rsID for any associated entries, and any conditions and classifications are listed (clinvar_condition, clinvar_classification). Allele frequencies are provided for the alternative (ALT) allele.

### 4. HLA Allele Frequencies

File: [`supplementary_data_04_hla_allele_frequencies.txt`](supplementary_data_04_hla_allele_frequencies.txt)

HLA Allele Frequencies. Frequencies of called HLA alleles stratified by self-reported ancestry and including reference populations.

### 5. Metabolomics QC

File: [`supplementary_data_05_metabolomics_qc.txt`](supplementary_data_05_metabolomics_qc.txt)

Metabolomics quality control summary. Summary statistics for batch normalized, imputed, and log-transformed metabolite quantifications measured by Metabolon in dried blood spot samples. The number of samples with metabolite detected versus not detected and imputed are listed. Transformation used for mGWAS is listed for each metabolite as either inverse normal transformation (INT) for continuously distributed metabolites, or binarization (BIN) for metabolites where >50% of samples were imputed. mGWAS were run for all INT-transformed metabolites and BIN-transformed metabolites with >= 50 non-imputed values.

### 6. Metabolite DQ Results

File: [`supplementary_data_06_metabolite_dq_results.txt`](supplementary_data_06_metabolite_dq_results.txt)

Metabolite DQ Results. Results from differential metabolite quantification analyses across binary traits: chronic kidney disease (CKD), elevated CRP (crp_high), gout, obesity, and type 2 diabetes (t2d). P-values (p_value) are from a two-sided moderated t-test (limma), age- and sex-adjusted, with Benjamini–Hochberg corrected values (p_adj) provided.

### 7. mGWAS Results

File: [`supplementary_data_07_mgwas_results.txt`](supplementary_data_07_mgwas_results.txt)

mGWAS Results. Annotated results for the lead variant in each genome-wide nominally significantly associated locus for all metabolite GWAS (p < 5e-8). Results are flagged if they are also significant after Bonferroni multiple testing correction across metabolites (mt_sig). Posterior probability from finemap for the lead variant is listed for each association (fm_prob). Loci were defined globally to capture those associated with multiple metabolites (global_locus). Annotations for the lead variant are listed (VEP, CADD, frequencies). Allele frequencies are provided for the alternative (ALT) allele (af_XXX) and the minor (maf). All mGWAS p-values (p_value) are two-sided from linear mixed model analyses.

### 8. mGWAS gnomAD Rare

File: [`supplementary_data_08_mgwas_gnomad_rare.txt`](supplementary_data_08_mgwas_gnomad_rare.txt)

Variants from metabolite association signals that were significant after multiple testing correction and rare in gnomAD. Variants from Bonferroni multiple testing correction significant metabolite association signals that were rare in gnomAD (MAF < 0.001). For each variant, annotations and mGWAS summary statistics are provided, and the lead variant in the signal (top_variant) and the global locus (global_locus) are indicated. All mGWAS p-values (p_value) are two-sided from linear mixed model analyses.

### 9. Cell Type Disease

File: [`supplementary_data_09_cell_type_disease.txt`](supplementary_data_09_cell_type_disease.txt)

Cell Type Disease Associations. Results from a logistic regression model of disease ~ cell type for each cell type by disease comparison. P-values (pval) are two-sided and adjusted for multiple testing across all comparisons using the Benjamini–Hochberg method (p_adj).

### 10. CRP DE Results

File: [`supplementary_data_10_crp_de_results.txt`](supplementary_data_10_crp_de_results.txt)

CRP DE Results. Results from blood differential expression analysis in gout cases of elevated CRP. P-values (p_value) are from a two-sided moderated t-test (limma), age- and sex-adjusted, and Benjamini–Hochberg corrected (p_adj).

### 11. cis-eQTL Results

File: [`supplementary_data_11_cis_eqtl_results.txt`](supplementary_data_11_cis_eqtl_results.txt)

cis-eQTL Results. Gene-level permutation results from eQTL mapping using fastQTL. Columns are the standard outputs from fastQTL run in permutation mode. In column names “ma” means “minor allele”. Slope is always provided for the alternative allele. Briefly, fastQTL p-values are two-sided and provided as nominal (linear regression; pval_nominal), permutation-based (pval_perm), and multiple-testing corrected by Storey's q-value method (qval).

### 12. eVariant Annotations

File: [`supplementary_data_12_evariant_annotations.txt`](supplementary_data_12_evariant_annotations.txt)

eVariant Annotations. Annotations for all unique, lead variants for significant eQTLs (eVariants). Allele frequencies are provided for the alternative (ALT) allele.

### 13. cis-sQTL Results

File: [`supplementary_data_13_cis_sqtl_results.txt`](supplementary_data_13_cis_sqtl_results.txt)

cis-sQTL Results. Gene-level permutation results from sQTL mapping using fastQTL. Columns are the standard outputs from fastQTL run in permutation mode. In column names “ma” means “minor allele”. Slope is always provided for the alternative allele. Briefly, fastQTL p-values are two-sided and provided as nominal (linear regression; pval_nominal), permutation-based (pval_perm), and multiple-testing corrected by Storey's q-value method (qval).

### 14. sVariant Annotations

File: [`supplementary_data_14_svariant_annotations.txt`](supplementary_data_14_svariant_annotations.txt)

sVariant Annotations. Annotations for all unique, lead variants for significant sQTLs (sVariants). Allele frequencies are provided for the alternative (ALT) allele.

### 15. Independent cis-eQTLs

File: [`supplementary_data_15_independent_cis_eqtls.txt`](supplementary_data_15_independent_cis_eqtls.txt)

Independent cis-eQTLs. Gene-level results from conditional eQTL analysis, with nominal two-sided p-value threshold used for conditional analysis (linear regression, p_value_threshold), number of conditionally independent eQTLs mapped (independent_signals), and variant IDs (variant_ids). Includes a flag indicating whether an error occurred before reaching 20 independent eQTLs (error).

### 16. Independent eVariant

File: [`supplementary_data_16_independent_evariant.txt`](supplementary_data_16_independent_evariant.txt)

Independent eVariant Annotations. Annotations for all unique, lead variants for conditionally independent eQTLs. Allele frequencies are provided for the alternative (ALT) allele.

### 17. GWAS Summary

File: [`supplementary_data_17_gwas_summary.txt`](supplementary_data_17_gwas_summary.txt)

GWAS Summary. Results from GWAS of 30 traits with type of trait (binary or quantitative), sample size, genomic inflation (lambda_gc), and genome-wide significant variants (hits) and loci.

### 18. GWAS Results

File: [`supplementary_data_18_gwas_results.txt`](supplementary_data_18_gwas_results.txt)

GWAS Results. Genome-wide significant, variant-level results from GWAS with the top three variants by finemap posterior probability in the 95% credible set shown for each locus/association (fm_prob, fm_index). Loci were defined globally to capture those associated with multiple phenotypes (global_locus). Allele frequencies are provided for the alternative (ALT) allele (af_XXX) and the minor (maf). All p-values are two-sided from linear mixed model analyses.

### 19. GWAS Replication

File: [`supplementary_data_19_gwas_replication.txt`](supplementary_data_19_gwas_replication.txt)

Replication of Polynesian Associations. Replication of Polynesian-enriched functional variants that were identified in previous association studies, replicated in this cohort. Betas and allele frequencies are provided for the alternative allele (ALT). All p-values are two-sided from linear mixed model analyses and 95% confidence intervals are provided (ci_lower, ci_upper).

### 20. Colocalization Results

File: [`supplementary_data_20_colocalization_results.txt`](supplementary_data_20_colocalization_results.txt)

Colocalization Results. Results with PP4 > 0.50 from colocalization analysis including variant explaining maximum proportion of PP4 (coloc_variant), proportion of H4 explained by coloc_variant (coloc_variant_H4), mGWAS/QTL beta (beta_qtl), GWAS beta (beta_gwas), mGWAS/QTL nominal p-value (pvalue_qtl), and GWAS p-value (pvalue_gwas). Betas and allele frequencies are provided for the alternative allele (ALT). All GWAS p-values are two-sided from linear mixed model analyses, and QTL p-values are two-sided from linear regression analyses.

### 21. Alpha Globin Variant mGWAS

File: [`supplementary_data_21_alpha_globin_variant_mgwas.txt`](supplementary_data_21_alpha_globin_variant_mgwas.txt)

Alpha Globin Variant mGWAS. Significant metabolite associations for the Polynesian-enriched alpha-globin haplotype tagged by rs537451609 (Benjamini–Hochberg FDR < 5% across all quantitative blood metabolites). Summary statistics are derived from the same model used for metabolite GWAS. Betas and 95% confidence intervals for the betas are provided for the alternative allele (ALT). All p-values are two-sided from linear mixed model analyses.

### 22. Metabolite PCs

File: [`supplementary_data_22_metabolite_pcs.txt`](supplementary_data_22_metabolite_pcs.txt)

Estimates from joint modeling of disease on metabolite principal components.

### 23. QTL Summary

File: [`supplementary_data_23_qtl_summary.txt`](supplementary_data_23_qtl_summary.txt)

Number of genes tested and with significant QTLs (FDR < 5%) split by expression and splice QTLs and by gene type.

### 24. Detailed Colocalizations

File: [`supplementary_data_24_detailed_colocalizations.txt`](supplementary_data_24_detailed_colocalizations.txt)

Colocalization posterior probabilities from analyses of metabolites and gene expression at the alpha-globin and WDR1 loci.
