# Model Card | بطاقة النماذج

## Purpose

An intermediate unsupervised screening system that compares Isolation Forest, PCA reconstruction error, and explainable statistical rules across 17 multivariate production features.

## Inputs

Six monthly measures are transformed into:

- six log-level features;
- six log-change features;
- gas/oil, produced-water/oil, injected-water/oil, flare/gas, and vent/gas ratios.

`RobustScaler` reduces scale sensitivity. PCA retains at least 95% of feature variance. Isolation Forest uses 400 trees, contamination 10%, and random seed 42.

## Decision policy

- **High:** at least two methods flag the month.
- **Review:** exactly one method flags the month.
- **Normal:** no method flags the month.
- **Risk score:** average percentile rank of Isolation Forest score, PCA error, and statistical trigger count.

## Result

Eight high months, seven review months, and 45 normal months. April 2021 is the only displayed example with all three methods agreeing and a risk score of 100. These are screening results, not verified operational incidents.

## Limitations

- No labelled anomalies; precision, recall, and F1 cannot be claimed.
- Contamination is an analyst assumption, not an observed incident rate.
- Top drivers are the largest robust-scaled deviations, not causal explanations.
- Relationships can reflect legitimate operational transitions.
- Not for alarms, shutdown decisions, safety, compliance, or reservoir diagnosis.

## العربية

يقارن النظام بين Isolation Forest وخطأ إعادة البناء في PCA والقواعد الإحصائية عبر 17 خاصية. الشهر العالي هو الذي تتفق عليه طريقتان على الأقل. لا توجد تسميات حقيقية للأعطال، ولذلك النتائج قائمة مراجعة وليست تشخيصاً أو نظام إنذار تشغيلياً.

