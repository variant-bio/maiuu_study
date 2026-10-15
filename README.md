# French Polynesian Multi-Omic Resource (Ma'i 'u'u)

The Ma'i 'u'u French Polynesian resource combines whole genome sequencing (WGS) with blood metabolomic and transcriptomic profiling in a gout-focused cohort of 1,043 French Polynesian participants. It was generated through a collaboration between [Variant Bio](https://www.variantbio.com/) and Tristan Pascart's group at [Lille Catholic University](https://www.univ-catholille.fr/), and was designed and conducted alongside an extensive community consultation campaign across the five archipelagos of French Polynesia. These data were used to map genetic variants that impact blood metabolite levels, gene expression, and splicing, and to associate them with inflammatory and metabolic traits including gout, type 2 diabetes, and chronic kidney disease.

This repository contains cohort information and the summary results reported in the following manuscript, along with details on how to request access to the full summary statistics.

**Genetic and multi-omic insights into inflammation and metabolism in a French Polynesian cohort. Pascart _et al._ _Nature Communications_ (2026).**

## Repository contents

| Path | Contents |
|------|----------|
| [`data_tables/`](data_tables/) | The 24 Supplementary Data tables, one tab-delimited file each. [`data_tables/README.md`](data_tables/README.md) describes every table. |
| [`documents/daa_august_2026.pdf`](documents/daa_august_2026.pdf) | Data Access Agreement for the genome-wide summary statistics (see below). |
| [`scripts/xlsx_to_tsv.py`](scripts/xlsx_to_tsv.py) | Script that generated `data_tables/` from the Supplementary Data workbook. |

## Data tables

Gene-, locus-, and variant-level annotated summary results are provided as tab-delimited text files, one per Supplementary Data table in the manuscript. Per-table descriptions are in [data_tables/README.md](data_tables/README.md). All coordinates are in GRCh38.

### Cohort and Genomes
- Sample sizes and analysis inclusion by recruitment site - [supplementary_data_01_study_participants.txt](data_tables/supplementary_data_01_study_participants.txt)
- Cohort characteristics by sex and gout status - [supplementary_data_02_cohort_characteristics.txt](data_tables/supplementary_data_02_cohort_characteristics.txt)
- Putatively functional (CADD > 30) Polynesian-enriched alleles - [supplementary_data_03_functional_alleles.txt](data_tables/supplementary_data_03_functional_alleles.txt)
- HLA class I allele frequencies by self-reported ancestry - [supplementary_data_04_hla_allele_frequencies.txt](data_tables/supplementary_data_04_hla_allele_frequencies.txt)

### Metabolomics and Metabolite GWAS
- Metabolomics quality control summary - [supplementary_data_05_metabolomics_qc.txt](data_tables/supplementary_data_05_metabolomics_qc.txt)
- Differential metabolite quantification across five binary traits - [supplementary_data_06_metabolite_dq_results.txt](data_tables/supplementary_data_06_metabolite_dq_results.txt)
- mGWAS lead variants for all significant loci (p < 5e-8) - [supplementary_data_07_mgwas_results.txt](data_tables/supplementary_data_07_mgwas_results.txt)
- Variants from significant mGWAS signals that are rare in gnomAD - [supplementary_data_08_mgwas_gnomad_rare.txt](data_tables/supplementary_data_08_mgwas_gnomad_rare.txt)
- Metabolite associations for the alpha-globin haplotype - [supplementary_data_21_alpha_globin_variant_mgwas.txt](data_tables/supplementary_data_21_alpha_globin_variant_mgwas.txt)
- Joint modeling of disease on metabolite principal components - [supplementary_data_22_metabolite_pcs.txt](data_tables/supplementary_data_22_metabolite_pcs.txt)

### Transcriptomics and cis-QTL Mapping
- Cell type by disease association results - [supplementary_data_09_cell_type_disease.txt](data_tables/supplementary_data_09_cell_type_disease.txt)
- Differential expression of elevated CRP - [supplementary_data_10_crp_de_results.txt](data_tables/supplementary_data_10_crp_de_results.txt)
- cis-eQTL gene-level results - [supplementary_data_11_cis_eqtl_results.txt](data_tables/supplementary_data_11_cis_eqtl_results.txt)
- eVariant annotations - [supplementary_data_12_evariant_annotations.txt](data_tables/supplementary_data_12_evariant_annotations.txt)
- cis-sQTL gene-level results - [supplementary_data_13_cis_sqtl_results.txt](data_tables/supplementary_data_13_cis_sqtl_results.txt)
- sVariant annotations - [supplementary_data_14_svariant_annotations.txt](data_tables/supplementary_data_14_svariant_annotations.txt)
- Conditionally independent cis-eQTLs - [supplementary_data_15_independent_cis_eqtls.txt](data_tables/supplementary_data_15_independent_cis_eqtls.txt)
- Independent eVariant annotations - [supplementary_data_16_independent_evariant.txt](data_tables/supplementary_data_16_independent_evariant.txt)
- Genes tested and with significant QTLs by QTL and gene type - [supplementary_data_23_qtl_summary.txt](data_tables/supplementary_data_23_qtl_summary.txt)

### Genome-wide Association Studies
- Summary of all 30 GWAS, including genomic inflation and sample sizes - [supplementary_data_17_gwas_summary.txt](data_tables/supplementary_data_17_gwas_summary.txt)
- Genome-wide significant GWAS results with fine mapping - [supplementary_data_18_gwas_results.txt](data_tables/supplementary_data_18_gwas_results.txt)
- Replication of previously reported Polynesian associations - [supplementary_data_19_gwas_replication.txt](data_tables/supplementary_data_19_gwas_replication.txt)

### Colocalization
- Colocalization results across GWAS, mGWAS, and QTLs - [supplementary_data_20_colocalization_results.txt](data_tables/supplementary_data_20_colocalization_results.txt)
- Detailed colocalizations at the alpha-globin and WDR1 loci - [supplementary_data_24_detailed_colocalizations.txt](data_tables/supplementary_data_24_detailed_colocalizations.txt)

### Allele Frequency Annotations

Variants in the data tables are annotated with allele frequencies for the **alternative (ALT) allele** across the cohort, self-reported ancestry groups within the cohort, and external reference groups:

| Column | Description |
| --- | --- |
| `af_STUDY` | Entire French Polynesian cohort |
| `af_FrenchPolynesia_POL` | Entire French Polynesian cohort, Polynesian-ancestry background only (accounting for local ancestry) |
| `af_ATIS` | Self-reported Austral Islands ancestry |
| `af_MQSN` | Self-reported Marquesas Islands ancestry |
| `af_SCIS` | Self-reported Society Islands ancestry |
| `af_TMTN` | Self-reported Tuamotu Islands ancestry |
| `af_CHN` | Self-reported Chinese ancestry |
| `af_EURO` | Self-reported European ancestry |
| `af_MULTI` | Self-reported multiple ancestries |
| `af_GBR` | 1000 Genomes British |
| `af_HAN` | 1000 Genomes Han Chinese |
| `af_YOR` | 1000 Genomes Yoruba |
| `af_MALY` | Singapore Sequencing Malay Project |
| `af_GNOMAD` | gnomAD v3.1.1 |

In [supplementary_data_03_functional_alleles.txt](data_tables/supplementary_data_03_functional_alleles.txt) the `_POL` suffix denotes allele frequencies computed on the Polynesian-ancestry background, taking local ancestry into account (e.g. `af_SCIS_POL` is the Society Islands frequency on the Polynesian-ancestry background).

## Data availability

Gene, locus, and variant-level annotated summary information for GWAS, mGWAS, and QTLs is included as Supplementary Data with the manuscript and in [`data_tables/`](data_tables/).

### Genome-wide summary statistics

Full genome-wide summary statistics are available on Zenodo through controlled access:

- **Accession:** [10.5281/zenodo.22759036](https://doi.org/10.5281/zenodo.22759036)
- **Record:** <https://zenodo.org/records/22759036>

Controlled access ensures the data are used in line with participants' informed consent and the study's ethical approvals, and it respects the French Polynesian community's governance over data derived from its members. This is a small and genetically distinct population, so even aggregate data carry a greater risk of re-identification and community-level harm than in larger populations.

A Data Access Committee (DAC) oversees access. It is made up of members of the study team and a representative of the Polynesian community in Tahiti. The [Data Access Agreement (DAA)](documents/daa_august_2026.pdf) governs use of the data, and a copy is also on the Zenodo record. Under the DAA:

- the data may be used only for non-commercial research related to gout or its comorbidities;
- access requires evidence of ethical approval, such as Institutional Review Board (IRB) approval;
- recipients may not attempt to re-identify participants, share the data with third parties, or use it beyond the approved application.

To request access, apply through the Zenodo record or contact the corresponding authors. Requests receive a response within two weeks.

## Citation

If you use these data, please cite:

1. Pascart, T. *et al.* Genetic and multi-omic insights into inflammation and metabolism in a French Polynesian cohort. *Nature Communications* (2026).
2. Pascart, T. *et al.* The gout epidemic in French Polynesia: a modelling study of data from the Ma'i u'u epidemiological survey. *Lancet Global Health* 12, e685–e696 (2024).

If you use the genome-wide summary statistics, please also include the dataset identifier (10.5281/zenodo.22759036).

## Contact

- Tristan Pascart (<pascart.tristan@ghicl.net>)
- Stephane E. Castel (<stephane@variantbio.com>)
