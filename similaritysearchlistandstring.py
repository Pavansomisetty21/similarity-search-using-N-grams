from nltk.util import ngrams
#similarit search using N grams in between list and string
# Example input: large string and district list
large_text = "This dataset contains data collected from the Bangalore Urban region, which includes demographic info."
district_list = ["Bengaluru Urban", "Bangalore Rural", "Chennai", "Mumbai", "Delhi"]

# Function to generate n-grams for a string
def generate_ngrams(text, n):
    return list(ngrams(text, n))

# Function to calculate Jaccard similarity
def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    return intersection / union if union != 0 else 0

# Function to find the best-matching district from a large text
def find_matching_district_from_text(large_text, district_list, n=2, threshold=0):
    text_ngrams = set(generate_ngrams(large_text.lower(), n))
    best_match = None
    best_similarity = 0

    for district in district_list:
        if isinstance(district, float):
            continue
        district_ngrams = set(generate_ngrams(district.lower(), n))
        similarity = jaccard_similarity(text_ngrams, district_ngrams)

        if similarity > best_similarity and similarity >= threshold:
            best_similarity = similarity
            best_match = district

    return best_match, best_similarity

# Run it
match, prob = find_matching_district_from_text(large_text, district_list)
print(f"Matched district: {match} (Similarity: {prob:.2f})")
