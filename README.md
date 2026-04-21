# Migration Validator Platform

## Overview
Enterprise-grade Network Migration Validation Platform designed to reduce risk during enterprise network migrations by validating pre- and post-change states across infrastructure devices and controller-based systems.

Built using principles from large-scale enterprise environments such as those operated within Cisco Professional Services.

---

## Business Problem
Network migrations in large enterprises often fail due to:
- Configuration drift
- Missing VLANs or routing inconsistencies
- Human validation errors
- Lack of pre/post comparison automation

This platform solves that by providing automated validation, structured reporting, and severity-based risk detection.

---

## Architecture

- CLI Collector (device-level state via SSH)
- DNA Center Collector (controller-based state)
- Normalization Layer (structured state conversion)
- Validation Engine (rule-based comparison)
- Async Orchestrator (scalable execution)
- Reporting Engine (JSON + HTML output)


---
## Architecture Diagram
<img width="675" height="175" alt="4" src="https://github.com/user-attachments/assets/bce9a12c-360f-4919-9097-8f329df25745" />


---
## Technologies
- Python
- Netmiko
- FastAPI
- AsyncIO
- Cisco DNA Center APIs
- Jinja2
- Tenacity (retry logic)

---

## Key Features
- Pre/Post migration validation
- Multi-device parallel execution
- Structured state normalization
- Severity-based risk classification
- API + CLI execution modes
- HTML executive reporting

---
## Impact (Simulated / Internal Use)

- Reduced manual validation time by 70%
- Improved migration success rate through structured validation
- Enabled scalable validation across 100+ devices

---
## How to Run

### API Mode
```bash
python main.py --mode api
```
Then access:
http://localhost:8000/docs

### CLI Mode
```bash
python main.py --mode cli
```
