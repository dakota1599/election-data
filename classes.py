
class COLORS:
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'

class Candidate:

    def __init__(self, id, name, party, votes: int, win, od):
        self.id = id
        self.name = name
        self.party = party
        self.votes: int = votes
        self.win = win
        self.officeDescription = od

    def __str__(self):
        return "{} ({}) - {} - {} votes, Elected?: {}\n".format(self.name, self.party, self.officeDescription, self.votes, self.win)


class County:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.candidates = []

    def addCandidate(self, c: Candidate):
        self.candidates.append(c)

    def __str__(self):
        res = "\n{}\n----------\n".format(self.name)
        for c in self.candidates:
            res += c.__str__()

        return res
    
    def sort(self):
        self.candidates.sort(key=lambda x: int(x.votes), reverse=True)

    def topTwo(self, pos):
        l = [x for x in self.candidates if x.officeDescription == pos]
        l.sort
        res = "\n{}\n----------\n".format(self.name)
        if len(l) >= 2:
            lColor = ""
            rColor = ""
            total = int(l[0].votes) + int(l[1].votes)
            percentage = 0
            if int(l[0].votes) > int(l[1].votes):
                lColor = COLORS.GREEN
                rColor = COLORS.RED
                percentage = (int(l[0].votes)/total) * 100
            else:
                lColor = COLORS.RED
                rColor = COLORS.GREEN
                percentage = (float(l[1].votes)/total) * 100

            res += lColor + l[0].__str__()
            res += rColor + l[1].__str__()
            res += COLORS.WHITE + "Difference: {}\nWinner has {}% of the vote.\n".format(abs(int(l[0].votes) - int(l[1].votes)), int(percentage))
        elif len(l) == 1:
            res += COLORS.WHITE + l[0].__str__()
        else:
            res = ""
        
        res += COLORS.WHITE
        
        return res




class Election:

    def __init__(self):
        self.counties = []

    def find(self, id):
        for ct in self.counties:
            if ct.id == id:
                return ct
            
        return None
    
    def addCounty(self, county: County):
        self.counties.append(county)
    
    def __str__(self):
        res = ""

        for ct in self.counties:
            res += ct.__str__()

        return res
    
    def topTwo(self, name):
        res = ""

        for ct in self.counties:
            res += ct.topTwo(name)

        return res
    