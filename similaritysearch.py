from nltk.util import ngrams

# Example lists
extracted_districts = ["Bangalore Urban", "South delhi", "mumbay", "Calcuttaa"]  # List A (messy/extracted)
master_districts = ["Bengaluru Urban", "South Delhi", "Mumbai", "Kolkata", "Chennai"]  # List B (clean/master)

# Function to generate n-grams for a string
def generate_ngrams(text, n):
    return list(ngrams(text, n))

# Jaccard similarity
def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    return intersection / union if union != 0 else 0

# Matching function
def find_matching_district(query_district, district_list, n=2, threshold=0):
    query_ngrams = set(generate_ngrams(query_district.lower(), n))
    best_match = None
    best_similarity = 0

    for district in district_list:
        if isinstance(district, float):  # skip NaN
            continue
        district_ngrams = set(generate_ngrams(district.lower(), n))
        similarity = jaccard_similarity(query_ngrams, district_ngrams)

        if similarity > best_similarity and similarity >= threshold:
            best_similarity = similarity
            best_match = district

    return best_match, best_similarity

# Loop through list A and match to list B
matches = []
for dist in extracted_districts:
    match, score = find_matching_district(dist, master_districts)
    matches.append((dist, match, score))

# Output
for a, b, p in matches:
    print(f"{a} => {b} (Similarity: {p:.2f})")
