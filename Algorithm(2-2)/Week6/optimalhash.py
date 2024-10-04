def optimal_hash(dna_sequence):
    """
    A simple hash function for DNA sequences.
    This is a basic implementation - real DNA sequence hashing
    would typically be more sophisticated.
    
    Args:
        dna_sequence (str): A DNA sequence containing A, T, G, C
    Returns:
        int: Hash value for the sequence
    """
    # Convert sequence to uppercase to ensure consistent hashing
    sequence = dna_sequence.upper()
    
    # Define base values for each nucleotide
    nucleotide_values = {'A': 1, 'T': 2, 'G': 3, 'C': 4}
    
    # Calculate hash using position-weighted sum
    hash_value = 0
    for i, nucleotide in enumerate(sequence):
        if nucleotide in nucleotide_values:
            # Use position-weighted value to ensure sequence order matters
            hash_value += nucleotide_values[nucleotide] * (5 ** i)
    
    return hash_value

# Example usage:
def test_optimal_hash():
    # Test case 1: Same sequences should have same hash
    seq1 = "ATGC"
    seq2 = "ATGC"
    print(f"Test 1: {seq1} vs {seq2}")
    print(f"Hash 1: {optimal_hash(seq1)}")
    print(f"Hash 2: {optimal_hash(seq2)}")
    print(f"Hashes match: {optimal_hash(seq1) == optimal_hash(seq2)}\n")
    
    # Test case 2: Different sequences should have different hash
    seq3 = "ATGC"
    seq4 = "CGTA"
    print(f"Test 2: {seq3} vs {seq4}")
    print(f"Hash 3: {optimal_hash(seq3)}")
    print(f"Hash 4: {optimal_hash(seq4)}")
    print(f"Hashes differ: {optimal_hash(seq3) != optimal_hash(seq4)}\n")
    
    # Test case 3: Case insensitive
    seq5 = "ATGC"
    seq6 = "atgc"
    print(f"Test 3: {seq5} vs {seq6}")
    print(f"Hash 5: {optimal_hash(seq5)}")
    print(f"Hash 6: {optimal_hash(seq6)}")
    print(f"Hashes match: {optimal_hash(seq5) == optimal_hash(seq6)}\n")

if __name__ == "__main__":
    test_optimal_hash()