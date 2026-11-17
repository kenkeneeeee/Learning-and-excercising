import streamlit as st

st.title("🇲🇾 Malaysia Income Tax Calculator by TK")

resident = st.radio("Are you resident of Malaysia?", ["YES", "NO"])
chargeable_income = st.number_input("Enter your chargeable income (RM):", min_value=0.0, step=1000.0)

def nr_income_tax(chargeable_income):
  return chargeable_income * 0.3

def t1_income_tax(chargeable_income):
  return (chargeable_income - 5000) * 0.01

def t2_income_tax(chargeable_income):
  return (chargeable_income - 20000) * 0.03 + 150

def t3_income_tax(chargeable_income):
  return (chargeable_income - 35000) * 0.06 + 600

def t4_income_tax(chargeable_income):
  return (chargeable_income - 50000) * 0.11 + 1500

def t5_income_tax(chargeable_income):
  return (chargeable_income - 70000) * 0.19 + 3700

def t6_income_tax(chargeable_income):
  return (chargeable_income - 100000) * 0.25 + 9400

def t7_income_tax(chargeable_income):
  return (chargeable_income - 400000) * 0.26 + 84400

def t8_income_tax(chargeable_income):
  return (chargeable_income - 600000) * 0.28 + 136400  

def t9_income_tax(chargeable_income):
  return (chargeable_income - 2000000) * 0.30 + 528400

if st.button("Calculate Tax"):
  if resident == "NO":
    st.success(f"Your income Tax is RM{nr_income_tax(chargeable_income):.2f}")
  elif resident == "YES":
    if chargeable_income <= 5000:
      st.info("Your income Tax is RM0.00 (below taxable threshold).")
    elif 5000 < chargeable_income <= 20000:
      st.success(f"Your income Tax is RM{t1_income_tax(chargeable_income):.2f}")
    elif 20000 < chargeable_income <= 35000:
      st.success(f"Your income Tax is RM{t2_income_tax(chargeable_income):.2f}")
    elif 35000 < chargeable_income <= 50000:
      st.success(f"Your income Tax is RM{t3_income_tax(chargeable_income):.2f}")
    elif 50000 < chargeable_income <= 70000:
      st.success(f"Your income Tax is RM{t4_income_tax(chargeable_income):.2f}")
    elif 70000 < chargeable_income <= 100000:
      st.success(f"Your income Tax is RM{t5_income_tax(chargeable_income):.2f}")
    elif 100000 < chargeable_income <= 400000:
      st.success(f"Your income Tax is RM{t6_income_tax(chargeable_income):.2f}")
    elif 400000 < chargeable_income <= 600000:
      st.success(f"Your income Tax is RM{t7_income_tax(chargeable_income):.2f}")
    elif 600000 < chargeable_income <= 2000000:
      st.success(f"Your income Tax is RM{t8_income_tax(chargeable_income):.2f}")
    elif chargeable_income > 2000000:
      st.success(f"Your income Tax is RM{t9_income_tax(chargeable_income):.2f}")
    else:
      st.error("Your income Tax is unable to calculate, please try again.")
  else:
    st.error("Invalid input for residency. Please answer YES or NO.")

st.title("🇲🇾 Malaysia Income Tax Calculator")
st.write("Your new description goes right here.")
