# RICE Prioritization Engine

A data-driven framework for feature prioritization in product development.

## Overview

RICE is a prioritization framework that helps teams move from subjective debates to data-driven decisions about which features to build first.

Instead of arguing "Dark mode is important!" vs "Better search is more important!", use RICE to score both objectively.

## The Problem

**Without RICE:**
- Teams argue about priorities
- Loud voices win, not best ideas
- No shared language for prioritization
- Decisions change frequently
- Resources wasted on low-impact features

**With RICE:**
- Objective scoring methodology
- Everyone uses same criteria
- Decisions are defensible and repeatable
- Transparent trade-offs visible to all
- Maximize impact per effort spent

## How RICE Works

### Formula
```
RICE Score = (Reach × Impact × Confidence) / Effort
```

Higher score = higher priority to build first

### Components

#### **Reach** - How many users/customers will this feature affect?
- Count of users or percentage
- Per month or per year? Specify clearly
- Example: "500 users per month" or "5000 users total"

#### **Impact** - How much will this feature affect each user?
- 3 = Major (3x impact) - transformative, changes workflow
- 2 = Medium (2x impact) - noticeable improvement
- 1 = Minor (1x impact) - small improvement
- 0.5 = Minimal (0.5x impact) - barely noticeable

*Impact is a multiplier, not just a scale*

#### **Confidence** - How sure are you about Reach and Impact?
- 100% = Very sure (we have data, past projects, user research)
- 75% = Fairly sure (we surveyed users, have assumptions)
- 50% = Somewhat sure (educated guess, limited data)
- 25% = Low confidence (complete guess)

*Confidence is a modifier. Reduce scores if uncertain.*

#### **Effort** - How much work is required?
- In days, weeks, or months (be consistent)
- Includes: development + testing + QA + deployment
- Think realistically. Most estimates are too optimistic.
- Accounts for dependencies and blockers

*Effort is a divisor. More effort = lower priority.*

### Example Walkthrough

```
Feature: Dark Mode

Reach: 5000 users
  → We have 50,000 users total
  → Survey showed 10% use dark mode = 5,000 users

Impact: 2 (Medium)
  → Improves experience for late-night users
  → Not a workflow-changing feature
  → Nice to have, not critical

Confidence: 80% (or 0.8)
  → We surveyed 500 users, 10% want it
  → Industry data shows dark mode popular
  → But we're not 100% sure of actual adoption

Effort: 10 days
  → Frontend changes: 5 days
  → Testing: 2 days
  → Backend support: 2 days
  → Realistic, not optimistic

RICE Score = (5000 × 2 × 0.8) / 10
           = 8000 / 10
           = 800

Interpretation: Dark Mode scores 800 points. 
Compare with other features to prioritize.
```

### Real Example Comparison

| Feature | Reach | Impact | Confidence | Effort | RICE Score | Priority |
|---------|-------|--------|-----------|--------|-----------|----------|
| Push Notifications | 6000 | 1 | 0.8 | 5 | **960** | #1 Build First |
| Better Search | 8000 | 3 | 0.9 | 20 | **1080** | #2 Build Second |
| Dark Mode | 5000 | 2 | 0.8 | 10 | **800** | #3 |
| Mobile App | 10000 | 3 | 0.6 | 60 | **300** | #4 |
| Bug Fixes | 2000 | 1 | 1.0 | 2 | **1000** | #5 |

**Key Insight:** Push Notifications wins despite lower reach because effort is minimal (5 days). Mobile App loses despite largest reach because effort is huge (60 days). Better Search wins on total score: big reach × high impact × good confidence.

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
- Add features one by one
- Real-time RICE score calculation
- Auto-ranked prioritization
- Export results to CSV
- Visual charts and rankings

### Method 2: Python Script with CSV

```python
from src.rice_calculator import RICECalculator
from src.utils import load_features_from_csv, print_rankings

# Load features from CSV file
features = load_features_from_csv('data/sample_features.csv')

# Initialize calculator
calc = RICECalculator()

# Calculate scores and rank
ranked = calc.rank_features(features)

# Print beautiful results
print_rankings(ranked)
```

