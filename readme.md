# RICE Prioritization Engine

A data-driven framework for prioritizing product features using the RICE methodology with Claude AI-powered explanations.

## Overview

This prioritization engine helps product managers decide which features to build first by scoring them on **Reach, Impact, Confidence, and Effort**.

**Key Insight:** The optimal feature roadmap is rarely obvious—use data and AI reasoning to remove bias and emotional decision-making.

## Why Claude API for Recommendations?

### The Problem with Feature Prioritization

```
Without AI:
"Feature A should be first" ← Manager opinion
"No, Feature B is better" ← Conflicting opinions
Decision made by: Loudest voice or politics ❌

With Claude API:
Feature A: RICE = 480
Feature B: RICE = 900
Claude explains: "Feature B reaches 500 customers, improves conversion by 40%, 
requires only 2 weeks. Recommendation: Build Feature B first."
Decision made by: Data + AI reasoning ✅
```

### Why We Use Claude API

1. **Explain RICE Scores in Natural Language**
   - Raw score (480) means nothing to stakeholders
   - Claude API generates: "This feature reaches 1,000 users, provides 3x impact, 
     80% confidence, takes 5 weeks of effort. ROI-weighted score: 480."
   - Stakeholders understand the reasoning, not just the number

2. **Generate Feature Recommendations**
   - Simple ranking: [Feature A, Feature B, Feature C]
   - Claude API powered: "Top 3 priorities: Feature B (highest ROI), Feature A 
     (quick win), Feature C (strategic). Feature D should be deprioritized because 
     reach is low despite high impact."

3. **Provide Strategic Context**
   - Data says: "Build Feature B"
   - Claude API explains: "This aligns with Q3 growth goals, targets high-value 
     customer segment, and creates competitive advantage against Competitor X"

4. **Handle Edge Cases**
   - Two features have same score?
   - Claude API reasons: "Both score equally, but Feature A builds on existing 
     infrastructure (lower risk), while Feature B requires new tech stack."

### Example: Claude API in Action

```python
from anthropic import Anthropic

client = Anthropic()

# After calculating RICE scores
features_with_scores = [
    {"name": "Dark Mode", "reach": 5000, "impact": 3, "confidence": 0.8, "effort": 3, "score": 400},
    {"name": "Analytics Dashboard", "reach": 500, "impact": 4, "confidence": 0.9, "effort": 5, "score": 360},
    {"name": "API Integration", "reach": 100, "impact": 5, "confidence": 0.7, "effort": 8, "score": 87}
]

# Ask Claude to explain and recommend
message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": f"""
            I have calculated RICE scores for these features:
            
            {features_with_scores}
            
            Please:
            1. Recommend the top 2 features to build
            2. Explain why in business terms
            3. Mention any strategic considerations
            """
        }
    ]
)

recommendation = message.content[0].text
print(recommendation)

# Output example:
# "Top priority: Dark Mode (400 score)
#  - Reaches 5,000 users (largest impact)
#  - High confidence (80%) - we know customers want this
#  - Reasonable effort (3 weeks)
#  - Strategic: Quick win for user satisfaction
#  
#  Second priority: Analytics Dashboard (360 score)
#  - Targets enterprise customers (high-value)
#  - Highest impact (4x) on customer retention
#  - Well-understood scope (90% confidence)
#  
#  Skip API Integration for now:
#  - Reaches only 100 users (low reach = low ROI)
#  - Requires 8 weeks (opportunity cost too high)
#  - Revisit in Q4 if customer demand increases"
```

## How Claude API Enhances This Project

| Without Claude | With Claude API |
|---|---|
| "Feature B wins: 900 vs 480" | "Build Feature B because it reaches 500 customers, provides 3x improvement, requires low effort" |
| Spreadsheet of scores | Natural language explanation stakeholders understand |
| PM makes final call | AI-assisted reasoning reduces bias |
| No strategic context | Claude suggests timing, risks, dependencies |

## Installation & Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Set Claude API key
export ANTHROPIC_API_KEY="sk-ant-..."

# Run the app
streamlit run app.py
```

## Usage with Claude API

### Method 1: Get AI-Powered Recommendations

```python
from src.rice_calculator import RICECalculator
from anthropic import Anthropic

# Step 1: Calculate RICE scores
calculator = RICECalculator()
scores = calculator.rank_features(features_data)

# Step 2: Get Claude's analysis
client = Anthropic()

message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": f"Analyze these RICE scores and recommend top 3 features: {scores}"
    }]
)

print(message.content[0].text)
# Returns: Natural language recommendation with reasoning
```

### Method 2: Explain Individual Feature

```python
# User selects "Dark Mode" feature and asks "Why should we build this?"
# App calls Claude API:

