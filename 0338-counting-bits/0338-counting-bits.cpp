#include <cmath>

class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> dp;
        
        dp.resize(1);
        dp[0] = 0;
        
        if (n == 0) {
            return dp;
        }
        if (n == 1) {
            dp.resize(2);
            dp[1] = 1;
        }
        
        dp.resize(n+1);
        
        dp[0] = 0;
        dp[1] = 1;
        int power = 1;
        
        for (int i = 2; i < n+1; i++) {
            if (i == pow(2, power+1)) {
                power++;
            }
            dp[i] = 1 + dp[i - pow(2, power)];
        }
        
        return dp;
    }
};