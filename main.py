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
        position = election.findPosition(w[6])
        setCounty = False
        setPosition = False
        if (county == None):
            county = County(w[4], w[5])
            setCounty = True

        if (position == None):
            position = Position(w[6])
            setPosition = True

        win = False
        if w[18] == "E\n" or w[18] == "N\n":
            win = True

        candidate = Candidate(w[10], w[11] + ', ' + w[12], w[8], w[15], win, w[6])

        county.addCandidate(candidate)

        posCandidate = position.getCandidate(candidate.name)
        if (posCandidate == None):
            position.addCandidate(candidate)
        else:
            v = int(posCandidate.votes) + int(candidate.votes)
            posCandidate.votes = v

        if(setCounty):
            election.addCounty(county)

        if (setPosition):
            election.addPosition(position)

    f.close()
    menu = Menu(election)

    menu.main()



if (__name__ == "__main__"):
    main()