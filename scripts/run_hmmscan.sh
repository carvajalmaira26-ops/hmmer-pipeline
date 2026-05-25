#!/bin/bash

echo "Iniciando análisis con HMMER..."

hmmscan ../data/Pfam_subset.hmm ../data/proteins.fasta > ../results/results.txt

echo "Análisis terminado"

echo "Resultados guardados en results/results.txt"
