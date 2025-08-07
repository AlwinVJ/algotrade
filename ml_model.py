from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from ta.trend import MACD
import pandas as pd

def build_model(df):
    print("Columns at start of model:", df.columns.tolist())

    # Step 1: Detect the correct 'Volume_*' column
    volume_cols = [col for col in df.columns if col.startswith("Volume")]
    if not volume_cols:
        raise ValueError("❌ No Volume column found in DataFrame.")
    volume_col = volume_cols[0]

    # Step 2: Check if RSI is available
    if 'rsi' not in df.columns:
        raise ValueError("❌ RSI column missing. Please run apply_indicators(df) before build_model().")

    # Step 3: Add MACD
    macd = MACD(close=df['ClosePrice_' + volume_col.split("_")[1]].squeeze())  # Use same ticker suffix
    df['macd'] = macd.macd()

    # Step 4: Drop rows with any missing values in features
    required_cols = ['rsi', 'macd', volume_col]
    df.dropna(subset=required_cols, inplace=True)

    # Step 5: Create binary target (1 if next day’s close is higher, else 0)
    close_col = 'ClosePrice_' + volume_col.split("_")[1]
    df['target'] = (df[close_col].shift(-1) > df[close_col]).astype(int)
    df.dropna(subset=['target'], inplace=True)

    # Step 6: Build logistic regression model
    X = df[['rsi', 'macd', volume_col]]
    y = df['target']

    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)

    accuracy = accuracy_score(y, model.predict(X))

    print(f"Model trained. Accuracy: {accuracy:.2%}")
    return model, round(accuracy * 100, 2)
