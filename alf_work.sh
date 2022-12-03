#！/bin/bash
set -e

if [[ $# -eq 0 ]]; then
  echo "Error: input path must be provided as an input argument."
  exit 1
fi

Database_DIR="./database"
Input_DIR="./alf_input"
Output_DIR="/media/ygb/Database/alphafold/alf_output"

echo "Prediction Starts..."
echo "Protein sequence file: /alf_input/$1"
echo ""

python3 alphafold/docker/run_docker.py \
  --fasta_paths="${Input_DIR}/$1" \
  --max_template_date=2022-12-02 \
  --data_dir="$Database_DIR" \
  --output_dir="${Output_DIR}"
  
  
echo "Prediction Finished."
echo "Protein sequence file: ${Input_DIR}/$1"
echo "Protein sequence file: ${Output_DIR}"
