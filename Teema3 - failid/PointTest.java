import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PointTest {

    private Point point1;
    private Point point2;

    @BeforeEach
    void setUp() {
        point1 = new Point(10, -10);
        point2 = new Point(-20, 10);
    }

    @Test
    void getX() {
        assertEquals(10.0, point1.getX());
    }

    @Test
    void getY() {
        assertEquals(-10.0, point1.getY());
    }

    @Test
    void getRho() {
        assertEquals(14.14214, point1.getRho());
    }

    @Test
    void getTheta() {
        assertEquals(-0.7854, point1.getTheta());
    }

    @Test
    void getDistance() {
        assertEquals(36.05551, point1.getDistance(point2));
    }

    @Test
    void vectorTo() {
        assertEquals(-30.0, point1.vectorTo(point2).getX());
        assertEquals(20.0, point1.vectorTo(point2).getY());
    }

    @Test
    void translate() {
        point1.translate(10, 10);
        assertEquals(20.0, point1.getX());
        assertEquals(0.0, point1.getY());
    }

    @Test
    void scale() {
        point1.scale(10);
        assertEquals(100.0, point1.getX());
        assertEquals(-100.0, point1.getY());
    }

    @Test
    void centre_rotate() {
        point1.centre_rotate(10);
        assertEquals(-13.83093, point1.getX());
        assertEquals(2.95053, point1.getY());
    }

    @Test
    void rotate() {
        point1.rotate(point2, 10);
        assertEquals(-56.05257, point1.getX());
        assertEquals(10.4607, point1.getY());
    }

    @Test
    void testToString() {
        assertEquals(
                "x: 10.0\n" +
                        "y: -10.0\n" +
                        "rho: 14.14214\n" +
                        "theta: -0.7854",
                point1.toString()
        );
    }
}