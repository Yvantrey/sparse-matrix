import os
from sparse_matrix import SparseMatrix
from addition import add_matrices
from subtraction import subtract_matrices
from multiplication import multiply_matrices
from transpose import transpose_matrix
from colorama import init, Fore, Style

def ensure_results_directory():
    """Create results directory if it doesn't exist"""
    results_dir = "../../results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    return results_dir

def process_matrices(file1_path, file2_path):
    """Process matrices with all operations and save results"""
    try:
        # Create results directory
        results_dir = ensure_results_directory()
        
        # Load matrices
        print(f"\nLoading matrices from:")
        print(f"Matrix 1: {file1_path}")
        print(f"Matrix 2: {file2_path}")
        
        matrix1 = SparseMatrix(file1_path)
        matrix2 = SparseMatrix(file2_path)
        
        print(f"\nMatrix 1 dimensions: {matrix1.rows}x{matrix1.cols} ({matrix1.nnz} non-zero elements)")
        print(f"Matrix 2 dimensions: {matrix2.rows}x{matrix2.cols} ({matrix2.nnz} non-zero elements)")
        
        # Perform multiplication
        try:
            print("\nPerforming multiplication...")
            result = multiply_matrices(matrix1, matrix2)
            output_file = f"{results_dir}/multiply_result.txt"
            result.save_to_file(output_file)
            print(f"Saved multiplication result to: {output_file}")
        except Exception as e:
            print(f"Error in multiplication: {str(e)}")
            
        # Perform addition
        try:
            print("\nPerforming addition...")
            if (matrix1.rows, matrix1.cols) != (matrix2.rows, matrix2.cols):
                print("Matrices have different dimensions. Transposing Matrix 2 for addition...")
                matrix2 = transpose_matrix(matrix2)
            result = add_matrices(matrix1, matrix2)
            output_file = f"{results_dir}/addition_result.txt"
            result.save_to_file(output_file)
            print(f"Saved addition result to: {output_file}")
        except Exception as e:
            print(f"Error in addition: {str(e)}")
            
        # Perform subtraction
        try:
            print("\nPerforming subtraction...")
            if (matrix1.rows, matrix1.cols) != (matrix2.rows, matrix2.cols):
                print("Matrices have different dimensions. Transposing Matrix 2 for subtraction...")
                matrix2 = transpose_matrix(matrix2)
            result = subtract_matrices(matrix1, matrix2)
            output_file = f"{results_dir}/subtraction_result.txt"
            result.save_to_file(output_file)
            print(f"Saved subtraction result to: {output_file}")
        except Exception as e:
            print(f"Error in subtraction: {str(e)}")
        
        print("\nAll operations completed!")
        
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    """Interactive matrix operations with enhanced validation"""
    print(Fore.GREEN + Style.BRIGHT + "\n \t \tDAVID BIRENZI")
    print(Fore.GREEN + Style.BRIGHT + "Welcome to the Sparse Matrix Operations program!")
    print("*****************************************************")

    # Get input files
    print("\nEnter the paths to the input files:")
    file1 = input("First matrix file path / press Enter for default: ").strip()
    file2 = input("Second matrix file path / press Enter for default: ").strip()
    
    # Use default file paths if not provided
    if not file1:
        file1 = "../../sample_inputs/matrix1.txt"
    if not file2:
        file2 = "../../sample_inputs/matrix2.txt"
    
    while True:
        print("\nAvailable operations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Transpose (T)")
        print("5. All operations")
        print("6. View matrix information")
        print("7. Exit")
        
        choice = input("\nSelect operation (1-7): ").strip()
        
        if choice == '7':
            print("\nExiting program...")
            break
            
        try:
            results_dir = ensure_results_directory()
            
            # Load matrices
            print(f"\nLoading matrices from:")
            print(f"Matrix 1: {file1}")
            print(f"Matrix 2: {file2}")
            
            matrix1 = SparseMatrix(file1)
            matrix2 = SparseMatrix(file2)
            
            print(f"\nMatrix 1 dimensions: {matrix1.rows}x{matrix1.cols} ({matrix1.nnz} non-zero elements)")
            print(f"Matrix 2 dimensions: {matrix2.rows}x{matrix2.cols} ({matrix2.nnz} non-zero elements)")
            
            if choice == '6':
                continue
            
            if choice in ['1', '5']:  # Addition
                try:
                    print("\nPerforming addition (+)...")
                    if (matrix1.rows, matrix1.cols) != (matrix2.rows, matrix2.cols):
                        print("Matrices have different dimensions. Transposing Matrix 2 for addition...")
                        matrix2 = transpose_matrix(matrix2)
                    result = add_matrices(matrix1, matrix2)
                    output_file = f"{results_dir}/addition_result.txt"
                    result.save_to_file(output_file)
                    print(f"Saved addition result to: {output_file}")
                except Exception as e:
                    print(f"Error in addition: {str(e)}")
            
            if choice in ['2', '5']:  # Subtraction
                try:
                    print("\nPerforming subtraction (-)...")
                    if (matrix1.rows, matrix1.cols) != (matrix2.rows, matrix2.cols):
                        print("Matrices have different dimensions. Transposing Matrix 2 for subtraction...")
                        matrix2 = transpose_matrix(matrix2)
                    result = subtract_matrices(matrix1, matrix2)
                    output_file = f"{results_dir}/subtraction_result.txt"
                    result.save_to_file(output_file)
                    print(f"Saved subtraction result to: {output_file}")
                except Exception as e:
                    print(f"Error in subtraction: {str(e)}")
            
            if choice in ['3', '5']:  # Multiplication
                try:
                    print("\nPerforming multiplication (*) ...")
                    result = multiply_matrices(matrix1, matrix2)
                    output_file = f"{results_dir}/multiply_result.txt"
                    result.save_to_file(output_file)
                    print(f"Saved multiplication result to: {output_file}")
                except Exception as e:
                    print(f"Error in multiplication: {str(e)}")
            
            if choice == '4':  # Transpose
                try:
                    print("\nPerforming transpose on Matrix 1...")
                    result = transpose_matrix(matrix1)
                    output_file = f"{results_dir}/transpose_result_matrix1.txt"
                    result.save_to_file(output_file)
                    print(f"Saved transpose result of Matrix 1 to: {output_file}")
                    
                    print("\nPerforming transpose on Matrix 2...")
                    result = transpose_matrix(matrix2)
                    output_file = f"{results_dir}/transpose_result_matrix2.txt"
                    result.save_to_file(output_file)
                    print(f"Saved transpose result of Matrix 2 to: {output_file}")
                except Exception as e:
                    print(f"Error in transpose: {str(e)}")
            
            if choice not in ['1', '2', '3', '4', '5', '6']:
                print("\nInvalid choice! Please select 1-7.")
                continue
                
            print("\nOperations completed!")
            
        except Exception as e:
            print(f"\nError: {str(e)}")
        
        input("\nPress Enter to continue...")
     # Print the message with colorama
    print(Fore.YELLOW + Style.BRIGHT + "Thank you for using the program!")

if __name__ == "__main__":
    main()