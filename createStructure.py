#https://stackoverflow.com/questions/19560044/how-to-concatenate-element-wise-two-lists-in-python
#https://stackoverflow.com/questions/4406389/if-else-in-a-list-comprehension
from functools import lru_cache
import os 
exampleOfInput = {
	"startyear":2015, "endyear":2017,
    "startqtr":1,
    "endqtr":4,
    "groupBY":"industry",
    "IND_CODE":4
}
'''
1) 2015/1/industry/
2) 2015/2/industry/
3) 2015/3/industry/
4) 2015/4/industry/
example of real url 
2016/2/industry/10.csv
2016/1/industry/10.csv
'''

'''Following class should is used to create directory for files'''
    
class Structure:
    CHACHES_DIR = 'CHACHES/'
    def __init__(self,**kwargs):
        self.listOfDirs = []
        self.kwargs = kwargs
    
    @lru_cache(maxsize=256)
    def createPath(self, pathdir):
        cwd = Structure.CHACHES_DIR + pathdir
        if not os.path.exists(cwd):
            print("following path doesn't exits ",Structure.CHACHES_DIR + pathdir,' attemp to create')
            os.makedirs(cwd)
    
    def _yearsTable(self):
        if 'endyear' in exampleOfInput:
            return [year for year in range(exampleOfInput['startyear'], exampleOfInput['endyear']+1)]
        else:
            return [year for year in range(exampleOfInput['startyear'], exampleOfInput['startyear']+1)]
        raise BrokenPipeError("You found unhandle case")
    
    def _qatarsTable(self):
        if 'endqtr' in exampleOfInput:
            return ["{}/{}".format(q_, exampleOfInput['groupBY']) for q_ in range(1,exampleOfInput['endqtr'])]
        else:
            return ["{}/{}".format(q_, exampleOfInput['groupBY']) for q_ in range(1,2)]
        raise BrokenPipeError("You found unhandle case")
    
    
    def createStructure(self):
        years = self._yearsTable()
        qartals = self._qatarsTable()
        dirs = ["{}/{}".format(a_,b_) for a_,b_ in zip(years, qartals)]
        return [self.createPath(x) for x in dirs]
    
s = Structure(**exampleOfInput)
output = s.createStructure()
 
