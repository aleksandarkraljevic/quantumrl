from dqn import *

# name that will be used to save both the model and all its data with
savename = 'experiment'
# amount of repetitions that will be averaged over for the experiment
repetitions = 20
# game parameters
n_holes = 5
memory_size = 2*n_holes
# model parameters
n_nodes = 12
# Hyperparameters of the algorithm and other parameters of the program
learning_rate = 0.01
gamma = 1  # discount factor
initial_exploration = 1  # 100%
final_exploration = 0.01  # 1%
num_episodes = 5000
tau = 0.1
decay_constant = 0.01  # the amount with which the exploration parameter changes after each episode
temperature = 0.1
batch_size = 32
min_size_buffer = 1000
max_size_buffer = 10000
exploration_strategy = 'anneal_epsilon_greedy'
#exploration_strategy = 'boltzmann'

data_names = []

start = time.time()

for rep in range(repetitions):
    classical_model = ClassicalModel(n_holes=n_holes, memory_size=memory_size, n_nodes=n_nodes,
                                     learning_rate=learning_rate)
    base_model = classical_model.initialize_model()
    target_network = classical_model.initialize_model()

    file_name = savename + str(rep)

    dqn = DQN(file_name, base_model, target_network, n_holes, memory_size, learning_rate, gamma, num_episodes, tau, initial_exploration, final_exploration, decay_constant, temperature, batch_size, min_size_buffer, max_size_buffer, exploration_strategy)

    dqn.main()

    data_names.append(file_name)

end = time.time()
print('Total time: {} seconds'.format(round(end - start, 1)))

plot_averaged(data_names=data_names, show=True, savename=savename)
#plot_averaged(data_names=data_names, show=True, savename=savename+'_smooth')