class Solution {
public:
void reverse(int i, int j, vector<int>&a){
        while(i<=j){
            int temp = a[i];
            a[i] = a[j];
            a[j] = temp;
            i++;
            j--;
        } 
        return;
    }
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k%n;
        reverse(0 , n-k-1, nums);
        reverse(n-k, n-1, nums);
        reverse(0 , n-1, nums);
    }
};