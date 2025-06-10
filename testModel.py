from database.DAO import DAO
from model.model import Model

m = Model()
m.creaGrafo(2017, 1, 0.6)
print(m.getNum())
print(m.getRedditizi())