import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(df)

# الخطوة 1: معالجة القيم المفقودة
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df = df.drop(columns=['Cabin'])

# الخطوة 2: إزالة التكرارات (صفوف مكررة بالكامل)
df = df.drop_duplicates()

print("Number of rows after removing duplicates:", len(df))

# الخطوة 3: توحيد صيغة الأسماء
df['Name'] = df['Name'].str.title()

print(df)

# الخطوة 4: هندسة ميزة جديدة - تصنيف الركاب حسب الفئة العمرية
def get_age_group(age):
    if age < 18:
        return 'Child'
    elif age < 60:
        return 'Adult'
    else:
        return 'Senior'

df['AgeGroup'] = df['Age'].apply(get_age_group)

print(df[['Age', 'AgeGroup']])

# الخطوة 5: معالجة القيم الشاذة (Outliers) في عمود Fare باستخدام IQR
# استخدمت طريقة IQR لأنها بسيطة وموثوقة لمعالجة القيم الشاذة
# أي قيمة أقل من Q1-1.5×IQR أو أكبر من Q3+1.5×IQR تعتبر شاذة، وتم تعديلها لأقرب حد مسموح
Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df['Fare'] = df['Fare'].clip(lower=lower_bound, upper=upper_bound)

print(df['Fare'].describe())

# الخطوة 6: عرض النتيجة النهائية وملخص إحصائي
summary = {
    'total_rows': len(df),
    'mean_fare': df['Fare'].mean(),
    'age_group_counts': df['AgeGroup'].value_counts().to_dict()
}

print(summary)
