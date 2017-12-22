from BinaryTree import ABR
from ARN import ARN
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import random
from timeit import default_timer as timer


def testHeight():
    size = 1
    x = []
    y = []
    z = []
    while size < 1000:
        tree = ABR()
        rbTree = ARN()
        print size
        x.append(size)
        for i in range(0, size):
            value = random.randint(1, size)
            tree.insert(value)
            rbTree.RBInsert(value)
        y.append(tree.getHeight(tree.root))
        print "Done"
        size += 50
        z.append(rbTree.getHeight(rbTree.root))
    print "Numero Elementi", x
    print "Altezza ABR", y
    print "Altezza ARN", z
    plt.plot(x, y, label="Albero Binario")
    plt.plot(x, z, label="Albero Rosso Nero")
    plt.legend(loc='upper left')
    plt.title('Alberi binari - Confronto Altezza')
    plt.ylabel('Altezza')
    plt.xlabel('Numero di elementi')
    plt.show()


def testInsertTime():
    x = []
    y = []
    z = []
    size = 10
    time = 0
    while size < 1000000:
        tree = ABR()
        rbTree = ARN()
        value = [0] * size
        x.append(size)
        start = timer()
        for i in range(1, size):
            value[i] = random.randint(1, size)
            tree.insert(value[i])
        end = timer()
        time = end-start
        y.append(time)
        print "Time ABR:", time
        start1 = timer()
        for j in range(1, size):
            rbTree.RBInsert(value[j])
        end1 = timer()
        time1 = end1-start1
        z.append(time1)
        print "Time ARN:", time1
        size *= 2
        print "Size: ", size
    print x
    print y
    print z
    plt.title("Alberi binari - Confronto Tempo di inserimento")
    plt.xlabel('# elementi inseriti')
    plt.ylabel('Tempo impiegato')
    plt.plot(x, y, label="Albero Binario")
    plt.plot(x, z, label="Albero Rosso Nero")
    plt.legend(loc='upper left')
    plt.show()


def testFindMinTime():
    x = []
    y = []
    z = []
    size = 1
    time = 0

    while size < 1000:
        print "Size: ", size
        tree = ABR()
        rbTree = ARN()
        x.append(size)
        for i in range(size, 0, -1):
            value = i
            tree.insert(value)
            rbTree.RBInsert(value)
        start = timer()
        tree.treeMinimum(tree.root)
        end = timer()
        time = end-start
        y.append(time)
        print "Time ABR:", time
        start1 = timer()
        rbTree.treeMinimum(rbTree.root)
        end1 = timer()
        time1 = end1-start1
        z.append(time1)
        print "Time ARN:", time1
        size += 50
    print x
    print y
    print z
    plt.title("Alberi binari - Confronto Tempo FindMin")
    plt.xlabel('# elementi inseriti')
    plt.ylabel('Tempo impiegato')
    plt.plot(x, y, label="Albero Binario")
    plt.plot(x, z, label="Albero Rosso Nero")
    plt.legend(loc='upper left')
    plt.show()


def testFindMaxTime():
    x = []
    y = []
    z = []
    size = 1
    time = 0

    while size < 1000:
        print "Size: ", size
        tree = ABR()
        rbTree = ARN()
        x.append(size)
        for i in range(0, size):
            value = i
            tree.insert(value)
            rbTree.RBInsert(value)
        start = timer()
        tree.treeMaximum(tree.root)
        end = timer()
        time = end-start
        y.append(time)
        print "Time ABR:", time
        start1 = timer()
        rbTree.treeMaximum(rbTree.root)
        end1 = timer()
        time1 = end1-start1
        z.append(time1)
        print "Time ARN:", time1
        size += 50

    plt.title("Alberi binari - Confronto Tempo FindMax")
    plt.xlabel('# elementi inseriti')
    plt.ylabel('Tempo impiegato')
    plt.plot(x, y, label="Albero Binario")
    plt.plot(x, z, label="Albero Rosso Nero")
    plt.legend(loc='upper left')
    plt.show()


def testSearch():
    x = []
    y = []
    z = []
    size = 1
    time = 0

    while size < 1000:
        print "Size: ", size
        tree = ABR()
        rbTree = ARN()
        x.append(size)
        for i in range(0, size):
            value = i
            tree.insert(value)
            rbTree.RBInsert(value)
        start = timer()
        tree.find(value)
        end = timer()
        time = end - start
        y.append(time)
        print "Time ABR", time
        start1 = timer()
        rbTree.find(value)
        end1 = timer()
        time1 = end1 - start1
        z.append(time1)
        print "Time ARN", time1
        size += 50

    plt.title("Alberi binari - Confronto Ricerca")
    plt.xlabel('# elementi inseriti')
    plt.ylabel('Tempo impiegato')
    plt.plot(x, y, label="Albero Binario")
    plt.plot(x, z, label="Albero Rosso Nero")
    plt.legend(loc='upper left')
    plt.show()
