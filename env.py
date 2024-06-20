import numpy as np

rows = ["A", "B", "C", "D", "E", "F", "G", "H"]

class Bacteria():
    def __init__(self, density: float):
        self.density = density

class Well():
    def __init__(self, name: str, bacteria: Bacteria, vol: float):
        self.name: str = name
        self.density: float = bacteria.density ##units of bacteria/mL
        self.vol: float = vol
        self.growth: bool = False
        self.num_bacteria: int = 0
    
    def has_growth(self):
        return self.growth
        
    
class WellPlate():
    def __init__(self, bacteria: Bacteria, vol: float , num_wells: int = 88):
        self.wells: list = []   
        for i in range(num_wells):
            self.wells.append(Well(rows[i//12] + f"{i%8 + 1}", bacteria, vol))

    def num_growths(self):
        count = 0
        singles = 0
        for well in self.wells:
            if well.has_growth():
                count += 1
                if well.num_bacteria == 1:
                    singles += 1
        
        return count

    def sim(self):
        rng = np.random.default_rng()
        rand = 0
            
        for well in self.wells:
            prob = well.density
            for _ in range(well.num_bacteria()):
                rand = rng.random()
                if rand < prob:
                    well.growth = True
                    break
        
        return self.num_growths()
    
    def populate(self):
        rng = np.random.poisson()
        rand = 0

        for well in self.wells:
            done = False
            prob = well.density 
            for _ in range(well.vol):
                while not done:
                    rand = rng.random()
                    if rand < prob:
                        well.growth = True
                        well.num_bacteria += 1
                    else:
                        done = True

        return self.num_growths()

    def reset(self):
        for well in self.wells:
            well.growth = False
            well.num_bacteria = 0
        
def run_sims(plate: WellPlate, prob: float, num_trials: int = 100):
    lst = []
    for _ in range(num_trials):
        lst.append(plate.sim(prob))
        plate.reset()
    lst.sort()
    
    return {i:lst.count(i) for i in lst}

def run_pops(plate: WellPlate, num_trials: int = 100):
    lst = []
    for _ in range(num_trials):
        lst.append(plate.populate())
        plate.reset()

    lst.sort()

    return {i:lst.count(i) for i in lst}

def calc_dilutions(initial):
    lst = []
    dirt = 5 * initial

    # First in 1.5 mL solution, then 10 microliters added to 140 microliters TSB
    conc0 = dirt / 1500 * (1/15) 
    lst.append(conc0)

    for i in range(10):
        lst.append(conc0 / (10 ** (i + 1)))

    return lst

    
# density = 10 ** 10 #10 ** int(input("Starting Density (Powers of 10):"))

# concs = calc_dilutions(density)

# results = []

# for conc in concs:
#     print(conc)
#     plate = WellPlate(conc, 150)
#     print(plate.wells[0].num_bacteria())
#     #print(run_sims(plate, .3, 1000))
        