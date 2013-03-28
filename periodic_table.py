from nucleus import *
import operator

def sumproduct(*lists):
  return sum(reduce(operator.mul, data) for data in zip(*lists))

#atomic number = protons
#ex. ag - 47, 60;62

class chemical_element:
  def __init__(self, name="", symbol="", category="", 
      atomic_weight=0, protons_num=0, neutrons_num=[],
      stable_with=[]):

    self.name = name
    self.symbol = symbol
    self.category = category
    self.atomic_weight = atomic_weight
    self.protons_num = protons_num
    self.neutrons_num = neutrons_num
    self.stable_with = stable_with

    sumproduct(neutrons_num, stable_with)

  def relative_atomic_mass(self): 
    pass

# list of few chemical elements for testing
Ag = chemical_element('Silver','Ag','transition metal',
    107.868, 47, [60,62], [0.51839, 0.48161])
P  = chemical_element('Phosphorus','P','nonmetal',
    30.973, 15, [16],[1.0])
