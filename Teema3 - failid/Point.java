import java.text.DecimalFormat;

/**
 * any x and y must be bigger than Double.MIN_VALUE and smaller than Double.MAX_VALUE
 **/
public class Point {

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
     * <p>
     * rho = sqrt(x^2 + y^2)
     */
    public double getRho() {
        double rho = Math.sqrt(x * x + y * y);
        return Double.parseDouble(new DecimalFormat("##.00000").format(rho));
    }

    /**
     * Angle to horizontal axis
     * <p>
     * theta = atan2(y, x)
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
     * <p>
     * Vector (x, y) from point (x1, x2) to another point (x2, y2) is defined as
     * (x, y) = (x2 - x1, y2 - y1)
     */
    public Point vectorTo(Point other) {
        return new Point(other.x - x, other.y - y);
    }

    /**
     * Move by dx horizontally, dy vertically
     * <p>
     * Point translation in 2D space is defined as
     * <p>
     * (x, y) = (old x + dx, old y + dy)
     */
    public void translate(double dx, double dy) {
        x += dx;
        y += dy;
    }

    /**
     * Scale by a factor
     * <p>
     * Point scaling by factor of k in 2D space is defined as
     * (x, y) = (old x * k, old y * k)
     */
    public void scale(double factor) {
        x *= factor;
        y *= factor;
    }

    /**
     * Rotate around origin (0, 0) by angle
     * <p>
     * Point rotation around (0, 0) origin is defined as
     * this.theta % (2*pi) = ((old this).theta + angle) % (2*pi)
     */
    public void centre_rotate(double angle) {
        double temp_x = getRho() * Math.cos(getTheta() + angle);
        y = getRho() * Math.sin(getTheta() + angle);
        x = temp_x;
    }

    /**
     * Rotate around p by angle
     * <p>
     * Point rotation around another point (p) is defined as
     * p.vectorTo(this).theta % (2*pi) = (p.vectorTo(old this).theta + angle) % (2*pi)
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
