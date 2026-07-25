"""
RICE Prioritization Framework Calculator

RICE = (Reach × Impact × Confidence) / Effort

This module provides functionality to calculate RICE scores
for feature prioritization in product development.
"""

class RICECalculator:
    """Calculate RICE scores for prioritization."""
    
    def __init__(self):
        """Initialize RICE calculator."""
        pass
    
    def calculate_score(self, reach, impact, confidence, effort):
        """
        Calculate RICE score for a feature.
        
        Args:
            reach (int): Number of users affected
            impact (float): Impact magnitude (0.5, 1, 2, 3)
            confidence (float): Confidence percentage (0-1)
            effort (int): Effort in days
            
        Returns:
            float: RICE score
            
        Example:
            >>> calc = RICECalculator()
            >>> score = calc.calculate_score(5000, 2, 0.8, 10)
            >>> print(score)
            800.0
        """
        if effort == 0:
            raise ValueError("Effort cannot be zero")
        
        if not (0 <= confidence <= 1):
            raise ValueError("Confidence must be between 0 and 1")
        
        if impact not in [0.5, 1, 2, 3]:
            raise ValueError("Impact must be 0.5, 1, 2, or 3")
        
        score = (reach * impact * confidence) / effort
        return round(score, 2)
    
    def rank_features(self, features_list):
        """
        Rank features by RICE score (highest first).
        
        Args:
            features_list (list): List of dicts with keys:
                - name: Feature name
                - reach: Number of users
                - impact: Impact magnitude
                - confidence: Confidence (0-1)
                - effort: Effort in days
                
        Returns:
            list: Features sorted by RICE score (descending)
        """
        for feature in features_list:
            feature['rice_score'] = self.calculate_score(
                feature['reach'],
                feature['impact'],
                feature['confidence'],
                feature['effort']
            )
        
        # Sort by score descending
        ranked = sorted(features_list, key=lambda x: x['rice_score'], reverse=True)
        return ranked
    
    def validate_input(self, reach, impact, confidence, effort):
        """Validate RICE inputs."""
        errors = []
        
        if reach < 0:
            errors.append("Reach must be non-negative")
        
        if impact not in [0.5, 1, 2, 3]:
            errors.append("Impact must be 0.5, 1, 2, or 3")
        
        if not (0 <= confidence <= 1):
            errors.append("Confidence must be between 0 and 1")
        
        if effort <= 0:
            errors.append("Effort must be positive")
        
        return errors