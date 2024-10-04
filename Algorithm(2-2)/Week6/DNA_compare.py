from optimalhash import optimal_hash

# Combine both functions and add a test
def DNAcompare(s1, s2):
    max_length = min(len(s1), len(s2))
    result = ""
    
    for i in range(1, max_length+1):
        for j in range(len(s1)-i+1):
            for k in range(len(s2)-i+1):
                if optimal_hash(s1[j:j+i]) == optimal_hash(s2[k:k+i]):
                    # if len(s1[j:j+i]) > len(result):
                        result = s1[j:j+i]
    
    return result

# Test the complete implementation
def test_dna_compare():
    # Test case 1: Finding common subsequence
    seq1 = "ATGCGT"
    seq2 = "ATACGT"
    result = DNAcompare(seq1, seq2)
    print(f"Sequence 1: {seq1}")
    print(f"Sequence 2: {seq2}")
    print(f"Longest common subsequence: {result}\n")
    
    # Test case 2: No common subsequence
    seq3 = "AAAA"
    seq4 = "TTTT"
    result = DNAcompare(seq3, seq4)
    print(f"Sequence 3: {seq3}")
    print(f"Sequence 4: {seq4}")
    print(f"Longest common subsequence: {result}")


    # Test case 3: Book example
    seq3 = "TGTCATGAGAAAAGACAGCCGACACT"
    seq4 = "AAAAGACAGCCGACACTGTT"
    result = DNAcompare(seq3, seq4)
    print(f"Sequence 3: {seq3}")
    print(f"Sequence 4: {seq4}")
    print(f"Longest common subsequence: {result}")

if __name__ == "__main__":
    test_dna_compare()