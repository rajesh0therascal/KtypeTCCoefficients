import numpy as np

maxTemp = 600
startVolt = 0.5
endVolt = 9.5


def preProcess(fileName):
    Kdat = []
    with open(fileName) as f:
        for line in f:
            nLine = line.rstrip()
            strLine = list(nLine.split('\t'))
            Kdat = Kdat + strLine

    return Kdat


def scmTF(data):
    scmData = []
    coEff = 1 / float(data[maxTemp])
    for point in data:
        numPoint = float(point)
        voltage = 9 * numPoint * coEff + 0.5
        scmData.append(voltage)
    return scmData


def makeMatrix(transferFunc):
    iniArray = np.zeros(shape=(maxTemp+1, 3))
    for i in range(maxTemp+1):
        iniArray[i] = [transferFunc[i] * transferFunc[i], transferFunc[i], 1]

    return iniArray

def makeTemp():
    iniArray = np.zeros(shape= (maxTemp+1, 1))
    for i in range(maxTemp+1):
        iniArray[i] = [i]

    return iniArray

def findCoffs(matArray):
    print("Shape of Input Matrix:", np.shape(matArray))
    matArrayTranspose = np.transpose(matArray)
    print("Shape of Input Matrix Transpose:", np.shape(matArrayTranspose))
    matMult1 = np.dot(matArrayTranspose, matArray)
    print("Shape of Multiplied Trans(A) * A:", np.shape(matMult1))
    matMult1Inv = np.linalg.inv(matMult1)
    print("Shape of Inverse",np.shape(matMult1Inv))
    matMult2 = np.dot(matMult1Inv, matArrayTranspose)
    print("Shape of Pseudo Inverse", np.shape(matMult2))
    print("Shape Temp Matrix:", np.shape(makeTemp()))
    print(makeTemp())
    coEffs = np.dot(matMult2, makeTemp())
    print(np.shape(coEffs))
    print(coEffs)




if __name__ == "__main__":
    listTdata = preProcess("K.txt")
    scmOut = scmTF(listTdata)
    matrixIni = makeMatrix(scmOut)
    findCoffs(matrixIni)
