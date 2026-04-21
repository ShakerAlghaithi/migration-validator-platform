from api.app import app
import uvicorn
from core.orchestrator import run_async_job


def run_cli_mode():
    """
    CLI mode for local execution (engineering/debug use)
    """
    import asyncio
    results = asyncio.run(run_async_job())

    print("\n===== MIGRATION VALIDATION RESULTS =====\n")
    for r in results:
        print(f"Device: {r['device']}")
        print(f"Status: {r['status']}")
        print(f"Severity: {r['severity']}")
        print("-" * 40)


def run_api_mode():
    """
    API mode for enterprise execution
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["cli", "api"], default="cli")

    args = parser.parse_args()

    if args.mode == "api":
        run_api_mode()
    else:
        run_cli_mode()