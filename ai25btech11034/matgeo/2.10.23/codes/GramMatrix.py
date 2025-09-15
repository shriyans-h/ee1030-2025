import numpy as np

def gram_matrix_and_determinant(vectors):
    # Convert list of vectors into numpy array
    V = np.array(vectors, dtype=float)
    
    # Compute Gram matrix: G = V @ V.T
    G = V @ V.T
    
    # Compute determinant
    det_G = np.linalg.det(G)
    
    return G, det_G

if __name__ == "__main__":
    # Take input for 3 vectors
    vectors = []
    for i in range(3):
        vec = list(map(float, input(f"Enter vector {i+1} (3 space-separated numbers): ").split()))
        if len(vec) != 3:
            raise ValueError("Each vector must have exactly 3 components.")
        vectors.append(vec)
    
    G, det_G = gram_matrix_and_determinant(vectors)
    
    print("\nGram Matrix:")
    print(G)
    print("\nDeterminant of Gram Matrix:", det_G)

