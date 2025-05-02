from main import calculate_similarity  
import pytest
def test_identical_sequences():
    seq = "CGTAC"
    result = calculate_similarity(seq, seq, k=3)
    assert result["similarity_score"] == 1.0

def test_different_sequences():
    seq1 = "ABCDEFG"
    seq2 = "GFEDCBA"
    result = calculate_similarity(seq1, seq2, k=3)
    assert result["similarity_score"] == 0.0

def test_overlapping_sequneces():
    seq1 = "ATCGATCG"
    seq2 = "ATCGTTTT"
    result = calculate_similarity(seq1, seq2, k=3)
    assert 0.0 < result["similarity_score"] < 1.0

def test_no_sequence():
    result = calculate_similarity("", "", k=3)
    assert result["similarity_score"] == 0.0 

def test_one_empty_sequence():
    result = calculate_similarity("ATCGATCG", "", k=3)
    assert result["similarity_score"] == 0.0
