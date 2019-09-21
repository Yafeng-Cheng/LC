# 1160. Find Words That Can Be Formed by Characters

# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character can only be used once).

# Return the sum of lengths of all good strings in words.

# Example 1:

# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: 
# The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.


# Example 2:

# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: 
# The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

# Note:

# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# All strings contain lowercase English letters only.


words = ["cat","bt","hat","tree"]
chars = "atach"

# words = ["hello","world","leetcode"]
# chars = "welldonehoneyr"


# words = ["dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin","ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb","ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl","boygirdlggnh","xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx","nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop","hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx","juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr","lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo","oxgaskztzroxuntiwlfyufddl","tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp","qnagrpfzlyrouolqquytwnwnsqnmuzphne","eeilfdaookieawrrbvtnqfzcricvhpiv","sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz","yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue","hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv","cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo","teyygdmmyadppuopvqdodaczob","qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs","qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"]
# chars = "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp"

class Solution:
    def count_to_dict(self, vec):
        """
        turn vec into a dictionary and count each of the items
        
        Arg:
        ----
        vec: string
        
        Return:
        ----
        a dict
        """
        out = {}
        for i in vec:
            out[i] = out.get(i,0)+1
        return out
    
    def countCharacters(self, words, chars):
        """
        create count dict for chars and each word;
        compare the keys and values to contine or stop
        
        Arg:
        ----
        words: list of string
        chars: string
        
        Return:
        ----
        sum of the good strings. int
        """
        chars_dict = self.count_to_dict(chars)
        chars_set = chars_dict.keys()
        len_chars_set = len(chars_set)
        
        good_string = ''
        for words_i in words:
            word_dict = self.count_to_dict(words_i)
            words_i_set = word_dict.keys()
            check = 0
            for i in words_i_set:
                if i not in chars_set:
                    check+=1
                    break
                if word_dict[i] > chars_dict[i]:
                    check+=1
                    break
            if check == 1:
                continue
            good_string = good_string+words_i
        return len(good_string)
    
Solution().countCharacters(words, chars)

