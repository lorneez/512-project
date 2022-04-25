import matplotlib.pyplot as plt
import numpy as np 

def obtainData(experiment):
    if experiment == "basic normal":
        return [[100, 0, 0], [100, 0, 0]]
    elif experiment == "basic quadratic":
        return [[68, 31, 1], [100, 0, 0]]
    elif experiment == "basic pqv":
        return [[22, 34, 44], [36, 22, 42]]
    elif experiment == "increasing percentage quadratic 30":
        return [[44, 52, 4], [59, 39, 2], [67, 28, 5], [81, 19, 0], [87, 11, 2], [94, 4, 2], [94, 6, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0]]
    elif experiment == "increasing percentage pqv 30":
        return [[36, 18, 46], [35, 24, 41], [39, 22, 39], [30, 24, 46], [27, 19, 54], [33, 23, 44], [37, 23, 40], [31, 21, 48], [26, 21, 53], [31, 22, 47], [32, 24, 44], [36, 19, 45], [41, 23, 36], [28, 27, 45], [40, 20, 40], [31, 26, 43], [32, 25, 43], [36, 19, 45], [38, 26, 36], [35, 23, 42], [38, 17, 45], [35, 23, 42], [31, 24, 45], [26, 25, 49], [36, 19, 45], [24, 20, 56], [37, 21, 42], [41, 25, 34], [33, 27, 40], [20, 21, 59], [38, 26, 36]]
    elif experiment == "increasing percentage pqv 100":
        return [[31, 23, 46], [25, 29, 46], [26, 25, 49], [25, 23, 52], [35, 22, 43], [35, 20, 45], [36, 30, 34], [37, 22, 41], [31, 17, 52], [32, 19, 49], [25, 29, 46], [33, 20, 47], [41, 23, 36], [37, 19, 44], [28, 24, 48], [36, 27, 37], [37, 17, 46], [38, 16, 46], [37, 16, 47], [33, 23, 44], [30, 26, 44], [25, 26, 49], [31, 21, 48], [32, 28, 40], [34, 16, 50], [33, 17, 50], [35, 23, 42], [38, 20, 42], [35, 18, 47], [36, 19, 45], [38, 17, 45], [37, 22, 41], [39, 21, 40], [30, 27, 43], [29, 31, 40], [32, 17, 51], [43, 24, 33], [33, 20, 47], [35, 23, 42], [30, 26, 44], [28, 23, 49], [35, 18, 47], [36, 29, 35], [31, 21, 48], [33, 24, 43], [30, 22, 48], [31, 21, 48], [28, 18, 54], [37, 23, 40], [40, 20, 40], [32, 15, 53], [41, 16, 43], [36, 19, 45], [43, 15, 42], [40, 21, 39], [35, 23, 42], [35, 23, 42], [42, 16, 42], [44, 16, 40], [45, 14, 41], [38, 20, 42], [31, 23, 46], [44, 19, 37], [36, 18, 46], [44, 20, 36], [45, 22, 33], [35, 17, 48], [41, 19, 40], [38, 24, 38], [49, 15, 36], [39, 20, 41], [42, 13, 45], [47, 17, 36], [43, 11, 46], [48, 12, 40], [41, 22, 37], [51, 13, 36], [46, 18, 36], [46, 14, 40], [53, 15, 32], [53, 15, 32], [51, 8, 41], [52, 11, 37], [48, 18, 34], [51, 15, 34], [48, 10, 42], [50, 8, 42], [59, 9, 32], [56, 12, 32], [58, 9, 33], [62, 13, 25], [56, 9, 35], [65, 7, 28], [69, 7, 24], [56, 11, 33], [67, 2, 31], [77, 4, 19], [79, 2, 19], [83, 3, 14], [95, 0, 5], [100, 0, 0]]


