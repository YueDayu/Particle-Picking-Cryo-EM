import os
import six
import pickle

from sklearn.svm import SVC
from sklearn import decomposition

from load import load_data


def pca(X):
    pca = decomposition.PCA(n_components=25*25)
    pca.fit(X)
    X = pca.transform(X)
    return X


def main():
    six.print_('loading data')
    train_x, train_y, val_x, val_y = load_data()
    train_x = train_x.reshape(-1, 64 * 64)
    val_x = val_x.reshape(-1, 64 * 64)
    six.print_('load data complete')

    train_x = pca(train_x)
    six.print_('PCA complete')

    clf = SVC(C=0.001, verbose=True, max_iter=100)
    six.print_('start training')
    clf.fit(train_x, train_y)
    six.print_('training complete')

    acc = sum(val_y == clf.predict(val_x)) / float(len(val_y))
    print(acc)


if __name__ == '__main__':
    main()