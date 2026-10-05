# UKCS Multivariate Anomaly Detection and Operational Risk Scoring

**Project 3 — Level 2 (Intermediate)**

An independent unsupervised machine-learning project using public NSTA/PPRS data for Schiehallion. It compares Isolation Forest, PCA reconstruction error, and transparent statistical consensus across 17 production features, then produces a traceable monthly risk score and review queue.
## Author

**Dr Khaldoun Shaker**  
Petroleum & Reservoir Engineer | Energy Data Analytics  
Edinburgh, United Kingdom  

Built as an independent professional portfolio project to apply my petroleum
and reservoir engineering experience to energy-data problems using Python,
SQL and machine learning. I reviewed the engineering assumptions, analytical
workflow, results and limitations.

© 2026 Khaldoun Shaker. All rights reserved.
## Why Level 2 is different

Level 1 screens each measure independently. This project models relationships between oil, gas, flaring, venting, injection, and produced water. It can therefore identify an unusual combination even when no individual value is extreme.

## Methods

- Isolation Forest: 400 trees, contamination 10%, seed 42
- PCA: seven components retaining 96.48% variance
- Statistical consensus: IQR, robust z-score, and context-aware rapid change
- Risk score: average of three percentile scores, bounded from 0 to 100

## Results

| Classification | Months |
|---|---:|
| High — at least two methods agree | 8 |
| Review — one method flags | 7 |
| Normal | 45 |

![Risk score timeline](outputs/charts/01_risk_score_timeline.png)

## Repository structure

```text
.
├── data/raw and data/processed
├── docs/                         # Methodology and bilingual report
├── models/                       # Scaler, Isolation Forest, PCA, metadata
├── outputs/charts                # Five portfolio figures
├── outputs/tables                # Scores, queue, rules, sensitivity
├── src/                          # Data, features, detection, pipeline
├── tests/
├── DATA_SOURCE.md
├── MODEL_CARD.md
├── run_project.py
└── requirements.txt
```

## Run

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run_project.py
python -m unittest discover -s tests -v
```

Main output: `outputs/tables/multivariate_review_queue.csv`.

## Responsible interpretation

This dataset has no verified anomaly labels. The project cannot claim precision, recall, or diagnostic accuracy. A high score means multiple statistical methods agree that the month is unusual; it does not mean an incident occurred.

---

## الملخص العربي

هذا هو **المشروع الثالث – المستوى الثاني**. بدلاً من فحص النفط أو الغاز أو الماء منفرداً، يبني النظام 17 خاصية تربطها معاً، ثم يقارن Isolation Forest وPCA والإجماع الإحصائي.

صُنفت ثمانية أشهر High وسبعة Review و45 Normal. درجة 100 تعني أن الشهر مرتفع الترتيب عند الطرق الثلاث، لكنها لا تعني احتمال عطل بنسبة 100%. النتائج مخصصة لترتيب المراجعة الهندسية فقط.

