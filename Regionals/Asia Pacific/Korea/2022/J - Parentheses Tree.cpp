#include<bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    
    string s;
    
    cin >> s;
    
    long long int sum = 0;
    int cnt = 0;
    
    for(int i = 0; i < s.length(); ++i) {
        if(i == 0) {
            cnt++;
            continue;
        }
        auto cur = s[i];
        if(cur == '(') {
            cnt++;
        }
        else {
            auto prev = s[i-1];
            cnt--;
            if(prev == '(') {
                sum += cnt;
            }
        }
    }
    cout << sum << "\n";
    return 0;
}
