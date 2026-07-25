"""Utility functions for RICE calculator."""

import pandas as pd
from src.rice_calculator import RICECalculator

def load_features_from_csv(filepath):
    """Load features from CSV file."""
    df = pd.read_csv(filepath)
    return df.to_dict('records')

def save_results_to_csv(ranked_features, filepath):
    """Save ranked features to CSV."""
    df = pd.DataFrame(ranked_features)
    df = df[['name', 'reach', 'impact', 'confidence', 'effort', 'rice_score']]
    df.to_csv(filepath, index=False)
    print(f"Results saved to {filepath}")

def print_rankings(ranked_features):
    """Pretty print feature rankings."""
    print("\n" + "="*70)
    print("RICE PRIORITIZATION RESULTS")
    print("="*70)
    print(f"{'Rank':<6} {'Feature':<25} {'RICE Score':<15} {'Effort':<10}")
    print("-"*70)
    
    for i, feature in enumerate(ranked_features, 1):
        print(f"{i:<6} {feature['name']:<25} {feature['rice_score']:<15.2f} {feature['effort']:<10}")
    
    print("="*70 + "\n")