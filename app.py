import streamlit as st
import pandas as pd

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Multi-Asset RL Portfolio Manager",
    page_icon="📈",
    layout="wide"
)

# =====================================
# TITLE
# =====================================

st.title("📈 Multi-Asset RL Portfolio Manager")

st.markdown("---")

# =====================================
# KPI CARDS
# =====================================

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Return (%)", "5.90")

with col2:
    st.metric("CAGR (%)", "5.95")

with col3:
    st.metric("Sharpe Ratio", "1.33")

with col4:
    st.metric("Max Drawdown (%)", "-4.24")

with col5:
    st.metric("Win Rate (%)", "53.76")

st.markdown("---")

# =====================================
# PERFORMANCE TABLE
# =====================================

st.subheader("📊 Performance Metrics")

metrics = pd.DataFrame({
    "Metric": [
        "Return",
        "CAGR",
        "Sharpe Ratio",
        "Maximum Drawdown",
        "Win Rate"
    ],
    "Value": [
        "5.90%",
        "5.95%",
        "1.33",
        "-4.24%",
        "53.76%"
    ]
})

st.table(metrics)

st.markdown("---")

# =====================================
# STRATEGY COMPARISON
# =====================================

st.subheader("📈 Strategy Comparison")

st.image(
    "Strategy Comparision.png",
    use_container_width=True
)

st.markdown("---")

# =====================================
# PPO EQUITY CURVE
# =====================================

st.subheader("📉 PPO Portfolio Equity Curve")

st.image(
    "PPO equity curve.png",
    use_container_width=True
)

st.markdown("---")

# =====================================
# ITC BUY & HOLD CURVE
# =====================================

st.subheader("📈 ITC Buy & Hold Equity Curve")

st.image(
    "ITC Buy hold curve.png",
    use_container_width=True
)

st.markdown("---")

# =====================================
# PPO vs ITC COMPARISON
# =====================================

st.subheader("⚔️ PPO vs ITC Buy & Hold")

st.image(
    "PPO itc comparison curve.png",
    use_container_width=True
)

st.markdown("---")

# =====================================
# PROJECT OVERVIEW
# =====================================

st.subheader("📋 Project Overview")

st.write("""
This project implements a Multi-Asset Reinforcement Learning Portfolio
Management System using PPO (Proximal Policy Optimization).

### Stocks Used
- ITC
- HDFC
- TCS

### Features Engineered
- Daily Returns
- RSI
- Moving Average (MA5)
- Moving Average (MA20)
- Volatility

### Reinforcement Learning Components
- Custom Portfolio Environment
- Multi-Asset Trading Actions
- PPO Agent
- Train/Test Split Evaluation

### Performance Evaluation
- Return
- CAGR
- Sharpe Ratio
- Maximum Drawdown
- Win Rate
- Buy & Hold Benchmark Comparison
""")

st.markdown("---")

st.success("✅ Multi-Asset RL Portfolio Manager Dashboard Successfully Built")