
import numpy as np


# static shapes, 

Box = np.ones((2,2), dtype=np.uint8)

Eater1 =  np.array([[1, 1, 0, 0],
                    [1, 0, 1, 0], 
                    [0, 0, 1, 0], 
                    [0, 0, 1, 1]], dtype=np.uint8)

Eater2 =  np.array([[0, 1, 0, 1, 0, 0],
                    [1, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 0],
                    [0, 0, 0, 1, 1, 1],], dtype=np.uint8)

Kite =    np.array([[1, 1, 0], 
                    [1, 0, 1],
                    [0, 1, 0]], dtype=np.uint8)

Moon =    np.array([[0, 1, 1, 0], 
                    [1, 0, 0, 1], 
                    [0, 1, 0, 1], 
                    [0, 0, 1, 0]], dtype=np.uint8)

Seed =    np.array([[0, 1, 1, 0], 
                    [1, 0, 0, 1],
                    [0, 1, 1, 0]], dtype=np.uint8)

# gliders

Glider =  np.array([[1, 0, 0], 
                    [0, 1, 1], 
                    [1, 1, 0]], dtype=np.uint8)

LightweightSpaceship =    np.array([[0, 1, 0, 0, 1], 
                                    [1, 0, 0, 0, 0],
                                    [1, 0, 0, 0, 1],
                                    [1, 1, 1, 1, 0],], dtype=np.uint8)

MiddleweightSpaceship =   np.array([[0, 0, 0, 1, 0, 0], 
                                    [0, 1, 0, 0, 0, 1],
                                    [1, 0, 0, 0, 0, 0],
                                    [1, 0, 0, 0, 0, 1],
                                    [1, 1, 1, 1, 1, 0],], dtype=np.uint8)

# grower

Unbounded =   np.array([[1, 1, 1, 0, 1], 
                        [1, 0, 0, 0, 0],
                        [0, 0, 0, 1, 1],
                        [0, 1, 1, 0, 1],
                        [1, 0, 1, 0, 1],], dtype=np.uint8)

# methuselahs

Century = np.array([[0, 0, 1, 1], 
                    [1, 1, 1, 0],
                    [0, 1, 0, 0]], dtype=np.uint8) 

Thunderbird = np.array([[1, 1, 1], 
                        [0, 0, 0],
                        [0, 1, 0],
                        [0, 1, 0],
                        [0, 1, 0]], dtype=np.uint8)

# oscilators

Beacon =  np.array([[1, 1, 0, 0],
                    [1, 1, 0, 0],
                    [0, 0, 1, 1],
                    [0, 0, 1, 1]], dtype=np.uint8)

Blinker = np.array([[0, 1, 0],
                    [0, 1, 0],
                    [0, 1, 0]], dtype=np.uint8)

Chacha =  np.array([[0, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 1, 0, 1, 0, 1, 0],
                    [1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1],
                    [0, 1, 0, 1, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0]], dtype=np.uint8)

Eight =   np.array([[1, 1, 1, 0, 0, 0],
                    [1, 1, 1, 0, 0, 0],
                    [1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 1, 1, 1]], dtype=np.uint8)

Pentadecathlon =  np.array([[1, 1, 1],
                            [1, 0, 1],
                            [1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1],
                            [1, 0, 1],
                            [1, 1, 1]], dtype=np.uint8)

Pulsar =  np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.uint8)

Toad =    np.array([[0, 0, 0, 0],
                    [1, 1, 1, 0],
                    [0, 1, 1, 1],
                    [0, 0, 0, 0]], dtype=np.uint8)

allShapes = {
        "Box": Box, 
        "Eater1": Eater1, 
        "Eater2": Eater2, 
        "Kite": Kite, 
        "Moon": Moon, 
        "Seed": Seed, 
        "Glider": Glider, 
        "LightweightSpaceship": LightweightSpaceship, 
        "MiddleweightSpaceship": MiddleweightSpaceship, 
        "Unbounded": Unbounded,
        "Century": Century,
        "Thunderbird": Thunderbird,
        "Beacon": Beacon,
        "Blinker": Blinker,
        "Chacha": Chacha,
        "Eight": Eight,
        "Pentadecathlon": Pentadecathlon,
        "Pulsar": Pulsar,
        "Toad": Toad,
}
