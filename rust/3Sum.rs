// Runtime: 32ms
// MemoryUsage: 3.9MB

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let len = nums.len();
        
        if len < 3 {
            return Vec::new();
        }

        let mut nums = nums;
        nums.sort();
        let mut i = 0;
        let mut result: Vec<Vec<i32>> = Vec::new();
        let mut previous = nums[0] - 1;
        while i < len - 2 {
            // sorted vector, skip same number
            if nums[i] == previous {
                i += 1;
                continue;
            }
            previous = nums[i];
            
            let mut vec = Solution::two_sum(&nums[(i + 1)..len], 0 - nums[i]);
            
            for t in vec.iter() {
                result.push(vec![nums[i], t.0, t.1]);
            }
            i += 1;
        }
        return result
    }

    
    fn two_sum(nums: &[i32], sum: i32) -> Vec<(i32, i32)> {
        let (mut i, mut j) = (0, nums.len() - 1);
        
        let mut result  = Vec::new();
        
        while i < j {
            if nums[i] + nums[j] > sum {
                j -= 1;
            } else if nums[i] + nums[j] < sum {
                i += 1;
            } else {
                result.push((nums[i], nums[j]));
                while(i < nums.len()-1) {
                    i += 1;
                    if (nums[i-1] == nums[i]) {
                        // do nothing
                    } else {
                        break;
                    }
                }
                while(j<0) {
                    j -= 1;
                    if (nums[j+1] == nums[j]) {
                        // do nothing
                    } else {
                        break;
                    }
                }
            }
        }
        
        return result
        
    }
