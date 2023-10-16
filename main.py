import sys
from classes import *
def main():
    fname = sys.argv[1]
    pos = sys.argv[2]

    f = open(fname, 'r')

    election = Election()

    for line in f:
        w = line.split(',')
        county = election.findCounty(w[4])
        setCounty = False
        if (county == None):
            county = County(w[4], w[5])
            setCounty = True

        win = False
        if w[18] == "E\n" or w[18] == "N\n":
            win = True

        candidate = Candidate(w[10], w[11] + ', ' + w[12], w[8], w[15], win, w[6])

        county.addCandidate(candidate)

        if(setCounty):
            election.addCounty(county)

    f.close()
    election.setPositions()
    menu = Menu(election)

    menu.main()



if (__name__ == "__main__"):
    main()