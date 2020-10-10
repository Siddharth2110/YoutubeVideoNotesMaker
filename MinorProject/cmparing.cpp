#include<bits/stdc++.h>
using namespace std;
string compairing_strings(string s1,string s2)
{
    string ans="";
    if(abs((int)s1.length()-(int)s2.length())>5 and s2.size()>5)
    {
        map<pair<char,char>,int> m1,m2;
        set<pair<char,char> > dupletes;
        int pos1=0,pos2=0;
        while(pos1<s1.length()-10 and pos2<s2.length()-10)
        {
            for(int j=0;j<10;j++)
            {
                dupletes.insert(make_pair(s1[pos1],s1[pos1+1]));
                m1[make_pair(s1[pos1],s1[pos1+1])]++;
                pos1++;
                dupletes.insert(make_pair(s2[pos2],s2[pos2+1]));
                m2[make_pair(s2[pos2],s2[pos2+1])]++;
                pos2++;
            }
            double mismatch=0;
            for(auto i:dupletes)
            {
                mismatch+=abs(m1[i]-m2[i]);
            }
            if(mismatch>3 and 10*mismatch>(pos2+pos1))
            {
                break;
            }
        }
        for(int i=pos2;i<s2.length();i++)
        {
            ans+=s2[i];
        }
    }
    return ans;
}
int main()
{
    string str1,str2;
    getline(cin,str1);
    cout<<"----------------\n";
    getline(cin,str2);
    cout<<"--------------\n";
    cout<<compairing_strings(str1,str2);
    return 0;
}
