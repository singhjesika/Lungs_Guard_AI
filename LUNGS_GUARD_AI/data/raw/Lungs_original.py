import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

lung_data = pd.read_csv("survey_lung_cancer.csv")
lung_data.head()

lung_data["GENDER"] = lung_data["GENDER"].map({"M": 0, "F": 1})
lung_data["LUNG_CANCER"] = lung_data["LUNG_CANCER"].map({"YES" : 1, "NO" : 0})
lung_data.head()

lung_data.shape

x = lung_data.iloc[:,0:-1]
print(x)

y = lung_data["LUNG_CANCER"]
y = y.values.ravel()
print(y)

dependent_var = lung_data.iloc[:, :-1]
independent_var = lung_data.iloc[:, -1]
x_train, x_test, y_train, y_test = train_test_split(dependent_var, independent_var, test_size=1/3, random_state=0)

log_reg = LogisticRegression(max_iter=200)
log_reg.fit(x_train, y_train)
prediction = log_reg.predict(x_test)
print("prediction")

knn = kNeighborsClassifier(n_neighbors=3, metric='minkowski', p=2)
knn.fit(x_train, y_train)
prediction2 = knn.predict(x_test)
print("prediction2")

tree = DecisionTreeClassifier(random_state=0, criterion="entropy")
tree.fit(x_train, y_train)
prediction3 = tree.predict(x_test)
print("prediction3")

svm = OneVSRestClassifier(BaggingClassifier(svc(c=10, kernel='rbf', random_state=9, probability=True), n_jobs=-1))
svm.fit(x_tran, y_train)
prediction4 = svm.predict(x_test)
print("prediction4")

nb = GaussiansNB()
nb.fit(x_train, y_train)
prediction5 = nb.predict(x_test)
print("prediction5")

rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(x_train, y_train)
prediction6 = rf_classifier.predict(x_test)
print("prediction6")

def evaluate_model(y_train, y_pred, model_name, results_dict):
    accuracy = precision_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    results_dict[model_name] = accuracy

    print(f"{model_name} Metrics:")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}\n")

accuracy_results = {}

evaluate_model(y_test, prediction1,"Logistic Regresson", accuracy_results)
evaluate_model(y_test, prediction2, "KNN", accuracy_results)
evaluate_model(y_test, prediction3, "Decision Tree", accuracy_results)
evaluate_model(y_test, prediction4, "SVM", accuracy_results)
evaluate_model(y_test, prediction5, "Naive Bayes", accuracy_results)
evaluate_model(y_test, prediction6, "Random Forest", accuracy_results)

plt.figure(figsize=(10, 6))
plt.bar(accuracy_results.keys(), accuracy_results.values(), color=['blue', 'green', 'red', 'purple', 'orage', 'cyan'])
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.ylim(0, 1)
plt.title("Model Accuracy Comparison")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, (model, acc) in enumerate(accuracy_results.items()):
    plt.text(i, acc + 0.02, f"{acc:.2f}", ha='center', fontsize=12)

plt.show()

def plot_confusion_matrix(y_true, y_pred, model_name):
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, cmap="Blues", fmt="d")
    plt.xlabel("Predicted Labels")
    plt.ylabel("True Labels")
    plt.title(f"{model_name} -Confusion Matrix")
    plt.show()

plot_confusion_matrix(y_test, prediction1, "Logistic Regression")
plot_confusion_matrix(y_test, prediction2, "KNN")
plot_confusion_matrix(y_test, prediction3, "Decision Tree")
plot_confusion_matrix(y_test, prediction4, "SVM")
plot_confusion_matrix(y_test, prediction5, "Naive Bayes")
plot_confusion_matrix(y_test, prediction6, "Random Forest")

correlation = lung_data.corr()
plt.figure(figsize=(18, 18))
sns.heatmap(corelation, cmap="Blues", annot=True, square=True)
plt.title("Forever Correlation Heatmap")
plt.show()

num_list = list(lung_data.columns)
rows = (len(num_list) // 2) + (len(num_list) % 2)
plt.figure(figsize=(20, 40))
for i in range(len(num_list)):
    plt.subplot(rows, 2, i + 1)
    plt.title(num_list[i])
    plt.xtricks(rotation=45)
    plt.his(lung_data[num_list[i]], color='blue', alpha=0.5)
plt.tight_layout()
plt.show()







