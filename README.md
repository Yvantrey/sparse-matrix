# Sparse Matrix Operations

## Overview
This program performs various operations on sparse matrices, including addition, subtraction, multiplication, and transposition. It reads matrices from input files, processes them, and saves the results to output files.

## Features
- Load sparse matrices from text files
- Perform matrix operations:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Transposition (T)
- Save results of operations to output files
- Interactive command-line interface with error handling
- Displays matrix dimensions and non-zero elements count

## Prerequisites
- Python 3.11 or higher
- Required Python package: `colorama`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Yvantrey/sparse-matrix.git
   cd sparse-matrix
   ```
2. Install the required package:
   ```bash
   pip install colorama
   ```

## Directory Structure
```
.
├── src
│   ├── main.py  # Main script with CLI interface
│   ├── sparse_matrix.py  # SparseMatrix class
│   ├── addition.py  # Addition functionality
│   ├── subtraction.py  # Subtraction functionality
│   ├── multiplication.py  # Multiplication functionality
│   ├── transpose.py  # Transposition functionality
├── sample_inputs
│   ├── matrix1.txt  # Example input matrix
│   ├── matrix2.txt  # Example input matrix
├── results  # Stores output files
└── README.md
```

## Usage
### Running the Program
1. Navigate to the `src` directory:
   ```bash
   cd src
   ```
2. Run the script:
   ```bash
   python main.py
   ```
3. Follow the on-screen instructions to select and execute matrix operations.

### Input File Format
- Each line represents a row of the matrix.
- Elements in a row are separated by spaces.
- Example input file (`matrix1.txt`):
  ```
  5 0 0 8
  0 0 3 0
  2 0 0 0
  ```

### Output Files
The results are saved in the `results` directory:
- `addition_result.txt`
- `subtraction_result.txt`
- `multiply_result.txt`
- `transpose_result_matrix1.txt`
- `transpose_result_matrix2.txt`

## Code Overview
- `main.py`: Provides an interactive CLI for operations.
- `sparse_matrix.py`: Defines the `SparseMatrix` class for handling sparse matrices.
- `addition.py`: Implements matrix addition.
- `subtraction.py`: Implements matrix subtraction.
- `multiplication.py`: Implements matrix multiplication.
- `transpose.py`: Implements matrix transposition.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements
- [Colorama](https://pypi.org/project/colorama/) for colored terminal text.

## Contact
For questions or suggestions, contact: [y.rugamba@alustudent.com]
Thank you!
