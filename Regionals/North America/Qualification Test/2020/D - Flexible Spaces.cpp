#include<bits/stdc++.h>

using namespace std;

bool used[101];

int main()
{
    ios_base::sync_with_stdio(0), cin.tie(0);
    
    int w, p;
    
    cin >> w >> p;
    
    int partition[w+1];
    
    partition[0] = 0;
    for(int i = 1; i < p + 1; ++i) cin >> partition[i];
    partition[p+1] = w;
    
    for(int i=0; i<p+2; ++i)
    {
        for(int j= i + 1; j < p + 2; ++j)
        {
            int length = partition[j] - partition[i];
            used[length] = true;
        }
    }
    
    for(int i = 1; i <= w; ++i)
    {
        if(used[i]) cout <<i<<" ";
    }

    return 0;
}
