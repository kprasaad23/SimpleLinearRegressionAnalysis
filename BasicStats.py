class BasicStats:

    def __init__(self, x_values, y_values):
        self.x_values = x_values
        self.y_values = y_values

    def mean(self, list_of_values): #calculate mean of the list of values given
        return sum(list_of_values) / float(len(list_of_values))

    def variance(self, list_of_values): #calculate variance of the list of values given
        return sum([(i - self.mean(list_of_values))**2 for i in list_of_values])

    def covariance(self): #covariance calculation
        cov = 0.0
        for i in range(len(self.x_values)):
            cov += (self.x_values[i] - self.mean(self.x_values)) * (self.y_values[i] - self.mean(self.y_values))
        return cov

