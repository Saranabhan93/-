import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(df)
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df = df.drop(columns=['Cabin'])


df['Name'] = df['Name'].str.title()

print(df)

grouped = df.groupby('Pclass').agg(
    mean_fare=('Fare', 'mean'),
    passenger_count=('Pclass', 'count')
).reset_index()

print(grouped)
class_desc = pd.DataFrame({
    'Pclass': [1, 2, 3],
    'ClassDescription': ['Upper', 'Middle', 'Lower']
})

merged = pd.merge(grouped, class_desc, on='Pclass')

print(merged)
pivot = df.pivot_table(values='Fare', index='Embarked', columns='Sex', aggfunc='mean')
pivot = pivot.fillna(0)

print(pivot)
def get_travel_group(row):
    total = row['SibSp'] + row['Parch'] + 1
    if total == 1:
        return 'Solo'
    elif total <= 3:
        return 'Small'
    else:
        return 'Large'

df['TravelGroup'] = df.apply(get_travel_group, axis=1)

print(df[['SibSp', 'Parch', 'TravelGroup']])
Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df['Fare'] = df['Fare'].clip(lower=lower_bound, upper=upper_bound)

print(df['Fare'].describe())
summary = {
    'mean_fare': df['Fare'].mean(),
    'max_travel_group_size': (df['SibSp'] + df['Parch'] + 1).max()
}

print(summary)
# استخدمت طريقة IQR لمعالجة القيم الشاذة بعمود Fare
# أي قيمة أقل من Q1-1.5×IQR أو أكبر من Q3+1.5×IQR تعتبر شاذة، وتم تعديلها لأقرب حد مسموح
