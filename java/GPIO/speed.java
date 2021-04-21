import java.util.concurrent.TimeUnit;

public class speed {
    
    public static void main(String[] args) throws InterruptedException {

        {
            //long sum = 0;
            int N = 1000;
            long t1 = System.currentTimeMillis ();
            for (int i = 0; i < N; i++) {
                TimeUnit.MILLISECONDS.sleep(2);
                //sum += System.currentTimeMillis ();
            }
            long t2 = System.currentTimeMillis ();
            System.out.println ("Elapsed time = " + (t2 - t1) +
                "; or " + ((float)(t2 - t1) / (float)N) + " ms / iter");
        }

    }

}
