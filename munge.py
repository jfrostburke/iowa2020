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
finals = []

votes = []
SDEs = []
SDEs_per_vote = []

for row in data[2:]:
    if row[0] == 'Total':
        continue

    v = [float(row[i]) for i in np.arange(2,42,3)]
    S = [float(row[i]) for i in np.arange(3,43,3)]

    for i in range(len(v)):
        vote = v[i]
        SDE = S[i]
        #if int(vote) == 0 and int(SDE) == 0:
        if int(vote) == 0 or SDE == 0.0:
            continue
        else:
            votes.append(vote)
            SDEs.append(SDE)
            SDEs_per_vote.append(SDE/vote)

    """
    initial_voters = np.sum([float(row[i]) for i in np.arange(1,41,3)])
    final_voters = np.sum([float(row[i]) for i in np.arange(2,42,3)])
    
    initials.append(initial_voters)
    finals.append(final_voters)
    if initial_voters < final_voters:
        #print("{county} fucked up".format(county=row[0]))
        continue
    elif initial_voters == final_voters:
        stayed_same += 1
    elif initial_voters > final_voters:
        lost_people += 1

    frac_lost = 100*(initial_voters - final_voters)/initial_voters
    fracs_lost.append(frac_lost)
    #if frac_lost > 40:
    #   print(row[0],initial_voters,final_voters)
    precinct_count += 1

    if final_voters <= 3:
        print("{name}\t{init}\t{final}".format(
            name=row[0],init=initial_voters,final=final_voters))
    elif final_voters >= 800:
        print("{name}\t{init}\t{final}".format(
            name=row[0],init=initial_voters,final=final_voters))
    """

cmap = plt.cm.viridis

spv_min = np.log(min(SDEs_per_vote))
spv_max = np.log(max(SDEs_per_vote))

for i in range(len(votes)):
    spv_scaled = (np.log(SDEs_per_vote[i]) - spv_min)/(spv_max-spv_min)
    color = cmap(spv_scaled)
    plt.plot(votes[i],SDEs[i],color=color,marker='o')
plt.ylabel('SDEs')
plt.xlabel('voters')
plt.show()
plt.close()

#print(sorted(finals))

iowa_population = 3156000
#print("Total initial voters: {val} ({frac:.2f}% of Iowans".format(
#    val=np.sum(initials),
#    frac=100*np.sum(initials)/iowa_population))
#print("Total final voters: ", np.sum(finals))
#print("Total number of voters who left: {val} ({frac:.2f}%)".format(
#    val = np.sum(initials) - np.sum(finals),
#    frac = 100*(np.sum(initials)-np.sum(finals))/np.sum(initials)))

# print(min(initials),max(initials))

"""
# Histogram of precincts losing voters
plt.hist(fracs_lost,bins=20)
plt.xticks(np.arange(0,105,step=10))
plt.yscale('log')
plt.ylabel('# of precincts')
plt.xlabel('% of voters who left between 1st and 2nd rounds')
plt.title('Iowa Caucus Voter Retention')
plt.savefig('hist.png',dpi=200,bbox_inches='tight')
plt.savefig('hist.pdf',dpi=200,bbox_inches='tight')
plt.show()
plt.close()
"""

"""
print("Total precincts: {count}".format(count=int(precinct_count)))
print("Precincts where everyone stayed: {count} ({frac:.1f}%)".format(
    count=int(stayed_same), frac=100*stayed_same/precinct_count))
print("Precincts that lost voters: {count} ({frac:.1f}%)".format(
    count=int(lost_people), frac=100*lost_people/precinct_count))
"""

# things to include in post
# Precincts that gained people
# Precincts that lost an unusually high percentage of people
#   Histogram of what percentage of voters precincts lost
#   What percentage of voters left?
# Smallest and largest precincts
#   And therefore SDEs/voter
# What fraction of time did person with fewer votes get most SDEs
#   Who did this happen to most?

# And update to most recent data
#   And fix comma problems I introduced

