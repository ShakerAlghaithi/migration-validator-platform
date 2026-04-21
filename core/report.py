def generate_report(results):
    for r in results:
        print(f"Device: {r['device']}")
        print(f"Status: {r['status']}")
        print("-" * 30)