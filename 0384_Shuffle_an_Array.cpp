#include <vector>
#include <random>
#include <chrono>
#include <iostream>
class Solution {
public:
    std::vector<int> nums{};
    std::vector<int> indexes;
    std::chrono::high_resolution_clock::time_point beginning = std::chrono::high_resolution_clock::now();
    Solution(std::vector<int> &_nums) {
        nums.swap(_nums);
        for (int i = 0; i < nums.size(); ++i) {
            indexes.push_back(i);
        }
    }
    std::vector<int> reset() {
        return nums;
    }

    std::vector<int> shuffle() {
        std::vector<int> res;
        for (int i = 0; i < nums.size(); ++i) {
            auto d = std::chrono::high_resolution_clock::now() - beginning;
            unsigned seed = d.count();
            std::mt19937 gen(seed);
            std::uniform_int_distribution<unsigned> u(0, nums.size() - i - 1);
            auto index = u(gen);
            res.push_back(nums[indexes[index]]);
            int t = indexes[index];
            indexes[index] = indexes[nums.size() - i - 1];
            indexes[nums.size() - i - 1] = t;
        }
        return res;
    }
};

int main() {
    std::vector<int> v{1, 2, 3, 4, 5};
    Solution s(v);
    for (int i = 10; i > 0; --i) {
        auto v1 = s.shuffle();
        for (auto &&n : v1) {
            std::cout << n;
        }
        std::cout << "\n";
    }
}
