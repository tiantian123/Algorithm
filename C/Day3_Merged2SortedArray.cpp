#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
void merge2SortedArray(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int p1 = m - 1;
    int p2 = n - 1;
    int q = m + n - 1;
    while (p1 >= 0 && p2 >= 0) {
        if (nums1[p1] > nums2[p2]) {
            nums1[q] = nums1[p1];
            p1 --;
        }else {
            nums1[q] = nums2[p2];
            //cout << nums1[q] << " ";
            p2 --;
        }
        q --;
    }
    //cout << endl;
    for (int i=0; i<=p2; i++){
        nums1[i] = nums2[i];
    }
    
}
};

int main()
{
    Solution So;
    vector<int> nums1 = {1,2,3,0,0,0};
    vector<int> nums2 = {2,5,6};
    int m = 3;
    int n = 3;
    So.merge2SortedArray(nums1, m, nums2, n);
    for (int i=0; i<m+n; i++) {
        cout << nums1[i] << ",";
    }
    cout << endl;
}