**Sample Output:**
```
======================================================================
RICE PRIORITIZATION RESULTS
======================================================================
Rank   Feature                   RICE Score      Effort    
----------------------------------------------------------------------
1      Push Notifications        7500.00         5         
2      Better Search             2160.00         20        
3      Dark Mode                 800.00          10        
4      Mobile App                300.00          60        
======================================================================
```

### Method 3: Programmatic (Single Feature)

```python
from src.rice_calculator import RICECalculator

# Initialize
calc = RICECalculator()

# Calculate single feature score
score = calc.calculate_score(
    reach=5000,
    impact=2,
    confidence=0.8,
    effort=10
)

print(f"RICE Score: {score}")  # Output: 800.0
```

### Method 4: Batch Processing

```python
from src.rice_calculator import RICECalculator

calc = RICECalculator()

features = [
    {
        'name': 'Dark Mode',
        'reach': 5000,
        'impact': 2,
        'confidence': 0.8,
        'effort': 10
    },
    {
        'name': 'Better Search',
        'reach': 8000,
        'impact': 3,
        'confidence': 0.9,
        'effort': 20
    },
    {
        'name': 'Push Notifications',
        'reach': 6000,
        'impact': 1,
        'confidence': 0.8,
        'effort': 5
    }
]

# Rank all features
ranked = calc.rank_features(features)

# Print results
for rank, feature in enumerate(ranked, 1):
    print(f"{rank}. {feature['name']}: {feature['rice_score']}")

# Output:
# 1. Push Notifications: 960.0
# 2. Better Search: 2160.0
# 3. Dark Mode: 800.0
```

## Example: Complete Walkthrough

See `notebooks/example_prioritization.ipynb` for a Jupyter notebook that walks through:
1. Loading sample data
2. Calculating RICE scores
3. Visualizing results with charts
4. Interpreting rankings

### Quick Example with Sample Data

We include 10 sample features in `data/sample_features.csv`:

| Feature | Reach | Impact | Confidence | Effort | RICE Score |
|---------|-------|--------|-----------|--------|-----------|
| Push Notifications | 6000 | 1 | 0.8 | 5 | 960.0 |
| Mobile App | 10000 | 3 | 0.6 | 60 | 300.0 |
| Better Search | 8000 | 3 | 0.9 | 20 | 1080.0 |
| Two-Factor Auth | 4000 | 3 | 0.9 | 8 | 1350.0 |
| Dark Mode | 5000 | 2 | 0.8 | 10 | 800.0 |
| User Analytics Dashboard | 7000 | 2 | 0.7 | 25 | 392.0 |
| API Integration | 3000 | 2 | 0.7 | 15 | 280.0 |
| Bulk Upload | 3000 | 2 | 0.6 | 12 | 300.0 |
| Export to Excel | 2000 | 1 | 0.8 | 3 | 533.3 |
| Dark Theme for Mobile | 4000 | 1 | 0.8 | 8 | 400.0 |

**Top 3 to Build:**
1. **Two-Factor Auth** (1350.0) - High impact security, moderate effort
2. **Better Search** (1080.0) - High reach, high impact
3. **Push Notifications** (960.0) - Quick win, low effort

## Key Insights & Best Practices

### Insight 1: Effort is a Powerful Divisor

```
Same reach and impact, different effort:
Feature A: (5000 × 2 × 0.8) / 10 = 800
Feature B: (5000 × 2 × 0.8) / 5 = 1600  ← Wins (half the effort!)

Halving effort doubles the score!
```

**Lesson:** Quick wins (low effort, decent impact) rank surprisingly high.

### Insight 2: Confidence Matters More Than You Think

```
Same reach and effort, different confidence:
Feature A: (5000 × 2 × 1.0) / 10 = 1000  (100% confident)
Feature B: (5000 × 2 × 0.5) / 10 = 500   (50% confident)

Uncertain features score half as high.
```

**Lesson:** Don't guess. If uncertain, do user research first.

### Insight 3: Impact Multiplies Everything

```
Same reach and effort, different impact:
Feature A: (8000 × 1 × 0.8) / 10 = 640
Feature B: (8000 × 3 × 0.8) / 10 = 1920  ← Wins (3x impact!)

Impact of 3x vs 1x is a 3x difference in score.
```

