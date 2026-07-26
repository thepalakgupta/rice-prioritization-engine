# RICE Prioritization Engine

A data-driven framework for prioritizing product features using the RICE methodology (Reach, Impact, Confidence, Effort).The live demonstration of which can be viewed here : https://rice-prioritization-engine.streamlit.app/

## Why Claude API?

Raw RICE scores don't mean much to stakeholders. Claude API converts scores (e.g., "480") into business language (e.g., "Reaches 5,000 users, 3x impact, 2 weeks effort") so teams align faster around decisions without endless debate.

## Overview

This prioritization engine helps product managers decide which features to build first by scoring them on **Reach, Impact, Confidence, and Effort**.

**Key Insight:** The optimal feature roadmap is rarely obvious—use data to remove bias and emotional decision-making.

## The Problem

**Without Prioritization:**
- Priorities driven by loudest voice or politics
- Revenue left on table (features built in wrong order)
- Team doesn't understand decisions
- Constant roadmap conflicts

**With Smart Prioritization:**
- Data-driven feature ranking
- Clear explanation of why
- Team alignment
- Predictable impact

### Example Scenario

```
Product: B2B SaaS Platform

Features waiting:
- Feature A: Dark Mode
- Feature B: Analytics Dashboard
- Feature C: API Integration

Without RICE: "Let's build Dark Mode" ← Why?
With RICE: "Build Analytics Dashboard (score: 900) because it 
reaches 500 enterprise customers, improves retention 4x, requires 
5 weeks. Dark Mode (400) is lower ROI—save for later."
```

## How It Works

### The RICE Formula

```
RICE Score = (Reach × Impact × Confidence) / Effort

Where:
- Reach: How many users affected? (per time period)
- Impact: How much does it affect each user? (3x, 2x, 1x, 0.5x, 0.25x)
- Confidence: How sure are you? (100%, 80%, 50%)
- Effort: How many person-weeks to build?
```

### Example Calculation

```
Feature: Dark Mode

Reach: 5,000 users/quarter
Impact: 3x (significant improvement to experience)
Confidence: 80% (pretty sure customers want this)
Effort: 3 person-weeks

RICE = (5000 × 3 × 0.8) / 3 = 4,000

Feature: Analytics Dashboard

Reach: 500 users/quarter (enterprise customers only)
Impact: 4x (critical for retention)
Confidence: 90% (customer requests prove it)
Effort: 5 person-weeks

RICE = (500 × 4 × 0.9) / 5 = 360

Result: Build Dark Mode first (4,000 > 360)
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/thepalakgupta/rice-prioritization-engine.git
cd rice-prioritization-engine

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

The app will open at `http://localhost:8501`

## Usage

### Method 1: Interactive Web App (Easiest)

```bash
streamlit run app.py
```

**Features:**
- Input features with RICE parameters
- Automatic score calculation
- Ranked feature list
- Export results to CSV

### Method 2: Python Script

```python
from src.rice_calculator import RICECalculator

calculator = RICECalculator()

features = [
    {"name": "Dark Mode", "reach": 5000, "impact": 3, "confidence": 0.8, "effort": 3},
    {"name": "Analytics", "reach": 500, "impact": 4, "confidence": 0.9, "effort": 5},
    {"name": "API Integration", "reach": 100, "impact": 5, "confidence": 0.7, "effort": 8}
]

scores = calculator.rank_features(features)
calculator.print_rankings(scores)
```

**Output:**
```
Feature Prioritization (RICE Scores)
====================================
1. Dark Mode              4000
2. Analytics Dashboard    360
3. API Integration        87
```

### Method 3: Batch Prioritization

```python
# For multiple feature requests at once

all_features = [
    {"name": "Feature A", ...},
    {"name": "Feature B", ...},
    # ... more features
]

ranked = calculator.rank_features(all_features)

for rank, feature in enumerate(ranked, 1):
    print(f"{rank}. {feature['name']}: {feature['score']}")
```

## Key Insights

### Insight 1: RICE Removes Politics

```
Without RICE:
Manager A: "We MUST build Dark Mode"
Manager B: "No, Analytics is more important"
Debate goes in circles...

With RICE:
Dark Mode: 4,000
Analytics: 360
Result: Data decides. Everyone moves on.
```

### Insight 2: Effort Matters More Than You Think

```
Feature A: (10,000 reach × 3 impact × 0.8 conf) / 2 effort = 12,000
Feature B: (10,000 reach × 3 impact × 0.8 conf) / 20 effort = 1,200

Even though A and B have same reach/impact/confidence,
A's lower effort makes it 10x more valuable.

Lesson: Quick wins compound. Build them first.
```

### Insight 3: Confidence is Underrated

```
Feature A: (5000 × 3 × 1.0) / 5 = 3,000
Feature B: (5000 × 3 × 0.5) / 5 = 1,500

Same reach/impact/effort, but higher confidence on A
makes it 2x more valuable.

Lesson: Don't build on assumptions. Validate first.
```

## When to Use

### ✅ Perfect For:
- Product roadmap planning
- Feature backlogs with 10+ items
- Cross-functional alignment
- Quarterly planning
- Budget allocation

### ❌ Not Suitable For:
- Bug fixes (different priority framework)
- Performance improvements (use different metrics)
- Technical debt (hidden impact, hard to score)
- Crisis mode (use urgency, not RICE)

## Limitations

⚠️ **RICE Assumptions:**

1. **Quantifiable Metrics**
   - Assumes you can estimate reach, impact, effort
   - Reality: Often guesses, especially for new products
   - Solution: Validate assumptions with data over time