def plotBasicExperiments():
    normal_data = obtainData("basic normal")
    quadratic_data = obtainData("basic quadratic")
    pqv_data = obtainData("basic pqv")
    X = ["Pass", "Fail", "Tie"]
    X_axis = X_axis = np.arange(len(X))
    
    plt.subplot(1, 3, 1)
    plt.bar(X_axis - 0.2, normal_data[0], 0.4, label = 'No Partition')
    plt.bar(X_axis + 0.2, normal_data[1], 0.4, label = 'Partition')
    plt.xticks(X_axis, X)
    plt.title('Normal Voting Protocol')
    plt.xlabel('Vote Status')
    plt.ylabel('Percentage')
    plt.legend()

    plt.subplot(1, 3, 2)
    plt.bar(X_axis - 0.2, quadratic_data[0], 0.4, label = 'No Partition')
    plt.bar(X_axis + 0.2, quadratic_data[1], 0.4, label = 'Partition')
    plt.xticks(X_axis, X)
    plt.title('Quadratic Voting Protocol')
    plt.xlabel('Vote Status')
    plt.ylabel('Percentage')
    plt.legend()
    
    plt.subplot(1, 3, 3)
    plt.bar(X_axis - 0.2, pqv_data[0], 0.4, label = 'No Partition')
    plt.bar(X_axis + 0.2, pqv_data[1], 0.4, label = 'Partition')
    plt.xticks(X_axis, X)
    plt.title('PQV Voting Protocol')
    plt.xlabel('Vote Status')
    plt.ylabel('Percentage')
    plt.legend()
    plt.show()

def plotIncreasingPercentageExperiments(max_percentage):
    if max_percentage == 30:

        quadratic_30_data = obtainData("increasing percentage quadratic 30")
        pass_quadratic_data = []
        fail_quadratic_data = []
        tie_quadratic_data = []

        for entry in quadratic_30_data:
            pass_quadratic_data.append(entry[0])
            fail_quadratic_data.append(entry[1])
            tie_quadratic_data.append(entry[2])

        pqv_30_data = obtainData("increasing percentage pqv 30")
        pass_pqv_data = []
        fail_pqv_data = []
        tie_pqv_data = []

        for entry in pqv_30_data:
            pass_pqv_data.append(entry[0])
            fail_pqv_data.append(entry[1])
            tie_pqv_data.append(entry[2])

        X_axis = X_axis = np.arange(len(pass_quadratic_data))

        plt.subplot(1, 2, 1)
        plt.plot(X_axis, pass_quadratic_data, label="Pass")
        plt.plot(X_axis, fail_quadratic_data, label="Fail")
        plt.plot(X_axis, tie_quadratic_data, label="Tie")
        plt.title('Increasing Percentage Quadratic Voting Protocol')
        plt.xlabel('Attacker Percentage Owned')
        plt.ylabel('Percentage')
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(X_axis, pass_pqv_data, label="Pass")
        plt.plot(X_axis, fail_pqv_data, label="Fail")
        plt.plot(X_axis, tie_pqv_data, label="Tie")
        plt.title('Increasing Percentage PQV Voting Protocol')
        plt.xlabel('Attacker Percentage Owned')
        plt.ylabel('Percentage')
        plt.legend()

        plt.show()
        
    elif max_percentage == 100:
        pqv_100_data = obtainData("increasing percentage pqv 100")
        pass_pqv_data = []
        fail_pqv_data = []
        tie_pqv_data = []

        for entry in pqv_100_data:
            pass_pqv_data.append(entry[0])
            fail_pqv_data.append(entry[1])
            tie_pqv_data.append(entry[2])

        X_axis = X_axis = np.arange(len(pass_pqv_data))

        plt.plot(X_axis, pass_pqv_data, label="Pass")
        plt.plot(X_axis, fail_pqv_data, label="Fail")
        plt.plot(X_axis, tie_pqv_data, label="Tie")
        plt.title('Increasing Percentage PQV Voting Protocol')
        plt.xlabel('Attacker Percentage Owned')
        plt.ylabel('Percentage')
        plt.legend()
        plt.show()

# plotBasicExperiments()
# plotIncreasingPercentageExperiments(30)
plotIncreasingPercentageExperiments(100)