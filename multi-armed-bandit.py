""" Multi armed bandit algorithm"""
import numpy as np
import matplotlib.pyplot as plt

class bandit:
    def __init__(self, m):
        self.m = m
        self. N = 0
        self.mean = 0
    def reset(self):
        self.N = 0
        self.mean = 0

    def pull(self):
        return np.random.randn() + self.m

    def update(self, X):
        self.N += 1
        self.mean = (1-(1/self.N)) * self.mean + ((1 / self.N) * X)

def n_armed_bandit(n, iterations, epsilon_greedy = True, UCB = False, epsilon = .1):

    # generate random n bandits
    bandits = {}
    means = []
    for b in range(n):
        np.random.seed(10)
        m_rand = np.random.randint(0,10)
        means.append(m_rand)
        bandits["bandit{}".format(b)] = bandit(m_rand)

    bandits = list(bandits.values())

    plot_data = []
    # begin iterations
    for i in range(iterations):

        if epsilon_greedy == True:
            # epsilon greedy
            p = np.random.random()
            if p < epsilon:
                j = np.random.choice(n)
            else:
                j = np.argmax([b.mean for b in bandits])

        if UCB == True:

            j = np.argmax([(b.mean + np.sqrt(2 * (np.log(iterations) / (b.N+.0000001)))) for b in bandits])

        X = bandits[j].pull()
        bandits[j].update(X)
        plot_data.append(X)

    cum_av = np.cumsum(plot_data) / np.arange(iterations) + 1

    real_mean = np.max(means)

    return real_mean, cum_av

def test_epsilon():
    eps = np.linspace(0,1,11)

    for e in eps:
        cum_av = n_armed_bandit(10,100,e, epsilon=False, UCB = True)[1]
        plt.plot(cum_av)
    plt.show()

def test_ucb_epsilon():
    plt.plot(n_armed_bandit(100,100,epsilon = .1)[1])
    plt.plot(n_armed_bandit(100,100,epsilon=False, UCB=True)[1])
    plt.show()

test_ucb_epsilon()

