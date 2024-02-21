import numpy as np

def ler_arquivo_data(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        dados = arquivo.readlines()
    return dados

nome_arquivo = "iris.data"
dados = ler_arquivo_data(nome_arquivo)

featureOne:list[float] = np.array([])
featureTwo:list[float] = np.array([])
featureThree:list[float] = np.array([])
featureFour:list[float] = np.array([])
featureFive:list[str] = []

for linha in dados:
    linhSplited:list[str] = linha.split(",")

    featureOne = np.append(featureOne, float(linhSplited[0]))
    featureTwo = np.append(featureTwo, float(linhSplited[1]))
    featureThree = np.append(featureThree, float(linhSplited[2]))
    featureFour = np.append(featureFour, float(linhSplited[3]))
    featureFive.append(linhSplited[4])


print(featureOne)
print(featureTwo)
print(featureThree)
print(featureFour)

deviation_pattern_featureOne:float = np.std(featureOne)
deviation_pattern_featureTwo:float = np.std(featureTwo)
deviation_pattern_featureThree:float = np.std(featureThree)
deviation_pattern_featureFour:float = np.std(featureFour)

average_featureOne:float = np.mean(featureOne)
average_featureTwo:float = np.mean(featureTwo)
average_featureThree:float = np.mean(featureThree)
average_featureFour:float = np.mean(featureFour)

def aplyZScore(featureOne, featureTwo, featureThree, featureFour):


    print(featureOne)

    with(open("zscore.data", "w")) as zscoreFile:

        for index in range(len(featureFive)):
            z_score_featureOne:float = (featureOne[index] - average_featureOne) / deviation_pattern_featureOne
            z_score_featureTwo:float = (featureTwo[index] - average_featureTwo) / deviation_pattern_featureTwo
            z_score_featureThree:float = (featureThree[index] - average_featureThree) / deviation_pattern_featureThree
            z_score_featureFour:float = (featureFour[index] - average_featureFour) / deviation_pattern_featureFour
            zscoreFile.write(f"{z_score_featureOne:.2f},{z_score_featureTwo:.2f},{z_score_featureThree:.2f},{z_score_featureFour:.2f},{featureFive[index]}")


aplyZScore(featureOne, featureTwo, featureThree, featureFour)