
| [English](README_EN.md) | 简体中文 |

# [53. 最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)

## 题目描述

<p>给定一个整数数组 <code>nums</code> ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>输出：</strong>6
<strong>解释：</strong>连续子数组 [4,-1,2,1] 的和最大，为 6 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1]
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [0]
<strong>输出：</strong>0
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>nums = [-1]
<strong>输出：</strong>-1
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>nums = [-100000]
<strong>输出：</strong>-100000
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 3 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup> <= nums[i] <= 10<sup>5</sup></code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong>如果你已经实现复杂度为 <code>O(n)</code> 的解法，尝试使用更为精妙的 <strong>分治法</strong> 求解。</p>


## 相关话题

- [数组](https://leetcode-cn.com/tag/array)
- [分治算法](https://leetcode-cn.com/tag/divide-and-conquer)
- [动态规划](https://leetcode-cn.com/tag/dynamic-programming)

## 相似题目

- [买卖股票的最佳时机](../best-time-to-buy-and-sell-stock/README.md)
- [乘积最大子数组](../maximum-product-subarray/README.md)
- [数组的度](../degree-of-an-array/README.md)
- [最长湍流子数组](../longest-turbulent-subarray/README.md)
