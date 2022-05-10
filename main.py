import json

def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as f:
        candidates = []
        candidat = json.load(f)
        for person in candidat:
            candidates.append(person)
        return candidates





# print(load_candidates())

