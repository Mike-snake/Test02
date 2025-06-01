

import pandas as pd
df = pd.read_csv("./auto-mpg.csv",
                 names=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name'])

# horsepower column을 정수화, 그리고 NaN 값 처리
df["horsepower"] = pd.to_numeric(df["horsepower"], errors="coerce")

bins = [0, 100, 150, float("inf")]              # 범위 설정
labels = ["저출력", "중간출력", "고출력"]       # 각 범주명

#horsepower column을 카테고리 화
df["horsepower"] = pd.cut(df["horsepower"], bins=bins, labels=labels)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', None)

#print(df["horsepower"])
#print(df)
print(df[df.isnull().axis==1])

