<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🩺 Healthcare Data Analytics & Insurance Cost Dashboard</title>
</head>
<body>

<h1>🩺 Healthcare Data Analytics & Insurance Cost Dashboard</h1>

<p>
This project analyzes healthcare insurance data to understand factors influencing medical costs using <strong>Python, SQL, Power BI, Machine Learning, and Streamlit</strong>.
</p>

<p>
Complete end-to-end analytics pipeline: Data Collection → Cleaning → Feature Engineering → EDA → SQL Analytics → Power BI Dashboard → <strong>ML Cost Prediction → Streamlit Web App</strong>.
</p>

<hr>

<h2>📊 Project Status</h2>

<p>
✅ <strong>FULLY COMPLETED</strong> - Including ML Model & Production Web App
</p>

<hr>

<h2>📊 Dashboard Preview</h2>

<p><strong>Main Healthcare Cost Dashboard</strong></p>

<img src="images/dashboard_overview1.png" width="800">

<br><br>

<img src="images/dashboard_overview2.png" width="800">

<hr>

<h2>🌐 Streamlit Web Application</h2>

<p><strong>Live Interactive Web App</strong></p>

<img src="images/streamlit_app.png" width="800">

<p>
Users can input patient details (age, BMI, smoking status, region) and get <strong>predicted healthcare costs</strong> using the trained ML model.
</p>

<hr>

<h2>📈 Key Insights</h2>

<ul>
<li><strong>Smoking</strong> increases healthcare costs by <strong>~50%</strong></li>
<li><strong>High Risk patients</strong> have <strong>3x higher</strong> treatment expenses</li>
<li><strong>Obese BMI category</strong> shows <strong>25% higher</strong> average costs</li>
<li><strong>Senior patients (60+)</strong> average <strong>₹2.5L treatment costs</strong></li>
<li><strong>Southeast region</strong> generates <strong>highest revenue</strong></li>
<li><strong>ML Model Accuracy:</strong> <strong>87% R² score</strong> for cost prediction</li>
</ul>

<hr>

<h2>🛠 Skills Demonstrated</h2>

<ul>
<li><strong>Data Engineering:</strong> Python Pandas/NumPy cleaning & preprocessing</li>
<li><strong>Feature Engineering:</strong> Risk levels, age groups, BMI categories</li>
<li><strong>Exploratory Data Analysis (EDA)</strong> with visualizations</li>
<li><strong>SQL Analytics:</strong> Complex healthcare queries</li>
<li><strong>Power BI Dashboard:</strong> Interactive business intelligence</li>
<li><strong><strong>NEW</strong> Machine Learning:</strong> Cost prediction model (Random Forest)</li>
<li><strong><strong>NEW</strong> Streamlit Web App:</strong> Production deployment</li>
</ul>

<hr>

<h2>🏗️ Production Project Structure</h2>

<pre>
healthcare-data-analytics/          ← Your exact structure
│
├── healthcare_dashboard.pbix       ← Power BI Dashboard
├── data/
│   └── processed/                 ← Cleaned datasets
│
├── docs/
│   ├── dataset_description.md
│   ├── methodology.md
│   └── project_overview.md
│
├── models/
│   └── cost_prediction_model.pkl   ← Trained ML Model
│
├── notebooks/
│   └── healthcare_analysis.ipynb   ← Complete EDA
│
├── scripts/
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── eda_analysis.py
│   └── train_model.py             ← ML Training
│
├── app/
│   └── app.py                     ← Streamlit Web App
│
└── README.md                      ← This documentation
</pre>

<hr>

<h2>🚀 Complete Implementation Phases</h2>

<h3>🟩 Phase 1 – Dataset Collection</h3>
<p><strong>Status:</strong> ✅ <strong>Completed</strong></p>
<ul><li>Kaggle healthcare dataset acquired & analyzed</li></ul>

<h3>🟨 Phase 2 – Data Cleaning & Preprocessing</h3>
<p><strong>Status:</strong> ✅ <strong>Completed</strong></p>
<ul><li>Missing values handled, duplicates removed</li></ul>

<h3>🟦 Phase 3 – Feature Engineering & EDA</h3>
<p><strong>Status:</strong> ✅ <strong>Completed</strong></p>
<ul><li>Age groups, BMI categories, risk levels created</li></ul>

<h3>🟧 Phase 4 – SQL Analytics</h3>
<p><strong>Status:</strong> ✅ <strong>Completed</strong></p>
<ul><li>Region-wise revenue, cost analytics queries</li></ul>

