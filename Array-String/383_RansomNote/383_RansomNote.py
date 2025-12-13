from typing import List


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        First, the algorithm utilizes the Counter library to create frequency maps for both the ransomNote and magazine
        strings, counting exactly how many times each character appears. These Counter objects function as hash maps
        where keys are the characters and values represent their respective counts. Although the code includes print
        statements to visually verify the contents of these maps, the core logic lies in the final comparison.
        The return statement uses the less-than-or-equal operator (<=) to check if the ransomNote's character counts
        are a subset of the magazine's counts. This efficiently determines True only if the magazine possesses enough
        of every specific character required to construct the note.
        '''
        # ranHash = Counter(ransomNote)
        # magHash = Counter(magazine)
        # print(ranHash)
        # print(magHash)


        '''
        This approach manually constructs frequency maps for both strings using standard Python dictionaries, 
        utilizing the .get() method to safely handle initial character counting. It iterates through the ransomNote 
        and magazine strings character by character to populate these hash maps with their respective frequencies. 
        After populating the maps, the algorithm loops specifically through the unique keys of the ransomNote dictionary 
        to verify if the requirements can be met. Inside this loop, it compares the required count against the available 
        count in the magazine map, returning False immediately if the magazine has insufficient characters (or none at all). 
        Finally, if the loop completes without encountering any deficits, the function returns True to indicate success.
        '''
        ranHash = {}
        magHash = {}

        for char in ransomNote:
            ranHash[char] = ranHash.get(char, 0) + 1

        for char in magazine:
            magHash[char] = magHash.get(char, 0) + 1
        print(ranHash)
        print(magHash)

        for key in ranHash:
            print(ranHash[key])
            if ranHash[key] > magHash.get(key, 0):
                return False

        return True


sol = Solution()

print(sol.canConstruct(ransomNote="a", magazine="b"))

print(sol.canConstruct(ransomNote="aa", magazine="ab"))

print(sol.canConstruct(ransomNote="aa", magazine="aab"))
