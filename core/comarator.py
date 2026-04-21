def compare_states(before, after):
    differences = {}

    for key in before:
        if before[key] != after[key]:
            differences[key] = {
                "before": before[key],
                "after": after[key]
            }

    return differences