class compare_object:
    def __init__(self):
        self.uni = dict()
        self.uni['str']=0
        self.di = dict()
        self.di['str','str']=0;
        self.tri = dict()
        self.tri['str','str','str']=0


def match_with_pos(pos,ss1,ss2):

    s1=""
    s2=""

    for i in ss1:
        if(i.isalnum() or i=='.' or i==',' or i=='!' or i==' ' or i=='-'):
            s1=s1+i


    for i in ss2:
        if(i.isalnum() or i=='.' or i==',' or i=='!' or i==' ' or i=='-'):
            s2=s2+i


    ob1=compare_object()
    ob2=compare_object()
    
    if(pos+20<len(s1) and len(s2)>=20):
        
        for i in range(20):
            if(s2[i] in ob2.uni):
                ob2.uni[s2[i]]=ob2.uni[s2[i]]+1
            else:
                ob2.uni[s2[i]]=1
            
            if(i<19):
                if((s2[i],s2[i+1]) in ob2.di ):
                    ob2.di[s2[i],s2[i+1]]=ob2.di[s2[i],s2[i+1]]+1
                else:
                    ob2.di[s2[i],s2[i+1]]=1
                
                if(i<18):
                    
                    if((s2[i],s2[i+1],s2[i+2]) in ob2.tri):
                        ob2.tri[s2[i],s2[i+1],s2[i+2]]=ob2.tri[s2[i],s2[i+1],s2[i+2]]+1
                    else:
                        ob2.tri[s2[i],s2[i+1],s2[i+2]]=1
                
        
                
        for xx in range(20):
            i=xx+pos
            if(s1[i] in ob1.uni):
                ob1.uni[s1[i]]=ob1.uni[s1[i]]+1
            else:
                ob1.uni[s1[i]]=1
                
            if(xx<19):
                if((s1[i],s1[i+1]) in ob1.di):
                    ob1.di[s1[i],s1[i+1]]=ob1.di[s1[i],s1[i+1]]+1
                else:
                    ob1.di[s1[i],s1[i+1]]=1
                
                if(xx<18):
                    
                    if((s1[i],s1[i+1],s1[i+2]) in ob1.tri):
                        ob1.tri[s1[i],s1[i+1],s1[i+2]]=ob1.tri[s1[i],s1[i+1],s1[i+2]]+1
                    else:
                        ob1.tri[s1[i],s1[i+1],s1[i+2]]=1
                        
                        
        points=0
        
        keywords_count=0
        for key in ob2.uni:
            if(key in ob1.uni):
                points=points+ob1.uni[key]
                
        
        
        
        for key in ob2.di:
            if(key in ob1.di):
                points=points + 2*ob1.di[key]
                
                
        for key in ob2.tri:
            if(key in ob1.tri):
                points=points + 3*ob1.tri[key]
                
        return points
    
    else:
        return 0
                
def finalresult(s1,s2):
    ans=""
    m1=dict()
    m1['str','str']=0
    m2=dict()
    m2['str','str']=0
    dupletes=set()
    pos1=0
    pos2=0
    while(pos1<len(s1)-10 and pos2<len(s2)-10):
        
        for j in range(10):
            dupletes.add((s1[pos1],s1[pos1+1]))
            if (s1[pos1],s1[pos1+1]) in m1:
                m1[s1[pos1],s1[pos1+1]]=m1[s1[pos1],s1[pos1+1]]+1
            else:
                m1[s1[pos1],s1[pos1+1]]=1
                
            dupletes.add((s2[pos2],s2[pos2+1]))
            if (s2[pos2],s2[pos2+1]) in m2:
                m2[s2[pos2],s2[pos2+1]]=m2[s2[pos2],s2[pos2+1]]+1
            else:
                m2[s2[pos2],s2[pos2+1]]=1
            
            pos1=pos1+1
            pos2=pos2+1
        
        mismatch=0
        for key in dupletes:
            if key not in m1:
                m1[key]=0
            if key not in m2:
                m2[key]=0
            mismatch=mismatch+abs(m1[key]-m2[key])
        if mismatch>3 and 10*mismatch>(pos1+pos2):
            break
    
    return s2[pos2:]
            


def compairing_strings(ss1,ss2):

    s1=""
    s2=""

    for i in ss1:
        if(i.isalnum() or i=='.' or i==',' or i=='!' or i==' ' or i=='-'):
            s1=s1+i


    for i in ss2:
        if(i.isalnum() or i=='.' or i==',' or i=='!' or i==' ' or i=='-'):
            s2=s2+i

    ans=""
    val=1
    pos=-1
    for i in range(len(s1)-20):
        if(match_with_pos(i,s1,s2)>val):
            val=match_with_pos(i,s1,s2)
            pos=i
    
    if(pos<20):
        return ans
    elif (pos!=-1):
        return finalresult(s1[pos:],s2)
    
    return ans



st1 = "Who uses big data? Walmart does! A leader in many industries, Walmart is also a leader when it comes to big data analytics. As the volume of data continues to pile up, Walmart continues to use it to it’s advantage, analyzing each aspect of the store to gain a real-time view of workflow across each store worldwide. In every department of the mega corporation, data analytics impact day to day operations. Over time this impacts key policy decisions, along with profits. From pharmacy efficiency to product assortment and supply chain management, Walmart continues to set the mark with it’s robust collection of data. From pharmacy efficiency to product assortment and supply chain management, Walmart continues to set the mark with it’s robust collection of data. Walmart is bullish on big data — especially when it comes to finding ways to better serve its shoppers. Big data volume continues to grow, but Walmart is using it to the company’s — and its customers’ — advantage. By analyzing the robust information "

st2 = "From pharmacy efficiency to product assortment and supply chain management, Walmart continues to set the mark with it’s robust collection of data. Walmart is bullish on big data — especially when it comes to finding ways to better serve its shoppers. Big data volume continues to grow, but Walmart is using it to the company’s — and its customers’ — advantage. By analyzing the robust information flowing throughout its operations, the discounter has gained a real-time view of workflow across its pharmacy, distribution centers, stores and e-commerce, according to a company blog. By analyzing the robust information flowing throughout its operations, the discounter has gained a real-time view of workflow across its pharmacy, distribution centers, stores and e-commerce, according to a company blog. Big data volume continues to grow, but Walmart is using it to the company’s — and its customers’ — advantage. By analyzing the robust information flowing throughout its operations, the discounter has gained a real-time view of workflow across its pharmacy, distribution centers, stores and e-commerce, according to a company blog. Here are five ways that Walmart is using big data to enhance, optimize and customize the shopping experience: 1.To make Walmart pharmacies more efficient. By analyzing simulations, the discount giant can understand how many prescriptions are filled in a day, and determine the busiest times during each day or month. Big data also helps Walmart schedule associates more efficiently, and reduce the time and labor needed to fill perceptions."
print("--possible output----")
print(compairing_strings(st1,st2))

