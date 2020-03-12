import matplotlib.pyplot as plt
import numpy as np

figWidth = 20
figHeight = 15
resolution = 70

plt.figure(figsize=(figWidth, figHeight), dpi=resolution)

pokedata = np.genfromtxt(
    "pokemon.csv", names=True,
    dtype="float", delimiter=",")
plt.xlabel('Pokemon HP')
plt.ylabel('Pokemon Attack')
plt.plot(pokedata["HP"], pokedata["Attack"], "go")
plt.savefig("out.png")
