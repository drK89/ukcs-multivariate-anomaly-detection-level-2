from pathlib import Path
from src.pipeline import run

if __name__ == "__main__":
    result=run(Path(__file__).resolve().parent)
    print(f"Features: {result['feature_count']}")
    print(f"PCA components: {result['pca_components']}")
    print(f"High months: {result['high_months']}")
    print(f"Review months: {result['review_months']}")
    print(f"Normal months: {result['normal_months']}")

