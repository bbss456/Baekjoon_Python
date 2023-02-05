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


>[타켓 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165) 
###
```
import java.util.*;

public class programmerce {
    public int solution(int[][] maps) {
        Queue<Integer> que = new LinkedList<>();

        int heightMax = maps.length;
        int widthMax = maps[0].length;
        Boolean[][] visitBoolean = new Boolean[heightMax][widthMax];

        int i=0;
        int j=0;
        for (i=0; i < heightMax; i++) {
            for (j=0; j < widthMax; j++) {
                visitBoolean[i][j] = false;
            }
        }



        que.offer(0);
        visitBoolean[0][0] = true;
        int distanceCost = 0;
        int width = 0;
        int h=0;

        while (!que.isEmpty()) {
            h = que.poll();
            if (h <= heightMax-1 && maps[h+1][width]==1 && !visitBoolean[h+1][width]) {
                que.offer(h+1);
                distanceCost += 1;
                h += 1;
                visitBoolean[h][width] = true;
            }
            else if (h <=heightMax-1 && maps[h+1][width] != 1) {
                if (maps[h][width + 1] == 1 && visitBoolean[h][width + 1] == false) {
                    width += 1;
                    que.offer(h-1);

                } else if (h > 0 && visitBoolean[h - 1][width] == false && maps[h - 1][width] == 1) {
                    que.offer(h-2);
                } else if (width > 0 && visitBoolean[h][width - 1] == false && maps[h][width - 1] == 1) {
                    width -= 1;
                    visitBoolean[h - 1][width] = true;
                    distanceCost += 1;
                    que.offer(h);
                }
            }
        }
        System.out.println(distanceCost);
        int answer = 0;
        return answer;
    }

    public static void main(String args[]) {
        int[][] s = 	{{1, 0, 1, 1, 1}, {1, 0, 1, 0, 1}, {1, 0, 1, 1, 1}, {1, 1, 1, 0, 1}, {0, 0, 0, 0, 1}};
        programmerce solution =new programmerce();
        solution.solution(s);
    }
}
```