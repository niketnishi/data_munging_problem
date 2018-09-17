class CreateDataStructure:
    def __init__(self, max_index, min_index):
        self.data_lst = []
        self.min_difference_lst = []
        self.max_index = max_index
        self.min_index = min_index

    def create_structure(self, file_url):
        with open(file_url, 'r') as file_handle:
            for line in file_handle:
                temp_list = []
                for word in line.split():
                    temp_list.append(word.strip('*, .'))
                if 0 <= len(temp_list) <= 1:
                    pass
                else:
                    self.data_lst.append(temp_list)
        return self.data_lst


class MinimumTempSpread(CreateDataStructure):
    def find_minimum_index(self):
        for line in range(1, len(self.data_lst)):
            self.min_difference_lst.append(abs(float(self.data_lst[line][self.max_index]) -
                                               float(self.data_lst[line][self.min_index])))
        return self.min_difference_lst.index(min(self.min_difference_lst))

    def cal_min_temp_spread(self):
        min_temp_lst = self.create_structure('/home/dell/PycharmProjects/data_munging_problem/data/weather.dat')
        min_index = self.find_minimum_index()
        return min_temp_lst[min_index + 1][0]

    def min_goal_difference_team(self):
        goal_diff_lst = self.create_structure('/home/dell/PycharmProjects/data_munging_problem/data/football.dat')
        min_goal_index = self.find_minimum_index()
        return goal_diff_lst[min_goal_index + 1][1]


if __name__ == '__main__':
    print(MinimumTempSpread(1, 2).cal_min_temp_spread())
    print(MinimumTempSpread(6, 8).min_goal_difference_team())
