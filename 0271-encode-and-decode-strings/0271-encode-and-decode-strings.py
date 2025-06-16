class Codec:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return strs
        new_str=''
        for i in range(len(strs)):
            new_str+= str(len(strs[i])) + '#' + strs[i]  
        
        return new_str


        

        


        """Encodes a list of strings to a single string.
        """
        

    def decode(self, s: str) -> List[str]:
        if not s:
            return s
        
        dec_str=[]

        i=0
        while i<len(s):
            j=i

            while s[j]!='#':
                j+=1

            n=int(s[i:j])
            j+=1

            dec_str.append(s[j:j+n])

            i=j+n

        return dec_str
        """Decodes a single string to a list of strings.
        """
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))