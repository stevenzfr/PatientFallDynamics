import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import statsmodels.api as sm

print(os.getcwd())

info = pd.read_excel("Test.xlsx")
print(info)
print(info.columns)

plt.scatter(info.BodyAngles, info.HeadRotation, c=info.FallRisk)
plt.xlabel("Body Angles")
plt.ylabel("Head Rotation")
plt.xlim(0,180)
plt.ylim(0,180)
plt.show()

