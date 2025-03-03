import pandas as pd
import numpy as np

# Change working directory to the location of this script
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#%% Imports and setup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class Experiment:
    def __init__(self, groups, people_per_group, throws_per_person):
        self.groups = groups
        self.people_per_group = people_per_group
        self.throws_per_person = throws_per_person
        self.results = pd.DataFrame()

    def run_experiment(self, mode='Manual'):
        data = []
        if mode == 'Template':
            # Generate random data for template mode
            for group in range(1, self.groups + 1):
                for person in range(1, self.people_per_group + 1):
                    for throw in range(1, self.throws_per_person + 1):
                        score = np.random.randint(1, 11)  # Random
                        data.append([f'Group {group}', f'Person {person}', throw, score])

        elif mode == 'Manual':
          # Manual input mode
          while True:
              name = input("Enter name (or 'Stop' to finish): ")
              if name.lower() == 'stop':
                  break
              trial = 1
              while True:
                  score = input(f"Enter score for {name} trial {trial} (or press Enter to finish): ")
                  if score == '':
                      break
                  # Check if the input is numeric before converting to int
                  if score.isdigit():  
                      data.append([name, trial, int(score)])
                  else:
                      print("Invalid input. Please enter a numeric score.")
                  trial += 1
        else:
            print("No data entered.")
            self.results = pd.DataFrame()
            return

        self.results = pd.DataFrame(data, columns=['Name', 'Trial', 'Score'])

    def save_results(self, filename):
        self.results.to_csv(filename, index=False)

#%% Input data manually
number_of_groups = 3
number_of_people_per_group = 5
number_of_throws_per_person = 10
group_name = 'NoName'

#%% Create an instance of the Experiment class
experiment = Experiment(groups=3, people_per_group=5, throws_per_person=10)
experiment.run_experiment(mode='Template') # Change to 'Template' to generate random data
experiment.save_results(f'results_{group_name}.csv')
experiment.results.head()




#%% END