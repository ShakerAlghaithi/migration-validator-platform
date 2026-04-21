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
This project follows a modular enterprise architecture:

- collectors/ → Multi-source data acquisition (CLI + Cisco DNA Center)
- normalization/ → Structured transformation of raw network data
- core/ → Orchestration, comparison, and reporting logic
- validators/ → Rule-based validation engine
- ci-cd/ → Automated pipeline integration
- docker/ → Containerized deployment

---
```markdown id="arch_portfolio"
## Architecture Diagram

CLI Devices ───────┐
                   ├──> Normalization Layer ──> Validation Engine ──> Report
Cisco DNA Center ──┘

                     ↓
              Async Orchestrator
                     ↓
              FastAPI Interface
```
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
###Output
- JSON validation report
- HTML executive report
- Structured logs
---
###Example Use Case
Used during enterprise network migrations to validate infrastructure consistency across:
- Core switches
- Distribution layers
- Controller-managed networks (Cisco DNA Center)

---
###Future Enhancements
- Real-time streaming validation
- Kubernetes deployment
- Event-driven architecture (Kafka)
- Full dashboard UI
---
###Author
Network Automation & Consulting Engineer
