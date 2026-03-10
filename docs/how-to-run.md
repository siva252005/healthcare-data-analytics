<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h2>🔢 Step-by-Step Execution</h2>

<h3>1️⃣ Setup Environment</h3>

<pre>
# Clone repository (if using Git)
git clone https://github.com/siva252005/healthcare-data-analytics.git

# Install dependencies
pip install pandas matplotlib seaborn scikit-learn streamlit jupyter
</pre>

<h3>2️⃣ Run Data Processing Pipeline</h3>

<pre>
# Clean raw data
python scripts/data_cleaning.py

# Create features
python scripts/feature_engineering.py

# Run EDA analysis
python scripts/eda_analysis.py
</pre>

<h3>3️⃣ Launch Jupyter Notebook (EDA)</h3>

<pre>
jupyter notebook notebooks/healthcare_analysis.ipynb
</pre>

<h3>6️⃣ Open Power BI Dashboard</h3>

<pre>
double-click healthcare_dashboard.pbix
</pre>

<hr>

<h2>📓 Jupyter Notebook Structure</h2>

<h3>healthcare_analysis.ipynb Contents:</h3>

<ol>
<li><strong>Project Introduction</strong> - Healthcare cost analysis overview</li>
<li><strong>Import Libraries</strong><br>
<code>import pandas as pd, matplotlib.pyplot as plt, seaborn as sns</code>
</li>
<li><strong>Load Dataset</strong><br>
<code>df = pd.read_csv("../data/processed/healthcare_cleaned.csv")</code>
</li>
<li><strong>Dataset Overview</strong><br>
<code>df.info() & df.describe()</code>
</li>
<li><strong>Exploratory Data Analysis</strong>
<ul>
<li>Charges by Smoker Status</li>
<li>Charges by Age Group</li>
<li>Charges by BMI Category</li>
<li>Charges by Region</li>
</ul>
</li>
<li><strong>Key Insights Summary</strong></li>
</ol>

<hr>

<h2>📈 Key Visualizations in Notebook</h2>

<h3>1. Charges by Smoking Status</h3>
<pre><code>sns.barplot(x="smoker", y="charges", data=df)
plt.title("Average Charges by Smoking Status")
plt.show()</code></pre>
<p><strong>Insight:</strong> Smoking significantly increases medical insurance charges.</p>

<h3>2. Charges by Age Group</h3>
<pre><code>sns.barplot(x="age_group", y="charges", data=df)
plt.title("Average Charges by Age Group")
plt.show()</code></pre>

<h3>3. Charges by BMI Category</h3>
<pre><code>sns.barplot(x="bmi_category", y="charges", data=df)
plt.title("Average Charges by BMI Category")
plt.show()</code></pre>

<h3>4. Charges by Region</h3>
<pre><code>sns.barplot(x="region", y="charges", data=df)
plt.title("Average Charges by Region")
plt.show()</code></pre>

<hr>

<h2>🔍 Key Insights (From EDA)</h2>

<ul>
<li><strong>Smokers</strong> have significantly higher insurance charges</li>
<li><strong>Obese patients</strong> (BMI > 30) incur higher healthcare costs</li>
<li><strong>Senior patients</strong> generally have higher insurance charges</li>
<li><strong>Southeast region</strong> shows highest average charges</li>
</ul>

<hr>

<h2>🎛️ Complete Execution Flow</h2>

<pre>
Raw Data (.csv)
     ↓
1️⃣ scripts/data_cleaning.py
     ↓
2️⃣ scripts/feature_engineering.py
     ↓
3️⃣ notebooks/healthcare_analysis.ipynb ← EDA + Visuals
     ↓
4️⃣ scripts/train_model.py
     ↓ → models/cost_prediction_model.pkl
5️⃣ app/app.py ← Streamlit Web App
     ↓
6️⃣ healthcare_dashboard.pbix ← Power BI Dashboard
</pre>

<hr>

<h2>⚡ Quick Commands Summary</h2>

<table border="1" cellpadding="8" cellspacing="0">
<thead>
<tr><th>Step</th><th>Command</th><th>Output</th></tr>
</thead>
<tbody>
<tr><td>1. Data Pipeline</td><td>python scripts/*.py</td><td>Cleaned CSV data</td></tr>
<tr><td>2. EDA Notebook</td><td>jupyter notebook</td><td>Visualizations + Insights</td></tr>
<tr><td>3. ML Training</td><td>python scripts/train_model.py</td><td>cost_prediction_model.pkl</td></tr>
<tr><td>4. Web App</td><td>streamlit run app/app.py</td><td>http://localhost:8501</td></tr>
<tr><td>5. Dashboard</td><td>healthcare_dashboard.pbix</td><td>Interactive BI Dashboard</td></tr>
</tbody>
</table>

<hr>

<h2>✅ Prerequisites</h2>

<ul>
<li>Python 3.8+</li>
<li>Jupyter Notebook</li>
<li>Power BI Desktop</li>
<li>Raw healthcare dataset (in data/raw/)</li>
</ul>

<hr>

<h2>📞 Troubleshooting</h2>

<ul>
<li><strong>Module not found:</strong> <code>pip install -r app/requirements.txt</code></li>
<li><strong>Jupyter not opening:</strong> <code>pip install notebook</code></li>
<li><strong>Streamlit port busy:</strong> Use <code>streamlit run app.py --server.port 8502</code></li>
<li><strong>Model not found:</strong> Run <code>python scripts/train_model.py</code> first</li>
</ul>

<hr>

<p><strong>🏥 Complete Healthcare Analytics Platform - Ready to Run! 🩺📊🤖🌐</strong></p>

</body>
</html>
