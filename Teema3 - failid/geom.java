import java.text.DecimalFormat;

class Point {

    private double x;
    private double y;

    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }

    /**
     * Abscissa
     */
    public double getX() {
        return Double.parseDouble(new DecimalFormat("##.00000").format(x));
    }

    /**
     * Ordinate
     */
    public double getY() {
        return Double.parseDouble(new DecimalFormat("##.00000").format(y));
    }

    /**
     * Distance to origin (0, 0)
     */
    public double getRho() {
        double rho = Math.sqrt(x * x + y * y);
        return Double.parseDouble(new DecimalFormat("##.00000").format(rho));
    }

    /**
     * Angle to horizontal axis
     */
    public double getTheta() {
        double theta = Math.atan2(y, x);
        return Double.parseDouble(new DecimalFormat("##.00000").format(theta));
    }

    /**
     * Distance to other
     */
    public double getDistance(Point other) {
        return vectorTo(other).getRho();
    }

    /**
     * Point representing the vector from self to other Point
     */
    public Point vectorTo(Point other) {
        return new Point(other.x - x, other.y - y);
    }

    /**
     * Move by dx horizontally, dy vertically
     */
    public void translate(double dx, double dy) {
        x += dx;
        y += dy;
    }

    /**
     * Scale by a factor
     */
    public void scale(double factor) {
        x *= factor;
        y *= factor;
    }

    /**
     * Rotate around origin (0, 0) by angle
     */
    public void centre_rotate(double angle) {
        double temp_x = getRho() * Math.cos(getTheta() + angle);
        y = getRho() * Math.sin(getTheta() + angle);
        x = temp_x;
    }

    /**
     * Rotate around p by angle
     */
    public void rotate(Point other, double angle) {
        translate(-other.getX(), -other.getY());
        centre_rotate(angle);
        translate(other.getX(), other.getY());
    }

    @Override
    public String toString() {
        return String.format("x: %s\ny: %s\nrho: %s\ntheta: %s", getX(), getY(), getRho(), getTheta());
    }
}

class Main {
    public static void main(String[] args) {
        // a
        Point first_point = new Point(10, 20);
        Point second_point = new Point(-20, 60);
        double distance = first_point.vectorTo(second_point).getRho();
        System.out.println(distance); // 50.0

        // b
        Point point = new Point(15, 0);
        point.centre_rotate(3);  // rotate by 3 radians
        System.out.println(point);
        // x: -14.84989
        // y: 2.1168
        // rho: 15.0
        // theta: 3.0
    }
}