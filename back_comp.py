from fuzzywuzzy import fuzz

# Convert user document into a list of compliance statements
user_rules = user_compliance_text.split("\n")

# Compare each user rule with RBI rules
for user_rule in user_rules:
    best_match = max(rules, key=lambda r: fuzz.ratio(user_rule, r))
    similarity = fuzz.ratio(user_rule, best_match)

    if similarity < 80:  # Threshold for mismatch
        print(f"Possible Compliance Issue: {user_rule}")
        print(f"Closest RBI Rule: {best_match}")
