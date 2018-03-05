import numpy as np
import matplotlib.pyplot as plt
import random


x_data = [338., 333., 328., 207., 226., 25., 179., 60., 208., 606.]
y_data = [640., 633., 619., 393., 428., 27., 193., 66., 226., 1591.]
# y_data = bias + weight * x_data



def trainSetinput(x, y):
    return x, y

def GradientDescent(x_data,y_data):
    lr = 1
    iterate = 100000
    w = random.uniform(-10, 10)
    b = random.uniform(-1, 1)
    w_history = [w]
    b_history = [b]
    lr_w = 0
    lr_b = 0
    for item in range(iterate):
        grad_w = 0
        grad_b = 0
        for i in range(len(x_data)):
            grad_b = grad_b + 2*(y_data[i]-b-w*x_data[i])*-1
            grad_w = grad_w + 2*(y_data[i]-b-w*x_data[i])*-1*x_data[i]
        lr_b = lr_b + grad_b**2
        lr_w = lr_w + grad_w**2
        b = b + lr/np.sqrt(lr_b)*grad_b
        w = w + lr/np.sqrt(lr_w)*grad_w
        w_history.append(w)
        b_history.append(b)
    return w_history,b_history


def drawplot(w_histroy, b_histroy,x_data):
    x = np.arange(-200, 100, 1)  # bias
    y = np.arange(-5, 5, 0.1)  # weight
    Z = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            w = x[i]
            b = y[j]
            Z[i][j] = 0
            for item in range(len(x_data)):
                Z[i][j] = Z[i][j] + b + (w*item)**2
            Z[i][j] = Z[i][j]/len(x_data)
    X,Y = np.meshgrid(x,y)
    plt.contourf(x,y,Z,50,alpha=0.75,cmap=plt.get_cmap("jet"))
    plt.plot([-188.4], [2.67],'x',ms=12,markeredgewidth=3,color="orange")
    plt.plot(b_histroy, w_histroy, 'o-', ms=3, lw=1.5, color='black')
    plt.xlim(-200,100)
    plt.ylim(-5,5)
    plt.xlabel(r"$b$",fontsize=16)
    plt.ylabel(r"$w$",fontsize=16)
    plt.show()


if __name__ == '__main__':
    x,y = trainSetinput(x_data, y_data)

    #define function set ,e.g. y = bias + x * weiget

    w_history,b_history = GradientDescent(x, y)

    drawplot(w_history, b_history, x)