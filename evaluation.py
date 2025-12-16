import numpy as np

def precision_at_k(recommended, relevant, k):
    recommended_k = recommended[:k]
    relevant_set = set(relevant)
    return len(set(recommended_k) & relevant_set) / k if k else 0

def recall_at_k(recommended, relevant, k):
    recommended_k = recommended[:k]
    relevant_set = set(relevant)
    return len(set(recommended_k) & relevant_set) / len(relevant_set) if relevant_set else 0

def average_similarity(scores, k):
    return float(np.mean(scores[:k]))
