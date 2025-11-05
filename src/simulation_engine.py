from .warehouse_model import WarehouseGraph
from .metrics import calculate_throughput
import time

class SimulationEngine:
    def __init__(self):
        self.graph = WarehouseGraph()
    
    def run_iteration(self, num_orders=100, iterations=5):
        """Build-test-prove: Simulate orders, validate metrics"""
        results = []
        for i in range(iterations):
            start = time.time()
            self.graph.simulate_failure()  # Inject risks
            paths = self.graph.shortest_paths()
            # Mock WES integration: Route orders via paths
            routed_orders = len(paths) * (num_orders // len(self.graph.nodes))
            throughput = calculate_throughput(routed_orders, time.time() - start)
            results.append({'iteration': i, 'throughput': throughput, 'paths_available': len(paths)})
            # Reset for next cycle
            for edge in self.graph.G.edges:
                if 'failed' in self.graph.G[edge[0]][edge[1]]:
                    del self.graph.G[edge[0]][edge[1]]['failed']
        return results
    
    # Add vendor mock: e.g., def integrate_wes_api(self, api_endpoint): ...