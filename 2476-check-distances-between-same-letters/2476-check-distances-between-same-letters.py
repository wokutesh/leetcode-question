class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        character = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 
                 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 
                 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    
        last_seen = {}
        
        for i in range(len(s)):
            if s[i] in last_seen:
               
                expected_distance = distance[character[s[i]]]
                actual_distance = i - last_seen[s[i]] - 1
                if actual_distance != expected_distance:
                    return False
            else:
                
                last_seen[s[i]] = i
        
        return True








