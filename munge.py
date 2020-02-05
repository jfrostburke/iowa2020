import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rcParams
import matplotlib as mpl
import numpy as np

fm._rebuild()   
mpl.rcParams['font.family'] = 'CMU Serif'
mpl.rcParams['font.size'] = 12
mpl.rcParams['axes.unicode_minus'] = False

data = np.genfromtxt('index_clean.csv',delimiter=',',dtype=str)

precinct_count = 0.
stayed_same = 0.
lost_people = 0.
fracs_lost = []
initials = []

for row in data[2:]:
    if row[0] == 'Total':
        continue

    initial_voters = np.sum([float(row[i]) for i in np.arange(1,41,3)])
    final_voters = np.sum([float(row[i]) for i in np.arange(2,42,3)])
    
    if initial_voters == 1.0:
        print(row[0],initial_voters)
    elif initial_voters == 837.0:
        print(row[0],initial_voters)

    initials.append(initial_voters)
    if initial_voters < final_voters:
        print("{county} fucked up".format(county=row[0]))
        continue
    elif initial_voters == final_voters:
        stayed_same += 1
    elif initial_voters > final_voters:
        lost_people += 1

    frac_lost = 100*(initial_voters - final_voters)/initial_voters
    fracs_lost.append(frac_lost)
    if frac_lost > 40:
        print(row[0],initial_voters,final_voters)
    precinct_count += 1

print(min(initials),max(initials))

plt.hist(fracs_lost,bins=20)
plt.xticks(np.arange(0,105,step=10))
plt.yscale('log')
plt.ylabel('# of precincts')
plt.xlabel('% of voters who left')
plt.title('Iowa Caucus Voter Retention')
plt.show()
plt.close()

print("Total precincts: {count}".format(count=int(precinct_count)))
print("Precincts where everyone stayed: {count} ({frac:.1f}%)".format(
    count=int(stayed_same), frac=100*stayed_same/precinct_count))
print("Precincts that lost voters: {count} ({frac:.1f}%)".format(
    count=int(lost_people), frac=100*lost_people/precinct_count))

# things to include in post
# Precincts that gained people
# Precincts that lost an unusually high percentage of people
#   Histogram of what percentage of voters precincts lost
#   What percentage of voters left?
# Smallest and largest precincts
#   And therefore SDEs/voter
# What fraction of time did person with fewer votes get most SDEs

# Also need to make a github
# And update to most recent data
#   And fix comma problems I introduced

# things to check
# no precincts where people appeared
#   whoops bad start lol
# histogram of what percentage of voters precincts lost
#   call out high losers
# what fraction of time did person with fewer votes get most SDEs
#   and who did that happen to the most
# curious about smallest and largest precincts
# better way to load data? tons of columns

