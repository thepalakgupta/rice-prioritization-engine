"""Unit tests for RICE calculator."""

import pytest
from src.rice_calculator import RICECalculator

class TestRICECalculator:
    """Test cases for RICE score calculation."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.calc = RICECalculator()
    
    def test_basic_calculation(self):
        """Test basic RICE score calculation."""
        score = self.calc.calculate_score(5000, 2, 0.8, 10)
        expected = (5000 * 2 * 0.8) / 10
        assert score == expected
    
    def test_zero_effort_raises_error(self):
        """Test that zero effort raises ValueError."""
        with pytest.raises(ValueError):
            self.calc.calculate_score(5000, 2, 0.8, 0)
    
    def test_invalid_confidence(self):
        """Test that confidence > 1 raises error."""
        with pytest.raises(ValueError):
            self.calc.calculate_score(5000, 2, 1.5, 10)
    
    def test_invalid_impact(self):
        """Test that invalid impact raises error."""
        with pytest.raises(ValueError):
            self.calc.calculate_score(5000, 2.5, 0.8, 10)
    
    def test_ranking_features(self):
        """Test feature ranking by RICE score."""
        features = [
            {'name': 'Feature A', 'reach': 1000, 'impact': 2, 'confidence': 0.8, 'effort': 10},
            {'name': 'Feature B', 'reach': 5000, 'impact': 1, 'confidence': 0.8, 'effort': 10},
        ]
        ranked = self.calc.rank_features(features)
        # Feature B should rank higher (500 vs 160)
        assert ranked[0]['name'] == 'Feature B'
    
    def test_score_precision(self):
        """Test that scores are rounded to 2 decimal places."""
        score = self.calc.calculate_score(1000, 3, 0.75, 7)
        assert len(str(score).split('.')[-1]) <= 2