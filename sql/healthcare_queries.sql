-- Check total patients
SELECT COUNT(*) AS total_patients
FROM patients;

-- Total hospital revenue
SELECT SUM(charges) AS total_revenue
FROM patients;

-- Average treatment cost
SELECT AVG(charges) AS avg_medical_cost
FROM patients;

-- Smoking impact analysis
SELECT smoker,
       COUNT(*) AS patients,
       AVG(charges) AS avg_cost
FROM patients
GROUP BY smoker;

-- Age group cost analysis
SELECT age_group,
       COUNT(*) AS patients,
       AVG(charges) AS avg_cost
FROM patients
GROUP BY age_group;

-- BMI category cost analysis
SELECT bmi_category,
       COUNT(*) AS patients,
       AVG(charges) AS avg_cost
FROM patients
GROUP BY bmi_category;

-- Region wise revenue
SELECT region,
       COUNT(*) AS patients,
       SUM(charges) AS total_revenue,
       AVG(charges) AS avg_cost
FROM patients
GROUP BY region;

-- Risk level analysis
SELECT risk_level,
       COUNT(*) AS patients,
       AVG(charges) AS avg_cost,
       SUM(charges) AS total_revenue
FROM patients
GROUP BY risk_level;

-- Top 10 highest cost patients
SELECT *
FROM patients
ORDER BY charges DESC
LIMIT 10;