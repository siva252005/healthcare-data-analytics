-- 🩺 Healthcare SQL Analytics

-- 🔹 1. Total Patients
SELECT COUNT(*) AS total_patients
FROM patients;

-- Insight:
-- The dataset contains 1337 patients used for healthcare analysis


-- 🔹 2. Total Healthcare Revenue
SELECT SUM(charges) AS total_revenue
FROM patients;

-- Insight:
-- Total healthcare revenue generated is approximately 17.75 million,
-- indicating high overall medical expenditure


-- 🔹 3. Average Treatment Cost
SELECT AVG(charges) AS avg_medical_cost
FROM patients;

-- Insight:
-- The average healthcare cost per patient is around 13,279,
-- showing moderate medical expenses across the dataset


-- 🔹 4. Smoking Impact Analysis 🔥
SELECT smoker,
       COUNT(*) AS patients,
       AVG(charges) AS avg_cost
FROM patients
GROUP BY smoker;

-- Insight:
-- Smokers (274 patients) have a very high average cost (~32,050)
-- Non-smokers (1063 patients) have much lower average cost (~8,440)
-- Smoking is the most significant factor affecting medical expenses


-- 🔹 5. Age Group Cost Analysis
SELECT age_group,
       COUNT(*) AS patients,
       AVG(charges) AS avg_cost
FROM patients
GROUP BY age_group;

-- Insight:
-- Senior group has the highest average cost (~17,902)
-- Middle Age group has moderate cost (~13,123)
-- Young group has the lowest cost (~9,200)
-- Medical expenses increase with age


-- 🔹 6. BMI Category Cost Analysis
SELECT bmi_category,
       COUNT(*) AS patients,
       AVG(charges) AS avg_cost
FROM patients
GROUP BY bmi_category;

-- Insight:
-- Obese category has the highest average cost (~15,572)
-- Overweight and Normal categories show moderate costs
-- Underweight group has the lowest cost
-- Higher BMI is associated with increased healthcare expenses


-- 🔹 7. Region-wise Revenue Analysis
SELECT region,
       COUNT(*) AS patients,
       SUM(charges) AS total_revenue,
       AVG(charges) AS avg_cost
FROM patients
GROUP BY region;

-- Insight:
-- Southeast region generates the highest revenue (~5.36M)
-- It also has the highest average cost (~14,735)
-- Regional differences exist but are less impactful than smoking


-- 🔹 8. Risk Level Analysis 🔥
SELECT risk_level,
       COUNT(*) AS patients,
       AVG(charges) AS avg_cost,
       SUM(charges) AS total_revenue
FROM patients
GROUP BY risk_level;

-- Insight:
-- High Risk group has extremely high average cost (~41,692)
-- Medium Risk group shows moderate cost (~21,369)
-- Low Risk group has lowest cost (~8,440)
-- Risk classification strongly predicts medical expenses


-- 🔹 9. Top 10 Highest Cost Patients
SELECT *
FROM patients
ORDER BY charges DESC
LIMIT 10;

-- Insight:
-- Top patients have charges above 48,000+
-- Most of them are smokers and belong to obese category
-- High-cost patients are typically high-risk individuals


-- 🔹 10. Average Charges (Recheck KPI)
SELECT AVG(charges) AS avg_charges
FROM patients;

-- Insight:
-- Confirms overall average healthcare cost (~13,279)


-- 🔹 11. Smoker vs Non-Smoker (Simple View)
SELECT smoker, AVG(charges) AS avg_cost
FROM patients
GROUP BY smoker;

-- Insight:
-- Reinforces that smokers incur nearly 4x higher costs than non-smokers


-- 🔹 12. Region Average Cost
SELECT region, AVG(charges) AS avg_cost
FROM patients
GROUP BY region;

-- Insight:
-- Southeast region has highest average charges
-- Other regions show similar moderate costs


-- 🔹 13. Age Group Average Cost
SELECT age_group, AVG(charges) AS avg_cost
FROM patients
GROUP BY age_group;

-- Insight:
-- Senior group contributes highest medical expenses
-- Clear increasing trend with age


-- 🔹 14. BMI Category Average Cost
SELECT bmi_category, AVG(charges) AS avg_cost
FROM patients
GROUP BY bmi_category;

-- Insight:
-- Obese individuals have significantly higher costs
-- BMI is a strong health cost indicator



-- 🔥 15. Risk Categorization using CASE
-- ============================================

/*
📊 Insight:
- Most patients fall under Medium Risk due to either smoking or high BMI
- Even non-smokers with BMI > 30 are classified as Medium Risk
- High-risk category is rare because it requires multiple severe conditions
- Smoking + BMI is a strong risk indicator

👉 Real-world:
Insurance companies use similar logic to assign premiums

📌 Fact: Smoking and age are major drivers of healthcare cost
*/

SELECT *,
CASE 
    WHEN smoker = 'yes' AND bmi > 30 AND age > 50 THEN 'High Risk'
    WHEN smoker = 'yes' OR bmi > 30 THEN 'Medium Risk'
    ELSE 'Low Risk'
END AS calculated_risk
FROM patients;



-- 🔥 16. Patients Above Average Cost
-- ============================================

/*
📊 Insight:
- Only a subset of patients generate above-average costs
- These patients represent a high financial risk group
- Likely includes smokers, older individuals, and high BMI patients

👉 Real-world:
Used for premium pricing & risk management
*/

SELECT *
FROM patients
WHERE charges > (
    SELECT AVG(charges) FROM patients
);



-- 🔥 17. Top Revenue Region
-- ============================================

/*
📊 Insight:
- Southeast region generates the highest insurance revenue
- Indicates higher medical costs and higher risk population

📌 Real-world pattern:
Southeast often shows higher insurance costs
*/

SELECT region, SUM(charges) AS total_revenue
FROM patients
GROUP BY region
ORDER BY total_revenue DESC
LIMIT 1;



-- 🔥 18. Ranking Patients by Cost
-- ============================================

/*
📊 Insight:
- Helps identify top spenders (high-cost patients)
- Few patients contribute to major portion of total cost
- Cost distribution is highly skewed

👉 Real-world:
Used in fraud detection and high-risk patient tracking
*/

SELECT *,
RANK() OVER (ORDER BY charges DESC) AS cost_rank
FROM patients;



-- 🔥 19. Avg Cost by Region & Smoker
-- ============================================

/*
📊 Insight:
- Smokers have very high average cost (~3–4x higher)
- Non-smokers have significantly lower cost
- Southeast smokers = highest cost group

📌 Key takeaway:
Smoking is the strongest cost driver
*/

SELECT region, smoker, AVG(charges) AS avg_cost
FROM patients
GROUP BY region, smoker;



-- 🔥 20. Running Total Analysis
-- ============================================

/*
📊 Insight:
- Healthcare cost increases gradually with age
- Older age groups contribute more to total expenses
- Cumulative cost rises continuously

👉 Real-world:
Used for lifetime cost prediction in insurance
*/

SELECT age, charges,
SUM(charges) OVER (ORDER BY age) AS running_total
FROM patients;