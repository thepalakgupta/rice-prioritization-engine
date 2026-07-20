import streamlit as st
import pandas as pd
import json
from datetime import datetime
import anthropic

st.set_page_config(
    page_title="RICE Prioritization Engine",
    page_icon="📊",
    layout="wide"
)

st.title("📊 RICE Feature Prioritization Engine")
st.markdown("Score features objectively. AI explains the 'why' behind priorities.")

# Initialize session state
if 'features' not in st.session_state:
    st.session_state.features = []
if 'client' not in st.session_state:
    st.session_state.client = None

# Sidebar - API Key
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input("Claude API Key", type="password", help="Get from console.anthropic.com")
    
    if api_key:
        st.session_state.client = anthropic.Anthropic(api_key=api_key)
        st.success("✓ API Connected")
    
    st.markdown("---")
    st.markdown("""
    ### RICE Framework
    - **Reach**: Users affected (1-100)
    - **Impact**: Impact per user (1=low, 2=medium, 3=high)
    - **Confidence**: Confidence % (0-100)
    - **Effort**: Weeks to build (1-20)
    
    **Score = (Reach × Impact ÷ Effort) × (Confidence/100)**
    """)

# Tabs
tab1, tab2, tab3 = st.tabs(["Add Features", "Prioritize", "Analysis"])

# TAB 1: ADD FEATURES
with tab1:
    st.header("Add New Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        feature_name = st.text_input("Feature name", placeholder="e.g., Dark mode")
        description = st.text_area("Description", placeholder="Why this matters...", height=80)
    
    with col2:
        reach = st.slider("Reach (users affected)", 1, 100, 50)
        impact = st.select_slider("Impact per user", options=[1, 2, 3], value=2)
    
    col3, col4, col5 = st.columns(3)
    
    with col3:
        confidence = st.slider("Confidence (%)", 0, 100, 80)
    
    with col4:
        effort = st.slider("Effort (weeks)", 1, 20, 4)
    
    with col5:
        st.markdown("---")
        if effort > 0:
            score = (reach * impact / effort) * (confidence / 100)
            st.metric("Quick Score", f"{score:.1f}")
    
    if st.button("➕ Add Feature", use_container_width=True, type="primary"):
        if feature_name.strip():
            new_feature = {
                "id": len(st.session_state.features) + 1,
                "name": feature_name,
                "description": description,
                "reach": reach,
                "impact": impact,
                "confidence": confidence,
                "effort": effort,
                "score": (reach * impact / effort) * (confidence / 100)
            }
            st.session_state.features.append(new_feature)
            st.success(f"✓ Added '{feature_name}'")
            st.rerun()
    
    st.markdown("---")
    st.subheader("Your Features")
    
    if st.session_state.features:
        sorted_features = sorted(st.session_state.features, key=lambda x: x['score'], reverse=True)
        for feature in sorted_features:
            col1, col2, col3 = st.columns([3, 1, 0.5])
            
            with col1:
                priority = "🔴 High" if feature['score'] >= 8 else "🟡 Medium" if feature['score'] >= 4 else "🟢 Low"
                st.write(f"**{feature['name']}** — {priority}")
                st.caption(feature['description'])
            
            with col2:
                st.metric("Score", f"{feature['score']:.1f}")
            
            with col3:
                if st.button("❌", key=f"del_{feature['id']}"):
                    st.session_state.features = [f for f in st.session_state.features if f['id'] != feature['id']]
                    st.rerun()
    else:
        st.info("No features yet. Add one above!")

# TAB 2: PRIORITIZE
with tab2:
    st.header("Feature Ranking")
    
    if st.session_state.features:
        sorted_features = sorted(st.session_state.features, key=lambda x: x['score'], reverse=True)
        
        df = pd.DataFrame(sorted_features)
        df['Rank'] = range(1, len(df) + 1)
        df_display = df[['Rank', 'name', 'reach', 'impact', 'confidence', 'effort', 'score']]
        df_display.columns = ['#', 'Feature', 'Reach', 'Impact', 'Confidence', 'Effort', 'Score']
        
        st.dataframe(df_display, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        if st.button("🤖 Get AI Reasoning for Top 3", use_container_width=True):
            if st.session_state.client:
                top_3 = sorted_features[:3]
                features_text = "\n".join([
                    f"{i+1}. {f['name']} (Score: {f['score']:.1f}) - {f['description']}"
                    for i, f in enumerate(top_3)
                ])
                
                with st.spinner("Claude is analyzing..."):
                    try:
                        message = st.session_state.client.messages.create(
                            model="claude-opus-4-6",
                            max_tokens=600,
                            messages=[{
                                "role": "user",
                                "content": f"You're a product strategist. Briefly explain why these top 3 features should be prioritized:\n\n{features_text}\n\nBe concise (2-3 sentences per feature)."
                            }]
                        )
                        st.markdown("### AI Analysis")
                        st.markdown(message.content[0].text)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Enter Claude API key in sidebar")
        
        st.markdown("---")
        csv = df_display.to_csv(index=False)
        st.download_button("📥 Download CSV", csv, f"rice_{datetime.now().strftime('%Y%m%d')}.csv", "text/csv")
    else:
        st.info("Add features first")

# TAB 3: ANALYSIS
with tab3:
    st.header("Analysis")
    
    if st.session_state.features:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Features", len(st.session_state.features))
        with col2:
            avg = sum(f['score'] for f in st.session_state.features) / len(st.session_state.features)
            st.metric("Avg Score", f"{avg:.1f}")
        with col3:
            high = len([f for f in st.session_state.features if f['score'] >= 8])
            st.metric("High Priority", high)
        
        st.markdown("---")
        
        st.subheader("Score Distribution")
        df = pd.DataFrame(st.session_state.features).sort_values('score', ascending=True)
        
        import plotly.express as px
        fig = px.bar(df, x='score', y='name', orientation='h', title="Features by Score")
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        st.subheader("Effort vs Impact")
        fig2 = px.scatter(df, x='effort', y='impact', size='score', hover_name='name', 
                         title="Effort vs Impact (bubble size = score)")
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("Add features to see analysis")

st.markdown("---")
st.caption("Built with Streamlit + Claude API | GitHub: thepalakgupta/rice-prioritization-engine") 
