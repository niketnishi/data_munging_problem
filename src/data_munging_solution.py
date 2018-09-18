class CreateDataStructure:
    def __init__(self,out_index, max_index, min_index, data_url):
        self.data_lst = []
        self.min_difference_lst = []
        self.output_index = out_index
        self.max_index = max_index
        self.min_index = min_index
        self.url = data_url

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


class ComputeOutput(CreateDataStructure):
    def find_minimum_index(self):
        for line in range(1, len(self.data_lst)):
            self.min_difference_lst.append(abs(float(self.data_lst[line][self.max_index]) -
                                               float(self.data_lst[line][self.min_index])))
        return self.min_difference_lst.index(min(self.min_difference_lst))

    def compute_output(self):
        min_diff_lst = self.create_structure(self.url)
        min_index = self.find_minimum_index()
        return min_diff_lst[min_index + 1][self.output_index]


if __name__ == '__main__':
    print(ComputeOutput(0, 1, 2, '/home/dell/PycharmProjects/data_munging_problem/data/weather.dat').compute_output())
    print(ComputeOutput(1, 6, 8, '/home/dell/PycharmProjects/data_munging_problem/data/football.dat').compute_output())
