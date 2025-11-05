import pandas as pd

def calculate_throughput(orders, duration):
    """Orders per minute, targeting 30% efficiency gain"""
    return orders / duration if duration > 0 else 0

def generate_report(results):
    df = pd.DataFrame(results)
    summary = {
        'avg_throughput': df['throughput'].mean(),
        'success_rate': (df['throughput'] > 50).mean() * 100,  # >95% target
        'efficiency_gain': (df['throughput'].max() / df['throughput'].min()) - 1
    }
    return summary, df