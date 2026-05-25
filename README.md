# Pipeline Bioinformático con HMMER y Pfam

## Descripción del proyecto

Este proyecto implementa un pipeline bioinformático para la identificación de familias de proteínas utilizando HMMER (hmmscan) y una base de datos reducida de Pfam.

El objetivo es comparar secuencias proteicas con modelos ocultos de Markov (HMMs) para identificar posibles familias funcionales y relaciones evolutivas.

---

## Estructura del proyecto
## Estructura del proyecto

El proyecto está organizado de la siguiente manera:

hmmer_pipeline/
│
├── data/
│   ├── Pfam_subset.hmm
│   ├── proteins.fasta
│   ├── family_names_clean.txt
│
├── results/
│   └── results.txt
│
├── scripts/
│   ├── run_hmmscan.sh
│   └── protein.py
│
├── docs/
├── README.md
└── .gitignore# Pipeline bioinformático con HMMER y Pfam

## Descripción

Este proyecto tiene como objetivo identificar familias proteicas mediante el uso de HMMER y la base de datos Pfam.

El pipeline permite comparar secuencias proteicas contra modelos ocultos de Markov (HMMs) para detectar similitudes evolutivas y asignar familias funcionales.

## Objetivos

- Instalar y configurar HMMER
- Organizar un pipeline bioinformático reproducible
- Analizar secuencias proteicas con hmmscan
- Identificar familias proteicas utilizando Pfam
- Automatizar el análisis mediante scripts

## Estructura del proyecto

```text
hmmer_pipeline/
│
├── data/
├── results/
├── scripts/
├── docs/
├── README.md
└── .gitignore

