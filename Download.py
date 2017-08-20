from createStructure4 import Structure
from functools import lru_cache
import asyncio
import csv
import requests
import wget

exampleOfInput = {
	"startyear":2015, "endyear":2016,
    "startqtr":1,
    "endqtr":4,
    "groupBY":"industry",
    "IND_CODE":10
}


'''
['2015/1/industry', '2015/2/industry', '2015/3/industry', '2015/4/industry', '2016/1/industry', '2016/2/industry', '2016/3/industry', '2016/4/industry', '2017/1/industry', '2017/2/industry', '2017/3/industry', '2017/4/industry', '2018/1/industry', '2018/2/industry', '2018/3/industry', '2018/4/industry', '2019/1/industry', '2019/2/industry', '2019/3/industry', '2019/4/industry']
['2016/1/industry/10.csv', '2016/1/industry/10.csv', '2016/1/industry/10.csv']
'''


class Downloader(Structure):
    def __init__(self,**kwargs):
        super(Downloader, self).__init__(**kwargs)
    
    def createStructure(self):
        super(Downloader,self).createStructure()
    
        with open(Structure.CHACHES_DIR+'/files.csv','w') as csvfile:
                backupwriter = csv.writer(csvfile, delimiter='\n')
                backupwriter.writerow(self.listOfDirs)
    
    #@asyncio.coroutine
    def _download(self, urlpath):
        filepath = urlpath[38:50]
        content = requests.get(urlpath)
        print ('filename = ',filepath,' with url ',urlpath)
        with open(filepath,'w+') as csvfile:
            csvfile.writelines(content.text)
        return filepath
    
    @asyncio.coroutine
    def _wget(self, urlpath):
        output = Structure.CHACHES_DIR + urlpath[33:48]
        print('outdir = ',urlpath)
        wget.download(urlpath, out = output, bar = wget.bar_adaptive)
        
    def pullData(self):
        links = [BLS_URL] * len (self.listOfDirs)
        links = ["{}{}/{}.csv".format(api_url, src, self.kwargs['IND_CODE']) for api_url, src in zip(links, self.listOfDirs)]
        loop = asyncio.get_event_loop()
        #tasks = [loop.run_in_executor(self._wget(link)) for link in links]
        #tasks = [self._wget(link) for link in links]        
        tasks = [asyncio.ensure_future(self._wget(link)) for link in links]
        # here we might be as parallel by no additional functionalities
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()
        
        
      
s = Downloader(**exampleOfInput)
output = s.createStructure()
s.pullData()
#print(s.listOfDirs)


