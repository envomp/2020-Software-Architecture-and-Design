import java.text.DecimalFormat;

public class Main {
    public static void main(String[] args) {
        // a
        Point first_point = new Point(10, 20);
        Point second_point = new Point(-20, 60);
        double distance = first_point.vectorTo(second_point).getRho();
        System.out.println(distance); // 50.0

        // b
        Point point = new Point(15, 0);
        point.centre_rotate(3.14 / 3);  // rotate by 3 radians
        System.out.println(point);
        // x: -14.84989
        // y: 2.1168
        // rho: 15.0
        // theta: 3.0
    }
}