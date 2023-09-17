
import matplotlib.pyplot as plt




def vytvoreni_grafu():
    # Data pro osu x a osu y
    x = [1, 2, 3, 4, 5]
    y = [10, 16, 5, 8, 9]

    # Vytvoření grafu
    plt.plot(x, y)

    # Zobrazení grafu
    plt.show()




def pojmenovani_xy():
    # Data pro osu x a osu y
    x = [1, 2, 3, 4, 5]
    y = [10, 16, 5, 8, 9]

    # Vytvoření grafu
    plt.plot(x, y)

    #Pojmenování x a y
    plt.xlabel("Kategorie")
    plt.ylabel("hodnota")
    plt.title("Hodnoty v kateregoriich")

    # Zobrazení grafu
    plt.show()





def ulozeni_grafu():
    x = [1, 2, 3, 4, 5]
    y = [10, 16, 5, 8, 9]

    plt.plot(x, y)

    plt.savefig("graf.png")

    # Zobrazení grafu
    plt.show()
   



def kolacovi_graf():
    # Data pro koláčový graf
    labels = ['A', 'B', 'C', 'D']
    sizes = [15, 30, 45, 10]

    # Vytvoření koláčového grafu
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')

    plt.title('Podíl jednotlivých kategorií')

    plt.show()    




def histogram():

    import numpy as np

    # Vygenerování náhodných dat
    data = np.random.randn(1000)

    # Vytvoření histogramu s 20 sloupci
    plt.hist(data, bins=20)


    plt.xlabel('Hodnoty')
    plt.ylabel('Četnost')
    plt.title('Histogram náhodných dat')


    plt.show()


def bodovy_graf():

    x = [1, 2, 3, 4, 5]
    y = [10, 16, 5, 8, 9]

    # Vytvoření bodového grafu
    plt.scatter(x, y)


    plt.xlabel('X osa')
    plt.ylabel('Y osa')
    plt.title('Bodový graf')


    plt.show()    


bodovy_graf()