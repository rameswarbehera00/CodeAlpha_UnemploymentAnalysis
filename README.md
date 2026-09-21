# Unemployment Analysis with Python — CodeAlpha Data Science Internship

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458?logo=pandas)
![Seaborn](https://img.shields.io/badge/Library-Seaborn-3776AB?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

An end-to-end Exploratory Data Analysis and statistical visualization project developed for the **CodeAlpha Data Science Internship**. This project evaluates the socioeconomic impact of the COVID-19 nationwide lockdowns on India's employment landscape across rural and urban sectors.

---

## 📌 Project Overview

This project analyzes the temporal fluctuations and regional disparities in India's unemployment figures before and during the COVID-19 pandemic. By performing comparative statistical evaluations and time-series decompositions, the project identifies vulnerable geographies and sector-specific recovery trajectories.

### Core Objectives
- Clean, standardize, and impute missing records from raw survey datasets.
- Track national unemployment trends across pre-lockdown and lockdown timelines.
- Quantify disparities between **Rural** and **Urban** labor markets.
- Identify the most severely impacted states and regional hotspots.

---

## 📁 Repository Structure

```text
CodeAlpha_UnemploymentAnalysis/
├── data/
│   ├── Unemployment in India.csv              # Raw survey dataset
│   └── Cleaned_Unemployment_India.csv        # Processed dataset with derived features
├── notebooks/
│   └── Unemployment_analysis.ipynb           # Interactive EDA, plotting, and statistical testing
├── outputs/
│   ├── 1_unemployment_timeline.png            # National monthly trendline
│   ├── 2_pre_vs_post_lockdown_distribution.png # Rural vs Urban distribution boxplots
│   ├── 3_top10_affected_states.png            # State-wise lockdown peak analysis
│   └── 4_correlation_heatmap.png              # Labor participation & employment matrix
├── src/
│   ├── clean_data.py                          # Data cleaning, null handling & ISO parsing
│   ├── visualize_trends.py                    # Static chart generation pipeline
│   └── generate_insights.py                   # Automated summary & metric extraction
├── .gitignore                                 # Environment and cache ignore rules
├── LICENSE                                    # MIT License
├── README.md                                  # Complete project documentation
└── requirements.txt                           # Project dependencies

```

---

## 🧹 Data Cleaning Pipeline

* **Header Normalization:** Stripped leading and trailing whitespace across all column names.
* **Missing Value Imputation:** Dropped 28 completely blank observation records (`NaN` across all features).
* **Date Parsing & Feature Engineering:** Transformed raw string dates into ISO standard `datetime64` (`dayfirst=True`) and engineered derived temporal attributes: `Year`, `Month`, and `Period` (Pre-Lockdown vs. Lockdown).

---

## 🔬 Key Insights & Findings

| Metric / Scenario | Pre-Lockdown (May 2019 – Mar 2020) | Lockdown Phase (Apr 2020 – Jun 2020) | Net Change |
| --- | --- | --- | --- |
| **Mean National Unemployment** | 9.61% | 20.19% | **+110.03% surge** |
| **Urban Peak Unemployment** | 10.45% | 22.08% | **+111.29% surge** |
| **Rural Peak Unemployment** | 8.87% | 18.26% | **+105.86% surge** |

### Critical Observations

* **Lockdown Shock:** The immediate onset of nationwide mobility curbs triggered an unprecedented spike in unemployment, peaking in April–May 2020.
* **Urban Vulnerability:** Urban regions faced sharper contractions due to stringent shutdowns in retail, manufacturing, hospitality, and daily-wage services. Rural labor was partially cushioned by agricultural seasons and MGNREGA programs.
* **Severely Affected States:**
1. **Puducherry:** 57.70% average lockdown unemployment
2. **Jharkhand:** 44.90%
3. **Haryana:** 37.69%
4. **Bihar:** 36.99%



---

## 🏛️ Policy Implications

* **Targeted Urban Safety Nets:** Rural relief mechanisms like MGNREGA proved crucial; establishing an equivalent urban employment guarantee scheme would buffer non-agricultural informal wage earners during external shocks.
* **State Buffer Funds:** High-volatility economies (e.g., Jharkhand, Bihar) require targeted micro-lending, supply chain continuity mechanisms, and localized emergency relief funds.

---

## 🚀 Getting Started (Windows Setup)

### 1. Clone the Repository

```cmd
git clone [https://github.com/rameswarbehera00/CodeAlpha_UnemploymentAnalysis.git](https://github.com/rameswarbehera00/CodeAlpha_UnemploymentAnalysis.git)
cd CodeAlpha_UnemploymentAnalysis

```

### 2. Set Up Virtual Environment & Dependencies

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

```

### 3. Run Data Cleaning

```cmd
python src\clean_data.py

```

### 4. Generate Visualizations

```cmd
python src\visualize_trends.py

```

### 5. Generate Summary Insights

```cmd
python src\generate_insights.py

```

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
