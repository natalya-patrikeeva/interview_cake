# Write a class TempTracker
# Temperatures will all be inserted as integers. We'll record our temperatures
# in Fahrenheit, so we can assume they'll all be in the range 0..110.

# O(1) time for each function and O(1) space 
class TempTracker :

    def __init__(self):
        # min
        self.min_temp = None
        # max
        self.max_temp = None
        # mean
        self.sum = 0.0
        self.count = 0
        # mode
        self.mode_list = [0] * (111)
        self.max_occurances = 0
        self.mode = None

    def insert(self, temp) :
        '''Records a new temperature'''
        # min
        if (self.min_temp is None) or (temp < self.min_temp) :
            self.min_temp = temp

        # max
        if not self.max_temp or (temp > self.max_temp) :
            self.max_temp = temp

        # mean
        self.sum += temp
        self.count += 1

        # mode
        self.mode_list[temp] += 1
        if self.mode_list[temp] > self.max_occurances :
            self.mode = temp
            self.max_occurances = self.mode_list[temp]

    def get_max(self):
        '''Returns the highest temp we've seen so far'''
        return self.max_temp

    def get_min(self):
        '''Returns the lowest temp we've seen so far'''
        return self.min_temp

    def get_mean(self):
        '''Returns the mean of all temps we've seen so far'''
        if self.count != 0 :
            return self.sum / self.count

    def get_mode(self):
        '''Returns a mode of all temps we've seen so far'''
        return self.mode

# Test
temp_tracker = TempTracker()

temp_tracker.insert(5)
temp_tracker.insert(15)
temp_tracker.insert(5)

print(temp_tracker.get_min())
print(temp_tracker.get_max())
print(temp_tracker.get_mean())
print(temp_tracker.get_mode())
print(temp_tracker.mode)
