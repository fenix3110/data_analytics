import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from data import get_transactions

st.set_page_config(page_title="Market Basket Analysis", layout="wide")

# Title
st.title("🛒 Market Basket Analysis (Apriori) Dashboard")

# Load dataset
transactions = get_transactions()
items = sorted({item for txn in transactions for item in txn})

# One-hot encoding
encoded_data = []
for txn in transactions:
    encoded_data.append({item: (item in txn) for item in items})
df = pd.DataFrame(encoded_data)

# Count item frequencies
item_counts = {}
for txn in transactions:
    for item in txn:
        item_counts[item] = item_counts.get(item, 0) + 1

df_counts = pd.DataFrame(list(item_counts.items()), columns=["Item", "Frequency"])
df_counts = df_counts.sort_values(by="Frequency", ascending=False)

# Plot frequency chart
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(df_counts["Item"], df_counts["Frequency"], color="skyblue")
ax.set_title("🛒 Item Frequency in Transactions")
ax.set_xlabel("Items")
ax.set_ylabel("Frequency")

# Display in Streamlit
st.subheader("📊 Item Frequency Chart")
st.pyplot(fig)

# Show raw data
with st.expander("🔍 View Transactions and Encoded Data"):
    st.subheader("Raw Transactions")
    st.write(pd.DataFrame({"Transaction Items": [", ".join(txn) for txn in transactions]}))
    
    st.subheader("One-Hot Encoded Data")
    st.dataframe(df)

# Sidebar inputs
st.sidebar.header("⚙️ Apriori Settings")
min_support = st.sidebar.slider("Min Support", 0.1, 1.0, 0.3, 0.05)
min_confidence = st.sidebar.slider("Min Confidence", 0.1, 1.0, 0.6, 0.05)

# Run Apriori
frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)

# Results
st.subheader("📋 Frequent Itemsets")
st.dataframe(frequent_itemsets.sort_values("support", ascending=False))

st.subheader("📈 Association Rules")
if not rules.empty:
    rules_display = rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].copy()
    rules_display['antecedents'] = rules_display['antecedents'].apply(lambda x: ', '.join(list(x)))
    rules_display['consequents'] = rules_display['consequents'].apply(lambda x: ', '.join(list(x)))
    st.dataframe(rules_display.sort_values(['confidence', 'lift'], ascending=False))
else:
    st.warning("No rules found. Try lowering support/confidence.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit and mlxtend")
