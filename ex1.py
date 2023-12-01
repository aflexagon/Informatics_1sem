import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/diamonds.csv')
x1 = df.loc[df.cut=='Ideal', ['depth']]
x2 = df.loc[df.cut=='Fair', ['depth']]
x3 = df.loc[df.cut=='Good', ['depth']]

# plot
fig, axes = plt.subplots(1, 3, figsize=(10, 3), sharey=True, dpi=100)
sns.distplot(x1 , color="dodgerblue", ax=axes[0], axlabel='Ideal')
sns.distplot(x2 , color="deeppink", ax=axes[1], axlabel='Fair')
sns.distplot(x3 , color="gold", ax=axes[2], axlabel='Good')
plt.xlim(50,75);