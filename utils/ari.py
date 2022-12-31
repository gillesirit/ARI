def Val(i,sample_set): #i is an attribute and we look for the set of values it can take X_i
    val = sample_set[:,i].tolist() #return a list of list  
    #print('i={} val={} size of val={}'.format(i, val, len(set(val))))
    return len(set(val))
    
#Dag is never empty because a is always distinct from b
def Dag(a,b,list_of_attributes):  #disagreement set between Boolean vectors of same dimension
    dis=[]
    for i in list_of_attributes:
        if a[i] != b[i]:  #this is where we test the equality of attribute value
            dis.append(i)
            
    #print('a={} b={} dag={}'.format(a, b, dis))    
    return  dis

def Dif(dim,attribute,list_of_attributes,set_of_pairs): #set_of_pairs = a list containing pairs of (a,b)    
    ag_att=0 # number of pairs such that: Dag={attribute} |Dif(i)s
    m_att=0  # number of pairs such that: Dag={attribute} with different label |Dif(i)s - Dif_Eq(i)s
    for (a,b) in set_of_pairs: 
        
        if Dag(a[0:dim],b[0:dim],list_of_attributes)==[attribute]: # differ only on 1            
            #print('a={} b={} attribute={}'.format(a, b, [attribute]))            
            ag_att+=1  
            if a[dim]!=b[dim]:  #this is where we test equality of label
                #print('differ')
                m_att+=1
    #print("\n")            
    return ag_att, m_att # ARI = m_att/ag_att

def ari(dim,attribute,list_of_attributes,sample_set,set_of_pairs):
    if Val(attribute,sample_set)==1: #zero-variance
        return 0
    ag_att, m_att = Dif(dim,attribute,list_of_attributes,set_of_pairs) 
    #print('{} ag_att(diff)={} m_att(diff_noteq)={}'.format(attribute, ag_att, m_att))            
    if ag_att==0:   #redundancy
        return 2
    return m_att/ag_att
        
def select_features_ars(dim,list_of_attributes,sample_set,set_of_pairs):
    scores=[]
    for attribute in list_of_attributes:
        ratio=ari(dim,attribute,list_of_attributes,sample_set,set_of_pairs)
        scores.append(ratio)
    return scores        