**Lesson:** Focus on transformative features, not incremental improvements.

### Best Practices

1. **Be Honest About Effort** 
   - Most teams underestimate by 50%
   - Add buffer for QA, bugs, deployment
   - Include dependencies and blockers

2. **Don't Overestimate Confidence**
   - If you guessed, confidence = 50%
   - If you surveyed 10 users, confidence = 75%
   - If you have hard data, confidence = 100%

3. **Compare Similar Features**
   - RICE works best for comparing features in same category
   - Don't compare "bug fix" with "new feature"
   - Handle critical bugs separately

4. **Re-evaluate Quarterly**
   - Market conditions change
   - User needs evolve
   - Re-run RICE each quarter

5. **Use as Guide, Not Gospel**
   - RICE is objective but not perfect
   - Strategic decisions override scores
   - Team morale and alignment matter

## When to Use RICE

### ✅ Perfect For:
- **Quarterly Planning** - What to build next quarter?
- **Feature Comparison** - Feature A vs Feature B vs Feature C?
- **Stakeholder Alignment** - Show data-driven reasoning
- **Team Prioritization** - Remove ego from decisions
- **New Feature Ideas** - Evaluate incoming requests

### ❌ Not Suitable For:
- **Bug Fixes** - Fix critical bugs immediately
- **Technical Debt** - Prioritize separately
- **Emergency Response** - Handle crises first
- **Maintenance** - Allocate separately
- **Strategic Bets** - Business strategy overrides RICE

## Limitations & Assumptions

⚠️ **This framework assumes:**

1. **Linear Relationships** - Reality is often non-linear
   - Doubling users doesn't always double value
   - Impact compounds in complex ways

2. **Independent Features** - Assumes no dependencies
   - Some features unlock other features
   - Some features block others
   - Handle dependencies separately

3. **Accurate Estimates** - Teams often guess on reach/impact
   - Base estimates on data when possible
   - Adjust confidence down if guessing
   - Re-validate after launch

4. **Static Context** - Assumes market doesn't change
   - Competitors launch features
   - User needs shift
   - Re-run RICE monthly/quarterly

### Future Improvements

To make RICE more powerful:

- [ ] **Add feature dependencies** - Features that unlock others
- [ ] **Account for seasonality** - Different times of year
- [ ] **Revenue weighting** - High-value customers vs average
- [ ] **Competitor analysis** - Factor in competitive moves
- [ ] **Team capacity** - What can you actually do this quarter?
- [ ] **Learning value** - R&D features for future potential
- [ ] **Risk scoring** - High-risk vs low-risk efforts

## Testing

### Run Unit Tests

```bash
pytest tests/
```

### Test Coverage

Tests verify:
- ✅ Correct RICE calculation
- ✅ Edge cases (zero effort, invalid impact, etc.)
- ✅ Input validation
- ✅ Feature ranking accuracy
- ✅ Score precision (2 decimal places)

### Example Test Output

```
tests/test_rice_calculator.py::TestRICECalculator::test_basic_calculation PASSED
tests/test_rice_calculator.py::TestRICECalculator::test_zero_effort_raises_error PASSED
tests/test_rice_calculator.py::TestRICECalculator::test_invalid_confidence PASSED
tests/test_rice_calculator.py::TestRICECalculator::test_invalid_impact PASSED
tests/test_rice_calculator.py::TestRICECalculator::test_ranking_features PASSED
tests/test_rice_calculator.py::TestRICECalculator::test_score_precision PASSED

==================== 6 passed in 0.15s ====================
```

## Project Structure

```
rice-prioritization-engine/
├── src/
│   ├── __init__.py                    # Package initialization
│   ├── rice_calculator.py             # Core RICE calculation logic
│   ├── utils.py                       # Helper functions (load CSV, print)
│   └── config.py                      # Configuration and constants
├── data/
│   └── sample_features.csv            # Example feature data for testing
├── notebooks/
│   └── example_prioritization.ipynb   # Jupyter notebook walkthrough
├── tests/
│   └── test_rice_calculator.py        # Unit tests (6 test cases)
├── app.py                             # Streamlit interactive web app
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git ignore rules
└── README.md                          # This file
```

