#include<bits/stdc++.h>

using namespace std;


bool check(string temp)
{
    stack<char> s;
    
    for(int i=0; i< temp.size(); ++i)
    {
        if(temp[i] == '(')
            s.push(temp[i]);
        
        else if (temp[i] == ')')
        {
            if(s.empty())
                return false;
            
            s.pop();
        }
    }
    
    if(s.empty())
        return true;
    else
        return false;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    
    while(n--)
    {
        string temp;
        
        cin >> temp;
        
        if (check(temp))
            cout << "YES";
        else
            cout << "NO";
        
        cout << "\n";
    }
    
    return 0;
}
