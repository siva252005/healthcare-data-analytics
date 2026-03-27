import pandas as pd

# Load dataset (UPDATED PATH ✅)
df = pd.read_csv("../data/raw/healthcare_raw.csv")

insights = []

# 1. Smoker vs Non-Smoker
smoker_avg = df[df['smoker'] == 'yes']['charges'].mean()
non_smoker_avg = df[df['smoker'] == 'no']['charges'].mean()

if smoker_avg > non_smoker_avg:
    insights.append(f"Smokers have higher average charges ({round(smoker_avg,2)}) vs non-smokers ({round(non_smoker_avg,2)})")

# 2. Highest Region
region_cost = df.groupby('region')['charges'].mean()
highest_region = region_cost.idxmax()

insights.append(f"{highest_region} region has highest healthcare cost")

# 3. Risk Category
def risk_category(row):
    if row['smoker'] == 'yes' and row['bmi'] > 30 and row['age'] > 50:
        return 'High Risk'
    elif row['smoker'] == 'yes' or row['bmi'] > 30:
        return 'Medium Risk'
    else:
        return 'Low Risk'

df['risk_level'] = df.apply(risk_category, axis=1)

risk_counts = df['risk_level'].value_counts()
top_risk = risk_counts.idxmax()

insights.append(f"Most patients fall under {top_risk} category")

# Print
print("\n📊 AUTOMATED INSIGHTS:\n")
for i, insight in enumerate(insights, 1):
    print(f"{i}. {insight}")


# 4. Percentage-Based Insights

import pandas as pd

# Load dataset
df = pd.read_csv("../data/raw/healthcare_raw.csv")

insights = []

# ============================================
# 1. Smoker vs Non-Smoker
# ============================================

smoker_avg = df[df['smoker'] == 'yes']['charges'].mean()
non_smoker_avg = df[df['smoker'] == 'no']['charges'].mean()

if smoker_avg > non_smoker_avg:
    insights.append(
        f"Smokers have higher average charges ({round(smoker_avg,2)}) vs non-smokers ({round(non_smoker_avg,2)})"
    )

# ============================================
# 2. Highest Region
# ============================================

region_cost = df.groupby('region')['charges'].mean()
highest_region = region_cost.idxmax()

insights.append(f"{highest_region} region has highest healthcare cost")

# ============================================
# 3. Risk Category
# ============================================

def risk_category(row):
    if row['smoker'] == 'yes' and row['bmi'] > 30 and row['age'] > 50:
        return 'High Risk'
    elif row['smoker'] == 'yes' or row['bmi'] > 30:
        return 'Medium Risk'
    else:
        return 'Low Risk'

df['risk_level'] = df.apply(risk_category, axis=1)

risk_counts = df['risk_level'].value_counts()
top_risk = risk_counts.idxmax()

insights.append(f"Most patients fall under {top_risk} category")


# 4. Percentage-Based Insights (STEP 14)

# % Increase: Smoker vs Non-Smoker
percentage_increase = ((smoker_avg - non_smoker_avg) / non_smoker_avg) * 100

insights.append(
    f"Smokers spend {round(percentage_increase,2)}% more on healthcare than non-smokers"
)

# % Difference Between Regions
region_avg = df.groupby('region')['charges'].mean()

max_region = region_avg.max()
min_region = region_avg.min()

percent_diff_region = ((max_region - min_region) / min_region) * 100

highest_region = region_avg.idxmax()
lowest_region = region_avg.idxmin()

insights.append(
    f"{highest_region} region costs {round(percent_diff_region,2)}% more than {lowest_region}"
)

# ============================================
# PRINT (ALWAYS LAST)
# ============================================

print("\n📊 AUTOMATED INSIGHTS:\n")

for i, insight in enumerate(insights, 1):
    print(f"{i}. {insight}")