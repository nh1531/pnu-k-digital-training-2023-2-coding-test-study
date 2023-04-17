package 백준.Week01_그리디알고리즘;

import java.util.Arrays;
import java.util.Scanner;

public class _2217_로프 {
    /*
    N(1 ≤ N ≤ 100,000)개의 로프가 있다.
     이 로프를 이용하여 이런 저런 물체를 들어올릴 수 있다.
      각각의 로프는 그 굵기나 길이가 다르기 때문에 들 수 있는 물체의 중량이
       서로 다를 수도 있다.

    하지만 여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다.
    k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때,
    각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.

    각 로프들에 대한 정보가 주어졌을 때,
    이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는
    프로그램을 작성하시오. 모든 로프를 사용해야 할 필요는 없으며,
     임의로 몇 개의 로프를 골라서 사용해도 된다.
     */

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        int[] a = new int[num];
        for (int i = 0; i < a.length; i++) {
            a[i] = sc.nextInt();
        }
        Arrays.sort(a);

        int[] sum = new int[num];
        for (int i = 0; i < a.length; i++) {
            sum[i]  = a[i] * (a.length-i);
//            System.out.println(sum[i]);
        }
        Arrays.sort(sum);
        System.out.println(sum[sum.length-1]);
//        System.out.println(a[0] *a.length);



    }


}
