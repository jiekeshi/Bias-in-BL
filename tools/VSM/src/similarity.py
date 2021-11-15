import os
import json
import time 
import numpy as np

def compute_similarity(bug_vector, code_vector, bug_data, past_bugs, storage_path):

    similarity = np.zeros((bug_vector.shape[0], code_vector.shape[0]), dtype=[("bug", "a30"),("file", "a250"), ("score", "f4")])

    for i in range(bug_vector.shape[0]):
        similarity[i]["bug"] = bug_vector[i]["id"][0]
        for j in range(code_vector.shape[0]):
            similarity[i][j]["file"] = code_vector[j]["id"][0]
            similarity[i][j]["score"] = 0.5 + 0.5 * np.sum(bug_vector[i]["tf_idf"] * code_vector[j]["tf_idf"])/(np.linalg.norm(bug_vector[i]["tf_idf"]) * np.linalg.norm(code_vector[j]["tf_idf"]))
        
    return similarity
