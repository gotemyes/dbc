import pandas as pd
import random
from matplotlib import pyplot as plt
import numpy as np

def grade_comp(char1,char2,delta):
    ord1 = ord(char1.lower())
    ord2 = ord(char2.lower())

    if (ord1-ord2 >= delta) | (ord2-ord1 >= delta):
        return True
    else:
        return False

def lower_grade(char1,char2):
    ord1 = ord(char1.lower())
    ord2 = ord(char2.lower())

    if ord1>ord2:
        return chr(ord2)
    elif ord2>=ord1:
        return chr(ord1)


random.seed(0)

testDF = pd.DataFrame({
    'R_AVE':[chr(random.randint(97,100)) for el in range(10)],
    'L_AVE':[chr(random.randint(97,100)) for el in range(10)],
    'CC_AVE':[chr(random.randint(97,100)) for el in range(10)],
    'MLO_AVE':[chr(random.randint(97,100)) for el in range(10)]
})

testDF['R_L_DISCREP'] = testDF.apply(lambda row: grade_comp(row['R_AVE'],row['L_AVE'],2),axis=1)
testDF['CC_MLO_DISCREP'] = testDF.apply(lambda row: grade_comp(row['CC_AVE'],row['MLO_AVE'],2),axis=1)


testDF['R_L_MOD'] = testDF.apply(lambda row: lower_grade(row['R_AVE'],row['L_AVE']) if row['R_L_DISCREP'] else None,axis=1)
testDF['CC_MLO_MOD'] = testDF.apply(lambda row: lower_grade(row['CC_AVE'],row['MLO_AVE']) if row['CC_MLO_DISCREP'] else None,axis=1)


test_data = sorted([random.randint(1,100) for el in range(15)])

cmap = plt.get_cmap('tab20')
colors = cmap(np.linspace(0, 1.0, len(test_data)))

plt.pie(
    test_data,
    colors = colors
)

plt.pie(
    test_data_errors,
    colors = colors[1:]
)
plt.show()
