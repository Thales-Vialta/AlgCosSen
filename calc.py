import numpy as np
import matplotlib.pyplot as plt

def entrada(): 
    n1 = float(input("Digite o valor de A: "))
    n2 = float(input("Digite o valor de B: "))
    n3 = float(input("Digite o valor de C: "))
    n4 = float(input("Digite o valor de D: "))
    while True: 
        trig = input("Qual função seria? Seno ou Cosseno: ")
        if trig not in ["Seno", "Cosseno"]:
            continue
        else: 
            break
    return n1,n2,n3,n4,trig

def func(trig,n1,n2,n3,n4,x): 
    if trig == "Seno": 
        funcY = n1 * np.sin(n2*x + n3) + n4
        return funcY
    elif trig == "Cosseno": 
        funcY = n1 * np.cos(n2*x + n3) + n4
        return funcY    

def grafico(x,y,trig,n1,n2,n3,n4): 
    plt.plot(x, y, label=f"{trig} com A={n1}, B={n2}, C={n3}, D={n4}")
    plt.legend()
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Gráfico de função Seno-Cosseno")
    plt.grid(True)
    plt.show()

def main():
    n1, n2, n3, n4, trig = entrada()
    x = np.linspace(-5, 5, 400)
    y = func(trig, n1, n2, n3, n4, x)
    grafico(x, y, trig, n1, n2, n3, n4)

if __name__ == "__main__":
    main()