explanation_request = f"""
Feature: Dark Mode
RICE Score: 400
- Reach: 5,000 users
- Impact: 3x
- Confidence: 80%
- Effort: 3 weeks

Explain why this is a good feature to prioritize right now, considering:
1. User base impact
2. Implementation difficulty
3. Competitive advantages
4. Strategic timing
"""

message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=512,
    messages=[{"role": "user", "content": explanation_request}]
)

print(message.content[0].text)
```

## Why Claude API Over Other Solutions?

### ✅ Claude API Advantages

1. **Natural Language Reasoning**
   - Explains WHY, not just ranking
   - Stakeholders understand the logic
   - Reduces meeting friction

2. **Context Understanding**
   - Understands product strategy
   - Considers trade-offs
   - Generates strategic insights

3. **Customizable Explanations**
   - For executives: "Reaches largest customer segment, high ROI"
   - For engineers: "Technical complexity: medium, uses existing stack"
   - For customers: "Requested by 5,000 users, improves experience"

4. **Handles Ambiguity**
   - Two features same score?
   - Claude suggests tie-breaking criteria
   - Explains risks and opportunities

### ❌ Without Claude API

- Numbers alone don't convince
- PMs spend hours explaining each decision
- Stakeholders second-guess the process
- No strategic context

## Real-World Example

### Scenario: SaaS Product Roadmap

**Features evaluated:**
- Feature A: Dark Mode (Score: 400)
- Feature B: Analytics (Score: 360)
- Feature C: API (Score: 87)

**Without Claude API:**
```
PM: "Build in this order: A, B, C"
Stakeholder: "Why not B first?"
PM: "Because the score is lower"
Stakeholder: "But my biggest clients want B"
[Debate continues for 30 minutes]
```

**With Claude API:**
```
Claude explains:
"Feature A reaches the broadest audience (5,000 users) and is quick to implement.
It's a quick win for user satisfaction.

Feature B targets enterprise customers (fewer users, but higher value).
It has the highest impact (4x) on retention for high-paying accounts.

Recommendation: Ship A in sprint 1 (morale + quick revenue), 
then B in sprint 2 (revenue retention). Skip C until customer demand increases."

Result: Stakeholders align. Decision is defensible. Time saved: 20 minutes.
```

## When Claude API is Most Valuable

✅ **Large feature backlogs** (20+ features to prioritize)
✅ **Stakeholder alignment needed** (explain reasoning to executives)
✅ **Conflicting priorities** (Claude identifies trade-offs)
✅ **Strategic planning** (Claude considers long-term implications)
✅ **Resource constraints** (Claude explains opportunity cost)

## Technical Implementation

### Adding Claude API to Your RICE App

```python
# In app.py (Streamlit app)

import streamlit as st
from anthropic import Anthropic

client = Anthropic()

st.title("RICE Prioritization Engine")

# User inputs features
features = st.text_area("Enter features (one per line)")

# Calculate RICE scores
rice_scores = calculate_rice(features)

# Get Claude's analysis
if st.button("Get AI Recommendation"):
    message = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"Analyze these RICE scores and provide strategic recommendations:\n{rice_scores}"
        }]
    )
    
    st.write("### Claude's Recommendation")
    st.write(message.content[0].text)
```

## Why This Matters for Your Resume

**Before (Traditional RICE):**
```
"Built RICE prioritization tool"
← Sounds like a calculator
```

**After (With Claude API):**
```
"Built AI-powered RICE prioritization engine using Claude API 
that generates natural language feature recommendations and 
strategic justifications—enabling faster stakeholder alignment 
and data-driven roadmap decisions"
← Sounds like a smart system
```

The Claude API integration shows:
- ✅ You understand prompt engineering
- ✅ You know how to add AI to products
- ✅ You think about user experience (explanations matter)
- ✅ You solve real problems (alignment takes time)

## Installation

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY="your-key-here"
streamlit run app.py
```

## Project Structure

```
rice-prioritization-engine/
├── src/
│   ├── rice_calculator.py    # RICE scoring logic
│   ├── claude_integrator.py  # Claude API calls
│   └── utils.py
├── app.py                    # Streamlit app with Claude
├── README.md
└── requirements.txt
```

## References

- [RICE Framework (Intercom)](https://www.intercom.com/blog/rice-scoring-product-prioritization/)
- [Claude API Documentation](https://docs.anthropic.com)
- [Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)

---

**Built with ❤️ for product teams** | Data-Driven Prioritization with AI

*Features are difficult to prioritize. Claude makes it easier.*