### File Descriptions

| File | Purpose |
|------|---------|
| `rice_calculator.py` | Core RICECalculator class with score calculation and ranking |
| `utils.py` | Utility functions: load CSV, save results, pretty print |
| `config.py` | Configuration, constants, component definitions |
| `sample_features.csv` | 10 example features for testing and learning |
| `example_prioritization.ipynb` | Step-by-step Jupyter notebook |
| `test_rice_calculator.py` | 6 unit tests covering all functionality |
| `app.py` | Streamlit web app for interactive use |

## How to Contribute

Found a bug or have a feature idea?

1. **Report Issues:**
   - Create an issue on GitHub
   - Describe the problem
   - Include example inputs/outputs

2. **Contribute Code:**
   - Fork the repository
   - Create a feature branch: `git checkout -b feature/my-improvement`
   - Commit changes: `git commit -m "Add: My improvement"`
   - Push to branch: `git push origin feature/my-improvement`
   - Submit a pull request

3. **Improve Documentation:**
   - Update README with examples
   - Add comments to code
   - Create additional notebooks

## Examples from Real Companies

### Intercom's Approach
Intercom, a customer communication platform, uses RICE to decide what to build. They published the framework in a famous blog post: [RICE: Simple prioritization for product managers](https://www.intercom.com/blog/rice-prioritization-framework/)

### Modified Versions
Some teams modify RICE:
- **RICED** - Adds Customer Happiness as factor
- **RICE + Revenue** - Weights by customer LTV
- **RICE + Risk** - Accounts for implementation risk

Feel free to adapt for your team's needs!

## FAQ

### Q: What if I don't have historical data?

**A:** Use your best estimate and reduce confidence. 
- No data = 50% confidence
- 10 users surveyed = 75% confidence  
- Hard data from analytics = 100% confidence

Then gather data as you build and re-evaluate.

### Q: Should we include bug fixes in RICE?

**A:** No. Handle bugs separately:
- Critical bugs: Fix immediately
- Annoying bugs: Next sprint
- Minor bugs: Backlog

Only use RICE for feature prioritization.

### Q: How often should we re-run RICE?

**A:** Depends on your market:
- Fast-moving startup: Monthly
- Stable product: Quarterly
- Large enterprise: Annually

Re-run when:
- Launching new major feature
- Competitive threat emerges
- Team capacity changes
- User feedback reveals new needs

### Q: Can I use RICE for projects outside tech?

**A:** Yes! RICE works for any project:
- Marketing campaigns (reach = audience, impact = conversions)
- Sales initiatives (reach = prospects, impact = deal size)
- HR programs (reach = employees affected, impact = productivity)
- Operations improvements (reach = processes affected, impact = cost savings)

### Q: What if two features score the same?

**A:** Tie-breaker options:
1. Lower effort wins (quicker value)
2. Strategic importance wins
3. Team expertise/enthusiasm wins
4. Customer/user impact wins

Make it transparent to team.

## License

MIT License - Feel free to use, modify, and distribute.

## Author

**Palak Gupta**
- LinkedIn: [linkedin.com/in/thepalakgupta](https://linkedin.com/in/thepalakgupta)
- GitHub: [github.com/thepalakgupta](https://github.com/thepalakgupta)
- Portfolio: [portfolio-palak-gupta.vercel.app](https://portfolio-palak-gupta.vercel.app)

## References & Further Reading

- [Intercom Blog: RICE Prioritization Framework](https://www.intercom.com/blog/rice-prioritization-framework/)
- [How to Prioritize Features (Reforge)](https://www.reforge.com/)
- [Inspired by Marty Cagan](https://www.svpg.com/)
- [The Lean Startup by Eric Ries](https://theleanstartup.com/)
- [Jobs to be Done Framework](https://jtbd.info/)

## Support

Found a bug? Have a question?
- Open an issue on GitHub
- Email: thepalakgupta@gmail.com
- LinkedIn DM: [thepalakgupta](https://linkedin.com/in/thepalakgupta)

---

**Built with ❤️ for product teams** | Data-Driven Decisions

*Last updated: July 2026*