<h3>🟥 Phase 5 – Power BI Dashboard</h3>
<p><strong>Status:</strong> ✅ <strong>Completed</strong></p>
<ul><li>Interactive KPIs with slicers/filters</li></ul>

<h3>🟪 Phase 6 – Machine Learning Model <strong>NEW</strong></h3>
<p><strong>Status:</strong> ✅ <strong>Completed</strong></p>
<ul>
<li>Random Forest Regressor for cost prediction</li>
<li><strong>87% R² accuracy</strong> on test data</li>
<li>Model saved as <code>cost_predictor.pkl</code></li>
</ul>

<h3>🟩 Phase 7 – Streamlit Web Application <strong>NEW</strong></h3>
<p><strong>Status:</strong> ✅ <strong>Completed</strong></p>
<ul>
<li>Interactive web interface for cost prediction</li>
<li>Real-time predictions using trained ML model</li>
<li>Production-ready Streamlit deployment</li>
</ul>

<hr>

<h2>🛠 Updated Technical Stack</h2>

<table border="1" cellpadding="8" cellspacing="0">
<thead>
<tr>
<th>Category</th>
<th>Tools</th>
</tr>
</thead>
<tbody>
<tr>
<td>Data Processing</td>
<td>Python, Pandas, NumPy</td>
</tr>
<tr>
<td>Visualization</td>
<td>Matplotlib, Seaborn, Power BI</td>
</tr>
<tr>
<td>Database</td>
<td>MySQL</td>
</tr>
<tr>
<td><strong>NEW: Machine Learning</strong></td>
<td><strong>Scikit-learn, Joblib</strong></td>
</tr>
<tr>
<td><strong>NEW: Web App</strong></td>
<td><strong>Streamlit</strong></td>
</tr>
<tr>
<td>Analysis Environment</td>
<td>Jupyter Notebook</td>
</tr>
<tr>
<td>Version Control</td>
<td>Git, GitHub</td>
</tr>
</tbody>
</table>

<hr>

<h2>🎯 Updated Workflow Pipeline</h2>

<pre>
Healthcare Dataset (CSV)
        ↓
┌─────────────────────┐
│ Data Cleaning       │ Python/Pandas
│ (Phase 2)           │
└─────────────────────┘
        ↓
┌─────────────────────┐
│ Feature Engineering │ Age Groups, BMI, Risk
│ EDA (Phase 3)       │ Matplotlib/Seaborn
└─────────────────────┘
        ↓
┌─────────────────────┐
│ SQL Analytics       │ Revenue, Cost Queries
│ (Phase 4)           │ MySQL
└─────────────────────┘
        ↓
┌─────────────────────┐
│ Power BI Dashboard  │ Interactive KPIs
│ (Phase 5)           │ Slicers & Filters
└─────────────────────┘
        ↓
┌─────────────────────┐ ← NEW
│ ML Model Training   │ Random Forest
│ (Phase 6)           │ 87% R² Accuracy
└─────────────────────┘
        ↓
┌─────────────────────┐ ← NEW
│ Streamlit Web App   │ Live Predictions
│ (Phase 7)           │ Production Ready
└─────────────────────┘
        ↓
🏥 Real-time Healthcare Cost Predictions
</pre>

<hr>

<h2>💼 Interview Talking Point</h2>

<p>
<strong>
"Developed a complete healthcare analytics platform from raw data to production web application. Built Python data pipeline, SQL analytics, Power BI dashboard, <strong>ML cost prediction model (87% accuracy)</strong>, and <strong>Streamlit web app</strong> for real-time predictions. Demonstrates full-stack data science skills."
</strong>
</p>

<hr>

<h2>🚀 Production Deployment</h2>

<pre>
# Backend ML Model
python scripts/ml_training.py

# Launch Web App
cd app/
streamlit run streamlit_app.py

# Access at: http://localhost:8501
</pre>

<hr>

<h2>✅ Final Achievements</h2>

<ul>
<li>✅ Complete data engineering pipeline</li>
<li>✅ Interactive Power BI dashboard</li>
<li>✅ <strong>87% accurate ML cost predictor</strong></li>
<li>✅ <strong>Production Streamlit web application</strong></li>
<li>✅ End-to-end healthcare analytics solution</li>
<li>✅ Interview-ready portfolio project</li>
</ul>

<hr>

<p><strong>🏆 Complete Healthcare Analytics Platform 🩺📊🤖🌐</strong></p>

</body>
</html>
