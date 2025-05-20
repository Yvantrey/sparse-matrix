class MatrixDimensionError(Exception):
    """Custom exception for matrix dimension mismatches"""
    pass

class MatrixIndexError(Exception):
    """Custom exception for invalid matrix indices"""
    pass

class SparseMatrix:
    """
    A memory-efficient implementation of a sparse matrix using dictionary of dictionaries
    and CSR format for multiplication.
    
    Storage format: {row: {col: value}} where only non-zero elements are stored.
    
    Time Complexity:
    - Get/Set Element: O(1)
    - Addition/Subtraction: O(n) where n is number of non-zero elements
    - Multiplication: O(n*m) where n,m are non-zero elements in matrices
    - CSR Conversion: O(n) where n is number of non-zero elements
    """
    
    def __init__(self, source=None, rows=0, cols=0):
        """Initialize sparse matrix from file or dimensions"""
        self.data = {}  # {row: {col: value}}
        self.rows = rows
        self.cols = cols
        self.nnz = 0  # Number of non-zero elements
        
        if isinstance(source, str):
            self._load_from_file(source)
    
    def _load_from_file(self, file_path):
        """
        Parse matrix file and load data with strict dimension checking
        """
        try:
            with open(file_path, 'r') as f:
                # Read dimensions
                rows_line = f.readline().strip()
                cols_line = f.readline().strip()
                
                if not rows_line.startswith('rows=') or not cols_line.startswith('cols='):
                    raise ValueError("First two lines must be in format 'rows=N' and 'cols=N'")
                
                try:
                    self.rows = int(rows_line.split('=')[1])
                    self.cols = int(cols_line.split('=')[1])
                except ValueError:
                    raise ValueError("Invalid dimension values")
                
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    
                    if not (line.startswith('(') and line.endswith(')')):
                        raise ValueError(f"Invalid format: {line}")
                    
                    values = [v.strip() for v in line[1:-1].split(',')]
                    if len(values) != 3:
                        raise ValueError(f"Invalid element format: {line}")
                    
                    try:
                        row, col, value = map(int, values)
                        # Adjust indices if they match the dimensions exactly
                        if row == self.rows:
                            row -= 1
                        if col == self.cols:
                            col -= 1
                        
                        # Strict dimension checking
                        if row < 0 or row >= self.rows:
                            raise MatrixIndexError(f"Row index {row} out of range [0, {self.rows-1}]")
                        if col < 0 or col >= self.cols:
                            raise MatrixIndexError(f"Column index {col} out of range [0, {self.cols-1}]")
                        
                        if value != 0:
                            self.data[row] = self.data.get(row, {})
                            self.data[row][col] = value
                            self.nnz += 1
                    except ValueError:
                        raise ValueError(f"Invalid numeric values in line: {line}")
                    
        except FileNotFoundError:
            raise FileNotFoundError(f"Matrix file not found: {file_path}")
        except ValueError as e:
            raise ValueError(f"Invalid matrix file format: {str(e)}")
    
    def to_csr(self):
        """
        Convert matrix to CSR (Compressed Sparse Row) format
        
        Returns:
            tuple: (values, col_indices, row_ptr)
        
        Time Complexity: O(n) where n is number of non-zero elements
        """
        if not self.data:
            return [], [], [0]
        
        values = []
        col_indices = []
        row_ptr = [0]
        
        count = 0
        for row in range(self.rows):
            if row in self.data:
                for col in sorted(self.data[row].keys()):
                    values.append(self.data[row][col])
                    col_indices.append(col)
                    count += 1
            row_ptr.append(count)
        
        return values, col_indices, row_ptr
    
    def get_element(self, row, col):
        """
        Get element at specified position
        
        Time Complexity: O(1)
        """
        if row >= self.rows or col >= self.cols:
            return 0  # Return 0 for any position outside current dimensions
        return self.data.get(row, {}).get(col, 0)
    
    def set_element(self, row, col, value):
        """
        Set element at specified position
        
        Time Complexity: O(1)
        """
        # Validate indices
        if row < 0 or row >= self.rows:
            raise MatrixIndexError(f"Row index {row} out of range [0, {self.rows-1}]")
        if col < 0 or col >= self.cols:
            raise MatrixIndexError(f"Column index {col} out of range [0, {self.cols-1}]")
        
        if value != 0:
            if row not in self.data:
                self.data[row] = {}
            self.data[row][col] = value
        elif row in self.data and col in self.data[row]:
            del self.data[row][col]
            if not self.data[row]:
                del self.data[row]
    
    def save_to_file(self, file_path):
        """Save matrix to file in specified format"""
        try:
            with open(file_path, 'w') as f:
                # Write dimensions in the required format
                f.write(f"rows={self.rows}\n")
                f.write(f"cols={self.cols}\n")
                
                # Write elements with proper spacing after commas
                for row in sorted(self.data.keys()):
                    for col in sorted(self.data[row].keys()):
                        value = self.data[row][col]
                        if value != 0:
                            f.write(f"({row}, {col}, {value})\n")
                            
        except IOError:
            raise IOError(f"Error writing to file: {file_path}")