class Solution(object):
    def gcdOfStrings(self, str1, str2):
        s1=str1+str2
        s2=str2+str1

        if s1!=s2:
            return ""
        if len(str1)==len(str2):
            return str1
        if len(str1)>len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        
        return self.gcdOfStrings(str2[len(str1):],str1)  