from propositional_logic import PropositionalLogic
from env import Environment
from itertools import combinations 


class KnowledgeBase():
    def __init__(self):
        self._kb_sentences = dict({})

        return
    
    def update(self, percept,numofmines):
        '''
        <puclic method>  
        According to the percept, we update the self._kb_sentences in
        the konwledge.
        TODO
        '''
        print("[KB]numofmines",numofmines)
        all_flags_num = 0
        for i in range(len(percept)):
            for j in range(len(percept)):
                
                
                    
                    
                if str.isdigit(percept[i][j]) and int(percept[i][j])!=0 :
                    
                    '''check m (number of no information blocks) and flags num'''
                    m = 0
                    flags_num=0
                    
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            
                            #get m
                            if -1 < (i+k) < len(percept) and -1 < (j + l) < len(percept) and percept[i+k][j+l] == ' ':
                                m += 1
                                
                            #get flags_num
                            elif -1 < (i+k) < len(percept) and -1 < (j + l) < len(percept) and percept[i+k][j+l] == 'F':
                                flags_num+=1
                            
                                

                    
                    if((int(percept[i][j]) == flags_num) ): # f = n, all neighbors(m) have no mines
                        for k in range(-1, 2):
                            for l in range(-1, 2):
                                if -1 < (i+k) < len(percept) and -1 < (j + l) < len(percept) and percept[i+k][j+l] == ' ':

                                    self._kb_sentences[str(chr(97+j+l)+"%d"%(i+k+1))] = ['~%s%d'%((chr(97+j+l)),(i+k+1))]
                                    
                                    
                    else: #f != n 
                        if(int(percept[i][j])-flags_num == m) :# if n-f = m ,all neighbors(m) have mines(True)
                        

                            for k in range(-1, 2):
                                for l in range(-1, 2):
                                    if -1 < (i+k) < len(percept) and -1 < (j + l) < len(percept) and percept[i+k][j+l] == ' ':
                                    
                                        self._kb_sentences[str(chr(97+j+l)+"%d"%(i+k+1))] = [str(chr(97+j+l)+"%d"%(i+k+1))]
                                        #print("[KB]",self._kb_sentences.get(str(chr(97+j+l)+"%d"%(i+k+1))))
                        
                        else: #(n-f!=m C(m,n-f))
                            comblist = []
                            sentence = []
                            
                            for k in range(-1, 2):
                                for l in range(-1, 2):
                                    if -1 < (i+k) < len(percept) and -1 < (j + l) < len(percept) and percept[i+k][j+l] == ' ':
                                        comblist.append(str(chr(97+j+l)+"%d"%(i+k+1)))
                            #print("[KB],comblist",comblist)
                            comb = combinations(comblist, (int(percept[i][j])-flags_num)) 
                            comb2 = combinations(comblist,int(int(percept[i][j])-flags_num+1))
                                    
                            # create sentence for C(n,m)#
                            for q in list(comb):
                            
                                a  = str(q[0])
                                   
                                for o in range(1,len(q)):
                                    a = a+'&'+q[o]

                                sentence.append(a)

                            
                            final_sentence = str(sentence[0])
                            for r in range(1,len(sentence)):
                                
                                final_sentence = final_sentence + '|' +sentence[r]
                            
                            self._kb_sentences[str(chr(97+j)+"%d"%(i+1))] = final_sentence
                            
                            ##############################

                            # create sentence for !C(n,m+1)#
                            sentence.clear()        
                            for q in list(comb2):
 
                                b  = str(q[0])
                                    
                                for o in range(1,len(q)):
                                    b = b+'&'+q[o]

                                sentence.append(b)
                     
                            final_sentence2 = str(sentence[0])
                            for r in range(1,len(sentence)):
                                
                                final_sentence2 = final_sentence2 + '|' +sentence[r]

                            final_sentence2 = '~'+'('+final_sentence2+')'
                            self._kb_sentences[str(chr(97+j)+"%d"%(i+1))] = [self._kb_sentences.get(str(chr(97+j)+"%d"%(i+1))),final_sentence2]
                            ##############################
                            
                #  this block already have flag
                
                elif str.isalpha(percept[i][j]) :

                    self._kb_sentences[str(chr(97+j)+"%d"%(i+1))] = [str(chr(97+j)+"%d"%(i+1))]
                    all_flags_num += 1
                    print("all_flags_num",all_flags_num)
                    
        self._kb_sentences['mines_left'] = [str(numofmines - all_flags_num)]
        print("[KB_kb_snetences]",self._kb_sentences)
        return self._kb_sentences
    
    def remove(self, pl):
        del self._kb_sentences[pl]
        return
