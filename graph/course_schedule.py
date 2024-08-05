"""
https://leetcode.com/problems/course-schedule/
https://www.youtube.com/watch?v=EUDwWbvtB_Q&t=1s

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] 
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0,
and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""


def can_finish(
    num_courses: int,
    prerequisites: list[list[int]],
) -> bool:
    from collections import deque

    adj = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    ans = []

    for pair in prerequisites:
        course = pair[0]
        prerequisite = pair[1]
        adj[prerequisite].append(course)
        indegree[course] += 1

    queue = deque()
    for i in range(num_courses):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()
        ans.append(current)

        for next_course in adj[current]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)

    return len(ans) == num_courses


if __name__ == '__main__':
    assert can_finish(num_courses=2, prerequisites=[[1, 0]])
    assert can_finish(num_courses=2, prerequisites=[[1, 0], [0, 1]]) is False
    assert can_finish(num_courses=5, prerequisites=[[1, 4], [2, 4], [3, 1], [3, 2]])
