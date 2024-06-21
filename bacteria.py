import numpy as np
import math

rows = ["A", "B", "C", "D", "E", "F", "G", "H"]

# class Bacteria():
#     def __init__(self, density: float):
#         self.density = density

class Well():
    def __init__(self, name: str, vol: float):
        self.name: str = name
        # self.density: float = bacteria.density ##units of bacteria/mL
        self.vol: float = vol
        self.growth: bool = False
        self.num_bacteria: int = 0
        
    
class WellPlate():
    def __init__(self, vol: float , num_wells: int = 96):
        self.wells: list = []   
        for i in range(num_wells):
            self.wells.append(Well(rows[i//12] + f"{i%8 + 1}", vol))

    def tot_bacteria(self):
        count = 0
        singles = 0
        for well in self.wells:
            if well.growth:
                count += well.num_bacteria
                if well.num_bacteria == 1:
                    singles += 1
        
        return (count, singles)

    def populate(self, num_empty):
        mean = calc_mean(num_empty)
        for well in self.wells[:96 - num_empty]:
            well.growth = True
            rand = 0
            while rand == 0:
                if mean != 0:
                    rand = np.random.poisson(mean)
                else:
                    rand = 1000
            well.num_bacteria = rand

        return self.tot_bacteria()

    def reset(self):
        for well in self.wells:
            well.growth = False
            well.num_bacteria = 0

def run_pops_single(plate: WellPlate, empty: int, num_trials: int = 100):
    lst = []
    for _ in range(num_trials):
        bacteria, singles = plate.populate(empty)
        lst.append(singles)
        plate.reset()

    lst.sort()

    return {i:lst.count(i) for i in lst}

def run_pops(plate: WellPlate, num_trials: int = 100):
    lst = []

    for i in range(97):
        tot = 0
        pops = run_pops_single(plate, 96 - i, num_trials)
        for mean, count in pops.items():
            tot += mean * count

        avg = tot/(sum(pops.values()))
        prob1 = avg/96
        prob2 = i/96 - prob1
        
        print(f"{i} wells with growth: {avg} singles, Arb. comparison: {math.exp(prob1 - prob2)}")
        lst.append(avg)

    return lst



def calc_dilutions(initial):
    lst = []
    dirt = 5 * initial

    # First in 1.5 mL solution, then 10 microliters added to 140 microliters TSB
    conc0 = dirt / 1500 * (1/15) 
    lst.append(conc0)

    for i in range(10):
        lst.append(conc0 / (10 ** (i + 1)))

    return lst

def calc_mean(val):
    if val == 0:
        result = 0   
    else:
        result = -math.log(val / 96)

    return result

