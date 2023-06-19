import numpy as np
def calculate(list):
    if len(list != 9):
        print('List msust contain 9 numbers.')
    # Reshaping list
    matrix = np.array(list).reshape(3,3)

    # Calculating statistics
    result = {
    'Mean': [np.mean(matrix, axis= 0).tolist(),
             np.mean(matrix, axis= 1).tolist(),
             np.mean(matrix)],
             
    'Variance': [np.var(matrix, axis= 0).tolist(),
                 np.var(matrix, axis= 1).tolist(),
                 np.var(matrix)],
                 
    'Standard Deviation': [np.std(matrix, axis= 0).tolist(),
                            np.std(matrix, axis= 1).tolist(),
                            np.std(matrix)],
                            
    'Max': [np.max(matrix, axis= 0).tolist(),
            np.max(matrix, axis= 1).tolist(),
            np.max(matrix)],
            
    'Min': [np.min(matrix, axis= 0).tolist(),
            np.min(matrix, axis= 1).tolist(),
            np.min(matrix)],
            
    'Sum': [np.sum(matrix, axis= 0).tolist(),
            np.sum(matrix, axis= 1).tolist(),
            np.sum(matrix)]
    }
    return calculations;
