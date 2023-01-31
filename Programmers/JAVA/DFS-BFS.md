# DFS/BFS
>[타켓 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165) 
###
```
class Solution {
    int answer =0;

    public int solution(int[] numbers, int target) {
        int result = 0;
        dfsrecursion(numbers, numbers[0], 0, target,0);
        dfsrecursion(numbers, -1 * numbers[0], 0, target, 0);

        return answer;
    }

    public void dfsrecursion(int[] numbers, int sum, int depth, int target ,int aa) {

        if(depth == numbers.length - 1) {
            if(sum == target) {
                answer++;
            }
            return;
        }

        dfsrecursion(numbers, sum + numbers[depth + 1], depth + 1, target,  numbers[depth + 1]);
        dfsrecursion(numbers, sum - numbers[depth + 1], depth + 1, target, -numbers[depth + 1]);
    }
}
```
