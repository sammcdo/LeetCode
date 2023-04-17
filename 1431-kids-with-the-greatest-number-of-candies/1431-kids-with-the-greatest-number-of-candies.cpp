class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> vec;

        vec.resize(candies.size());

        int max = max = *max_element(candies.begin(), candies.end());
        
        for (int i = 0; i < candies.size(); i++) {
            vec[i] = (candies[i]+extraCandies>=max);
        }
        
        return vec;
    }
};