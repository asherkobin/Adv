from rooms import rooms

rooms['outside'].n_to = None #rooms['mine-entrance']
rooms['outside'].s_to = None
rooms['outside'].e_to = None
rooms['outside'].w_to = None
rooms['mine-entrance'].n_to = None
rooms['mine-entrance'].s_to = None
rooms['mine-entrance'].e_to = rooms['cool-room']
rooms['mine-entrance'].w_to = None
rooms['cool-room'].n_to = None
rooms['cool-room'].s_to = None
rooms['cool-room'].e_to = rooms['narrow-corridor']
rooms['cool-room'].w_to = rooms['mine-entrance']
rooms['narrow-corridor'].n_to = None
rooms['narrow-corridor'].s_to = None
rooms['narrow-corridor'].e_to = rooms['barrel-shaped-room']
rooms['narrow-corridor'].w_to = rooms['cool-room']
rooms['barrel-shaped-room'].n_to = None
rooms['barrel-shaped-room'].s_to = None
rooms['barrel-shaped-room'].e_to = None
rooms['barrel-shaped-room'].w_to = rooms['narrow-corridor']