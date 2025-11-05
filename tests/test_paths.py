import pytest
from src.warehouse_model import WarehouseGraph

def test_graph_connectivity():
    g = WarehouseGraph()
    assert nx.is_weakly_connected(g.G)  # Ensures end-to-end paths
    assert len(g.shortest_paths()) > 0

# Run: pytest tests/