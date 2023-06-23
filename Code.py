#%%
import numpy as np

#%%
PLAYGROUND_SIZE = (20,20)
# PLAYGROUND = np.random.random(PLAYGROUND_SIZE)
PLAYGROUND = np.random.randint(0, 2, size=PLAYGROUND_SIZE)
print(PLAYGROUND) #window of game

# for _ in range(PLAYGROUND_SIZE[0] * 3) :


from scipy.signal import convolve2d


def die_or_alive_codex(playground = PLAYGROUND):
    # print(convolve2d(playground,np.ones((3,3),dtype=int),'same') - playground) #test
    # print(playground) #test
    sum_matrix = convolve2d(playground,np.ones((3,3),dtype=int),'same') - playground
    for x in range(PLAYGROUND_SIZE[0]):
        for y in range(PLAYGROUND_SIZE[1]):
            # print(playground[x,y]) #test
            if playground[x,y] >= 1: # bit is live
                if sum_matrix[x,y] >= 2 and sum_matrix[x,y] <= 3: #classic rules of game (can be modificate)
                    playground[x,y] = 1 # bit is most be live
                else:
                    playground[x,y] = 0 #bit is dead
            else: # bit is dead
                if sum_matrix[x,y] == 3 :
                    playground[x,y] = 1
                else:
                    playground[x,y] = 0
    print('\n\n\n')
    print(playground)

die_or_alive_codex()

#%%
import time

while True:

    input() # for hand control of cycles
    time.sleep(0.2) # for auto control 

    die_or_alive_codex()
