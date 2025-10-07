from RWP import rwp_examples

total_exp = len(rwp_examples)

def tot(attribute, value):
    """Count how many examples have a given attribute=value."""
    return sum(1 for example in rwp_examples.values() if example[attribute] == value)

def get_prob(attribute, attrib_val, ans_val):
    """P(attribute=attrib_val | ans=ans_val)"""
    count = sum(
        1 for example in rwp_examples.values()
        if example[attribute] == attrib_val and example['ans'] == ans_val
    )
    return count / tot('ans', ans_val)

# Human-readable labels for the output
labels = {
    ('Alt', 'Y'): "Probability for will wait if there is an Alternate Restaurant Nearby:",
    ('Alt', 'N'): "Probability for will wait if there No is an Alternate Restaurant Nearby:",
    ('Est', '0-10'): "Probability for will wait if Estimated Wait time is 0-10 minutes:",
    ('Est', '10-30'): "Probability for will wait if Estimated Wait time is 10-30 minutes",
    ('Est', '30-60'): "Probability for Will Wait if the Estimated Wait Time is 30-60 mins:",
    ('Est', '>60'): "Probability for Will Wait if the Estimated Wait Time is >60 mins:",
    ('Pat', 'S'): "Probability for will wait if there are Some Patrons",
    ('Pat', 'N'): "Probability for Will Wait if there are None Patrons:",
    ('Pat', 'F'): "Probability for Will Wait if there are Full Patrons:",
    ('Type', 'T'): "Probability for will wait if the place is Thai",
}

def main():
    ans_values = ['Y', 'N']
    p_ans = {ans: tot('ans', ans) / total_exp for ans in ans_values}

    for (attr, val), title in labels.items():
        p_val = tot(attr, val) / total_exp
        print(title)
        for ans in ans_values:
            prob = (get_prob(attr, val, ans) * p_ans[ans] / p_val) * 100
            print(f"{'Yes' if ans=='Y' else 'No'}: Will Wait {prob} %")

if __name__ == "__main__":
    main()
