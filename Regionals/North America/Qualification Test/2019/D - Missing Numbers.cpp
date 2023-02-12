#include<bits/stdc++.h>

using namespace std;

char used[201];

int main()
{
    int n, end;
    cin >> n;
    end = n;
    
    for(int i=0; i<n; i++)
    {
        int data;
        cin>> data;
        used[data] = true;
        
        if(i == n-1)
            end = data;
    }
    
    bool flag = true;
    
    for(int i=1; i< end + 1; i++)
    {
        if(not used[i])
        {
            flag = false;
            cout << i <<"\n";
        }
    }
    
    if(flag)
        cout << "good job";
}
