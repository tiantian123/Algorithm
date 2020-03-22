#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minIncrementForUnique1(vector<int>& A) {
        int level = -1;
        int res = 0;
        sort(A.begin(), A.end());
        for (int a: A) {
            if (level < a) {
                level = a;
            }else
            {
                res += level - a + 1;
                level += 1;
            }
            
        }
        return res;
    }

    int minIncrementForUnique2(vector<int>& A) {
        sort(A.begin(), A.end());
        int res = 0, need = 0;
        for (int a: A) {
            res += max(need - a, 0);
            need = max(a, need) + 1;
        }
        return res;
    }     
};