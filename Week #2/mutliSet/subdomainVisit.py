from collections import defaultdict
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        subDomains = defaultdict(int)
        result = []
        for i in cpdomains:
            info = i.split(" ")
            lenDomain = len(info[1])
            if(info[1] in subDomains):
                subDomains[info[1]] += int(info[0])
            else:
                subDomains[info[1]] = int(info[0])

            for domain in range(len(info[1])):
                if(info[1][domain] == '.'):
                    if(info[1][domain+1:lenDomain] in subDomains):
                        subDomains[info[1][domain+1:lenDomain]] += int(info[0])
                    else:
                        subDomains[info[1][domain+1:lenDomain]] = int(info[0])


        for key,value in subDomains.items():
            data = ""
            data += str(value)
            data += " "
            data += key
            result.append(data)
        return result
                
        
