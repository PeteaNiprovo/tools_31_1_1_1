#https://stackoverflow.com/questions/1198777/double-iteration-in-list-comprehension
#https://stackoverflow.com/questions/19560044/how-to-concatenate-element-wise-two-lists-in-python
#https://stackoverflow.com/questions/4406389/if-else-in-a-list-comprehension
from functools import lru_cache
import os 
import asyncio


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
        self.listOfDirs = [] #save privious one
        self.privious = []
        self.kwargs = kwargs
    
    @lru_cache(maxsize=256)
    def createPath(self, pathdir):
        cwd = Structure.CHACHES_DIR + pathdir
        if not os.path.exists(cwd):
            print("following path doesn't exits ",Structure.CHACHES_DIR + pathdir,' attemp to create')
            os.makedirs(cwd)
    
    def _yearsTable(self):
        if 'endyear' in self.kwargs:
            return [year for year in range(self.kwargs['startyear'], self.kwargs['endyear']+1)]
        else:
            return [year for year in range(self.kwargs['startyear'], self.kwargs['startyear']+1)]
        raise BrokenPipeError("You found unhandle case")
    
    def _qatarsTable(self):
        if 'endqtr' in self.kwargs:
            #l = [self.kwargs['groupBY']] * self.kwargs['endqtr']
            #return ["{}/{}".format(qt_,ind_) for qt_, ind_ in enumerate(l, start = 1)] 
            return ["{}/{}".format(q_, self.kwargs['groupBY']) for q_ in range(1,self.kwargs['endqtr']+1)]
        else:
            print("warning endqtr are't present")
            return ["{}/{}".format(q_, self.kwargs['groupBY']) for q_ in range(1,2)]
        raise BrokenPipeError("You found unhandle case")
    #there is a clever way to do that like enumerate with 
    def createStructure(self):
        years = self._yearsTable()
        print('years = ', years)
        qartals = self._qatarsTable()
        print('qartals = ',qartals)
        #self.listOfDirs = ["{}/{}".format(a_,b_) for a_,b_ in zip(years, qartals)]
        self.listOfDirs = ["{}/{}".format(year, qartal) for year in years for qartal in qartals]
        return [self.createPath(x) for x in self.listOfDirs]

