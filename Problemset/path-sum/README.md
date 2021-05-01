
| [English](README_EN.md) | 简体中文 |

# [112. 路径总和](https://leetcode-cn.com/problems/path-sum/)

## 题目描述

<p>给你二叉树的根节点 <code>root</code> 和一个表示目标和的整数 <code>targetSum</code> ，判断该树中是否存在 <strong>根节点到叶子节点</strong> 的路径，这条路径上所有节点值相加等于目标和 <code>targetSum</code> 。</p>

<p><strong>叶子节点</strong> 是指没有子节点的节点。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg" style="width: 500px; height: 356px;" />
<pre>
<strong>输入：</strong>root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg" />
<pre>
<strong>输入：</strong>root = [1,2,3], targetSum = 5
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = [1,2], targetSum = 0
<strong>输出：</strong>false
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点的数目在范围 <code>[0, 5000]</code> 内</li>
	<li><code>-1000 <= Node.val <= 1000</code></li>
	<li><code>-1000 <= targetSum <= 1000</code></li>
</ul>


## 相关话题

- [树](https://leetcode-cn.com/tag/tree)
- [深度优先搜索](https://leetcode-cn.com/tag/depth-first-search)

## 相似题目

- [路径总和 II](../path-sum-ii/README.md)
- [二叉树中的最大路径和](../binary-tree-maximum-path-sum/README.md)
- [求根节点到叶节点数字之和](../sum-root-to-leaf-numbers/README.md)
- [路径总和 III](../path-sum-iii/README.md)
- [路径总和 IV](../path-sum-iv/README.md)