2. **Equal Impact Weight**
   - RICE treats all impact equally
   - Reality: Some features drive disproportionate value
   - Solution: Adjust impact multipliers by customer segment

3. **No Strategic Context**
   - Pure ROI calculation
   - Reality: Some low-RICE features are strategic (brand, morale)
   - Solution: Use RICE as input, not gospel

4. **Doesn't Account for Dependencies**
   - Feature B depends on Feature A
   - RICE ranks independently
   - Solution: Manually check dependencies before execution

5. **Confidence Uncertainty**
   - Hard to estimate "80% vs 90% confidence"
   - Reality: Confidence changes as you learn
   - Solution: Re-score quarterly with new information

## Testing

### Run Unit Tests

```bash
pytest tests/
```

### Test Coverage

Tests verify:
- ✅ RICE score calculation accuracy
- ✅ Ranking order correctness
- ✅ Input validation
- ✅ Edge cases (zero effort, zero reach)
- ✅ CSV import/export

## Project Structure

```
rice-prioritization-engine/
├── src/
│   ├── __init__.py
│   ├── rice_calculator.py   # RICE scoring logic
│   ├── utils.py             # Helper functions
│   └── config.py            # Configuration
├── data/
│   └── sample_features.csv  # Example features
├── tests/
│   └── test_rice_calculator.py  # Unit tests
├── app.py                   # Streamlit web app
├── requirements.txt         # Dependencies
├── .gitignore
└── README.md
```

## Configuration

Edit `src/config.py` to customize:

```python
RICE_COMPONENTS = {
    'reach': 'Users affected',
    'impact': 'Improvement multiplier',
    'confidence': 'Certainty level',
    'effort': 'Weeks to build'
}

IMPACT_OPTIONS = {
    3: '3x - Massive impact',
    2: '2x - Major impact',
    1: '1x - Noticeable',
    0.5: '0.5x - Minor',
    0.25: '0.25x - Tiny'
}
```

## Real-World Example

### Scenario: E-Commerce Platform

**Goal:** Decide Q3 roadmap

**Features in backlog:**
1. Product Recommendations
2. One-Click Checkout
3. Wishlist Feature
4. Mobile App Push Notifications
5. Live Chat Support

**RICE Scores:**

| Feature | Reach | Impact | Conf | Effort | Score |
|---------|-------|--------|------|--------|-------|
| Recommendations | 10,000 | 3x | 90% | 4 wks | 6,750 |
| One-Click | 8,000 | 2x | 80% | 2 wks | 6,400 |
| Wishlist | 5,000 | 2x | 70% | 2 wks | 3,500 |
| Push Notif | 3,000 | 2x | 60% | 1 wk | 3,600 |
| Live Chat | 1,000 | 3x | 50% | 4 wks | 375 |

**Recommended Q3 Roadmap:**
1. **Recommendations** (6,750) - Highest ROI
2. **One-Click Checkout** (6,400) - High impact, quick
3. **Push Notifications** (3,600) - Easy win
4. **Wishlist** (3,500) - Lower priority
5. **Live Chat** (375) - Defer to Q4

**Business Impact:**
- Q3 features: 6,750 + 6,400 + 3,600 = 16,750 ROI
- Expected outcomes: 
  - Recommendations: 10% revenue lift
  - One-Click: 5% conversion increase
  - Push: 3% re-engagement

---

## FAQ

### Q: How do I estimate Reach?

**A:** 
- Ask: How many monthly active users will use this?
- Consider: Not all users → affected users only
- Example: Mobile app push → 40% of users have app enabled → 40% reach

### Q: What if two features have same RICE score?

**A:** 
- Check effort (lower effort = better)
- Consider strategic alignment
- Check dependencies (does one unblock another?)
- Flip a coin if truly equal (paralysis is worse than wrong choice)

### Q: Should I re-score features?

**A:** 
- Yes, quarterly minimum
- As you learn: adjust confidence
- As market changes: adjust reach/impact
- RICE is input, not output—revisit regularly

### Q: Can I customize the formula?

**A:** 
Yes! Some teams use:
```
Score = (Reach × Impact) / Effort  # Ignore confidence
Score = (Reach × Impact × Confidence) / (Effort × Risk)  # Add risk
```

Customize in `src/config.py`

### Q: What about technical debt?

**A:** 
Hard to score with RICE:
- Low reach (only internal team affected)
- Impact is hard to quantify
- Better approach: Budget 20% of sprints for debt, use RICE for remaining 80%

## Contributing

Found a bug or want improvements?

1. **Report Issues** - Create GitHub issue with example
2. **Contribute Code** - Fork, improve, submit PR
3. **Share Roadmaps** - Show how you used RICE
4. **Suggest Metrics** - Improve scoring formulas

## License

MIT License - Free to use, modify, and distribute

## Author

**Palak Gupta**
- LinkedIn: [linkedin.com/in/thepalakgupta](https://linkedin.com/in/thepalakgupta)
- GitHub: [github.com/thepalakgupta](https://github.com/thepalakgupta)
- Portfolio: [portfolio-palak-gupta.vercel.app](https://portfolio-palak-gupta.vercel.app)

## References

- [RICE Framework (Intercom)](https://www.intercom.com/blog/rice-scoring-product-prioritization/)
- [Product Prioritization (Product School)](https://www.productschool.com/blog/product-management/rice-prioritization/)
- [Feature Prioritization Frameworks](https://www.prodpad.com/blog/product-prioritization-frameworks/)

---

**Built with ❤️ for product teams** | Data-Driven Feature Prioritization

*Features are hard to prioritize. RICE makes it easier.*
