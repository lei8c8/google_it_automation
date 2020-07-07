class Solution:
    def reverseVowels(self, s):
        s_list = list(s)
        lookup = 'aeiou'
        left, right = 0, len(s_list) - 1
        while left < right:
            while (s_list[left].lower() not in lookup) and (left < right):
                left += 1
            while (s_list[right].lower() not in lookup) and (left < right):
                right -= 1
            print("left = {}, right = {}".format(left, right))
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        return ''.join(s_list)
        
if __name__ == '__main__':
    s = Solution()
    result = s.reverseVowels("leetcode")
    print(result)