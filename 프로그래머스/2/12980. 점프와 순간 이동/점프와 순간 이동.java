import java.util.*;

public class Solution {
    public int solution(int n) {
        int ans = 0; //점프 횟수
        while(n!=0){
            //2의 거듭제곱인경우는, ans가 항상 1 -> 2로 나누어 내려가면서 계속 확인하기
            if(n%2==0){
                n=n/2;
            }
            //2의 거듭제곱이 아닌 경우, 점프가 1회 이상 필요함
            //점프 +1, 거리 n -1
            else{
                n-=1;
                ans+=1;
            }
        }
        return ans;
    }
}
//1 -> 1(점)
//2 -> 1(점,순)
//3 -> 2(점,순,점)
//4 -> 1(점,순,순)
//5 -> 2(점,순,순,점)
//6 -> 2(점,순,점,순)
//7 -> 3(점,순,점,순,점)
//8 -> 1(점,순,순,순)