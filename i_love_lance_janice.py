"""
I Love Lance & Janice
=====================
You've caught two of your fellow minions passing coded notes back and forth - while they're on duty, no less! Worse, you're pretty sure it's not job-related - they're both huge fans of the space soap opera "Lance & Janice". You know how much Commander Lambda hates waste, so if you can prove that these minions are wasting her time passing non-job-related notes, it'll put you that much closer to a promotion.
Fortunately for you, the minions aren't exactly advanced cryptographers. In their code, every lowercase letter [a..z] is replaced with the corresponding one in [z..a], while every other character (including uppercase letters and punctuation) is left untouched.  That is, 'a' becomes 'z', 'b' becomes 'y', 'c' becomes 'x', etc.  For instance, the word "vmxibkgrlm", when decoded, would become "encryption".
Write a function called answer(s) which takes in a string and returns the deciphered string so you can show the commander proof that these minions are talking about "Lance & Janice" instead of doing their jobs.
Languages
=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java
Test cases
==========
Inputs:
    (string) s = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
Output:
    (string) "did you see last night's episode?"
Inputs:
    (string) s = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
Output:
    (string) "Yeah! I can't believe Lance lost his job at the colony!!"
"""

def strSlice(s):
    str_lst = []

    for i in range(len(s)):
        sliced_str = s[0:i+1]
        str_lst.append(sliced_str)

    return str_lst


def answer(s):

    str_lst = strSlice(s)
    str_len_lst = []

    for elmt in str_lst:
        cnt_elmt = s.count(elmt)
        quotient = len(s)/len(elmt)
        if (elmt * quotient) == s:
            str_len_lst.append(cnt_elmt)

    return max(str_len_lst)

# s = "abccbaabccba"
# 2

s = "abcabcabcabc"
# 4

print answer(s)
