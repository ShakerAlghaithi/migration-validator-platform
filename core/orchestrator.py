import asyncio
from collectors.cli_collector import collect_device_state_async
from core.comparator import compare_states
from validators.validators import validate_all

async def run_async_job():
    devices = load_inventory()

    before_tasks = [collect_device_state_async(d) for d in devices]
    before_states = await asyncio.gather(*before_tasks)

    # In real system this is triggered externally
    await asyncio.sleep(2)

    after_tasks = [collect_device_state_async(d) for d in devices]
    after_states = await asyncio.gather(*after_tasks)

    results = []
    for before, after, device in zip(before_states, after_states, devices):
        diff = compare_states(before, after)
        validation = validate_all(before, after)

        severity = "LOW"
        if not validation['routes']:
            severity = "HIGH"
        elif not validation['interfaces']:
            severity = "MEDIUM"

        results.append({
            "device": device['name'],
            "status": "PASS" if not diff else "FAIL",
            "severity": severity,
            "validation": validation
        })

    return results