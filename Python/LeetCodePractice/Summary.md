# 算法小课心得
### Day1: 删除有序数组中的重复值
【8480-总结提交】今天第一天打卡，发现自己刷题还是有些惯性思维，先按照自己的思路解题，最后测试没
通过，才发现审题错误～按照老师说的先仔细审题，并且看了大牛的解题方法，再自己用python实现了一遍，
除了本题算法需要用双指针来解，觉得里面提到的引入判断减少数据搬移的优化方法很有用，有效减少了一些
运行时间@晨晨@极客大学
### Day2：旋转数组
【8480-总结提交】对于数组的旋转，自己思考了几分钟，限于空间复杂度为O(1)，对于切片法和翻转法都只是
想到了一半，在实现的过程中由于考虑不周而只通过了测试案例，提交不通过。后来学习了一下大牛们的结题，
这两种方法算是一点就通了，但感觉能3行代码内实现主要还是依赖了python的特性，所以还是老老实实重新啃
了一下环状替换法的思想，并自己手动实现了一遍，理论+实践能促进更好的认知。希望下次解题，自己也能想
出多种方法~
### Day3: 合并两个有序链表
【8480-总结提交】数组的查找效率高于链表，链表的插入和删除效率高于数组，两者各有优劣。在实现链表的
时候，还不是很习惯递归思维，以后还是要多刻意练习这一方面。熟悉了老师说的五毒刷题方法，现在每次刷题
都会去思考多种解法，没有思路的时候也会先去看牛人们的解答，并且切换到国际站看讨论，很多解法是理解了，
但不能保证过几天还记得，所以留下这些记录，争取一个星期后再来刷一次。
### Day4: 合并两个有序数组
【8480-总结提交】数组和链表原理上看上去简单，但链表的指向调整还需要多加练习。今天的数组，虽然知道
需要用双指针法，自己选择的指针也是从前往后，可是在O(1)的空间复杂度条件下一直没能完成。看牛人解答
才知道O(1)的空间复杂度，双指针需要从后往前遍历，还需要多加练习。
### Day5: 栈和队列实现的特性，两数之和
【8480-总结提交】栈和队列的特性，合理使用这些栈和队列的特性，可以很好的降低问题的时间复杂度。但通常
Deque这种双端队列会使用得更多。还是还不太习惯去看这些特殊数据结构的底层代码，以后要多加尝试。
### Day6: 零移动
【8480-总结提交】发现在空间和时间复杂度的限制下，双指针的破题法很受用。
### Day7：循环队列的实现
【8480-总结提交】循环队列的实现，需要我们清楚双端队列的特性，双端可操作，需要头尾指针来记录数据的位置，
且双端队列的大小是固定的。很少写这样比较底层的数据结构代码，感觉很受用，这样对一个数据结构的了解会更加
透彻。
