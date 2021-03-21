'''
Author: Luke Shrimpton, Sharon Goldwater, Henry Thompson
Date: 2014-11-01, 2016-11-08
Copyright: This work is licensed under a Creative Commons
Attribution-NonCommercial 4.0 International License
(http://creativecommons.org/licenses/by-nc/4.0/): You may re-use,
redistribute, or modify this work for non-commercial purposes provided
you retain attribution to any previous author(s).
'''
fp = open("/afs/inf.ed.ac.uk/group/teaching/anlp/lab8/wid_word");
wid2word={}
word2wid={}
for line in fp:
    widstr,word=line.rstrip().split("\t")
    wid=int(widstr)
    wid2word[wid]=word
    word2wid[word]=wid
