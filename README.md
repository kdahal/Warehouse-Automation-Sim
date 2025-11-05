# Warehouse Automation Simulation

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/) [![NetworkX](https://img.shields.io/badge/NetworkX-Graph%20Modeling-green)](https://networkx.org/)

## Overview
Modular Python sim for GreenBox-style warehouse automation: Models pallet-to-eaches flows using graph routing (AGVs/AMRs), validates throughput (95%+ target), and iterates designs. Inspired by ConOps translation—run "build-test-prove" cycles to mitigate risks like 5% failures.

**Key Features**:
- End-to-end paths: 10+ zones with capacities.
- Metrics: Throughput, efficiency gains (sim 30% uplift).
- Mock WES: API-ready for vendor integration.
- Jupyter demos for UAT.

## Quick Start
1. Clone: `git clone https://github.com/kdahal/Warehouse-Automation-Sim.git`
2. Install: `pip install -r requirements.txt`
3. Run demo: `jupyter notebook notebooks/demo_simulation.ipynb`
4. Test: `pytest tests/`

### Sample Output
| Iteration | Throughput (orders/min) | Paths Available |
|-----------|--------------------------|-----------------|
| 0         | 85.2                     | 6               |
| 1         | 92.1                     | 5               |
| ...       | ...                      | ...             |
**Avg Efficiency Gain: 28%**

![Throughput Plot](throughput_plot.png)  <!-- Add your generated plot -->

## Usage in Automation Design
- Tweak `warehouse_model.py` for custom ConOps (e.g., add AS/RS nodes).
- Extend `simulation_engine.py` for real WMS hooks.
- For risks: Adjust `failure_rate` to stress-test scalability.

## Contributing
Fork, PR with tests. See [issues](https://github.com/kdahal/Warehouse-Automation-Sim/issues).

License: MIT