import numpy as np


class UCB():
    """Implements a random policy."""

    def __init__(self, nbArms):
        #    self.arms = arms
        self.nbArms = nbArms
        #    self.budgets = np.asarray([arm.budget for arm in arms])
        self.nbpulls = np.zeros(nbArms)
        self.rewards = np.zeros(nbArms)
        self.t = -1
        self.params = ''

    def startGame(self):
        #    self.budgets = np.asarray([arm.budget for arm in self.arms])
        self.nbpulls = np.zeros(self.nbArms)
        self.rewards = np.zeros(self.nbArms)
        self.t = -1
        self.init = True

    def choice(self):
        self.t += 1
        if (self.t < self.nbArms):
            arm = self.t%self.nbArms
            self.nbpulls[arm] += 1
            return arm
        #print self.rewards, self.nbpulls, self.t
        arm = np.argmax(self.rewards/self.nbpulls + np.sqrt((2*np.log(self.t))/self.nbpulls))
        self.nbpulls[arm] += 1
        return arm

    def getReward(self, arm, reward):
        self.rewards[arm] += reward

    def __str__(self):
        return "UCB"
