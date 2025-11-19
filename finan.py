
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Finance Tracker", layout="wide")

st.title("💰 Advanced Finance Tracker (Browser Version)")

# --- Sidebar Input ---
st.sidebar.header("Add New Record")

type_choice = st.sidebar.selectbox("Type", ["Income", "Expense"])
amount = st.sidebar.number_input("Amount", min_value=0.0, step=100.0)
category = st.sidebar.text_input("Category")
note = st.sidebar.text_area("Notes")

if st.sidebar.button("Add Record"):
    st.session_state.data.append(
        {"Type": type_choice, "Amount": amount, "Category": category, "Notes": note}
    )
    st.sidebar.success("Record added!")

# --- Initialize Storage ---
if "data" not in st.session_state:
    st.session_state.data = []

df = pd.DataFrame(st.session_state.data)

st.subheader("📊 Transaction History")

if not df.empty:
    st.dataframe(df, use_container_width=True)

    total_income = df[df["Type"] == "Income"]["Amount"].sum()
    total_expense = df[df["Type"] == "Expense"]["Amount"].sum()
    balance = total_income - total_expense

    st.metric("Total Income", f"₹{total_income:,.2f}")
    st.metric("Total Expense", f"₹{total_expense:,.2f}")
    st.metric("Balance", f"₹{balance:,.2f}")

else:
    st.info("No records yet. Add some using the sidebar.")

