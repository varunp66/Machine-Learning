# In classification problem, accuract is the cmmonly used metric

# The accuracy is Defined = Number of Correct Predictions/ Total Number of Data Points

# The main objective of accuracy is how our model perform on new data.

'''

We can Train and Test the model by using the following steps:

from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(X,y, test_sixe = 0.3,
                                        random_state=21, stratify = y)

Note: Here test_size is 30% of original data.
      random_state is same as 'random seed'.
      On running the code,we will get 4 arrays as an output. the Training Data,
      Test Data, Training Labels and the test labels.
      By default the model splits the data in 75%:25% ratio i.e. 75% Training Data
      and 25% Test data.
      If we want our Labels to be distributed in the same we as they are in the
      original data set, Hence we are using the keyword 'stratify =y' in our code,
      where y is the list or arrays containing the Labels.

knn = KNeighborsClassifier(n_neighbors=8)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print("Test set predictions: \n{}".format(y_pred))

# To chack the accuracy of our Model we use 'score' method

knn.score(X_test, y_test)

NOTE: IF THE VALUE OF 'N' IS HIGH, THE MODEL BECOMES LESS CURVY/ COMPLEX.
      Hence the model will perform less well.
      IF THE VALUE OF 'N' IS LOW, THEN THE MODEL WILL BECOME MORE CURVY/COMPLEX
      AND WILL RESULT IN OVERFITTING.

Larger K = Smooth decision boundary = Less Complex Model
Smaller K = more complex model = Can lead to Over Fitting

'''

# Import necessary modules
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split

# Create feature and target arrays
X = digits.data
y = digits.target

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42, stratify=y)

# Create a k-NN classifier with 7 neighbors: knn
knn = KNeighborsClassifier(n_neighbors=7)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Print the accuracy
print(knn.score(X_test, y_test))


