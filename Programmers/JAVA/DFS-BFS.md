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


>[게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) 
###
```
import java.util.LinkedList;
import java.util.Queue;
import java.awt.*;

class Solution {
      public int solution(int[][] maps) {
        int X = maps[0].length;
        int Y = maps.length;
        boolean[][] visited = new boolean[Y][X];
        Queue<Point> q = new LinkedList<Point>();
        int x = 0;
        int y = 0;
        int size = 0;
        int distanceCost = 0;
        Point p = new Point();
        q.add(new Point(y,x));
        while(q.isEmpty()==false) {
            size = q.size();
            distanceCost++;
            for(int i=0;i<size;i++)
            {
                p = q.peek();
                x = p.y;
                y = p.x;
                q.remove();
                if(visited[y][x]==true)
                    continue;
                maps[y][x] = 0;
                visited[y][x] = true;
                if(x==X-1 && y==Y-1) {
                    return distanceCost;
                }
                if(x-1 > -1 && maps[y][x-1]==1) {
                    q.add(new Point(y,x-1));
                }
                if(x+1 < X && maps[y][x+1]==1) {
                    q.add(new Point(y,x+1));
                }
                if(y-1 > -1 && maps[y-1][x]==1) {
                    q.add(new Point(y-1,x));
                }
                if(y+1 < Y && maps[y+1][x]==1) {
                    q.add(new Point(y+1,x));
                }
            }
        }
        return -1;
    }
}
```