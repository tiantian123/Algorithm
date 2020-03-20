#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        int i = 0;
        for (int j = 1; j < nums.size(); j++) {
            if (nums[i] != nums[j]) {
                i += 1;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }
};

int main()
{
    Solution Arr;
    vector<int> nums = {1, 1, 2};
    int k = Arr.removeDuplicates(nums);
    cout << k << endl;
    for (int i = 0; i< k; i++) {
        cout << nums[i] << ",";
    }
    cout << endl;
}

