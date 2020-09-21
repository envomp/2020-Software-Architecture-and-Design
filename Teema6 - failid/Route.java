import java.util.ArrayList;
import java.util.List;

public class Route {

    private List<Point> points = new ArrayList<>();
    private final Integer max_length;

    public Route(List<Point> points, Integer max_length) {
        this.points = points;
        this.max_length = max_length;
    }

    public Route(Integer max_length) {
        this.max_length = max_length;
    }

    /**
     * @return a new Route with a max size of 10
     **/
    public static Route create_route() {
        return new Route(10);
    }

    /**
     * @return a new Route with a max size
     **/
    public static Route create_route(Integer size) {
        return new Route(size);
    }

    /**
     * Adds a new point to the route into the given index. Increases the route size by 1
     *
     * @throws IllegalArgumentException when index is smaller than 0 or bigger than min(max_length, route_length)
     **/
    public void add_point(double x, double y, int index) {
        if (index < 0 || index > Math.min(max_length, points.size())) {
            throw new IllegalArgumentException("index must be in range [0 and min(max_length, #points)]");
        }

        points.add(index, new Point(x, y));
    }

    /**
     * Removes a point from the route given an index. Decreases the route size by 1
     *
     * @throws IllegalArgumentException when index is smaller than 0 or bigger or equal to min(max_length, route_length)
     **/
    public void remove_point(int index) {
        if (index < 0 || index >= Math.min(max_length, points.size())) {
            throw new IllegalArgumentException("index must be in range [0, min(max_length, #points))");
        }
        points.remove(index);
    }

    /**
     * @return length of the given route. Sum of distances between neighbouring points
     * **/
    public double get_length() {
        double total_length = 0.0;
        for (int i = 0; i < points.size() - 1; i++) {
            total_length += points.get(i).getDistance(points.get(i + 1));
        }
        return total_length;
    }

    public static void main(String[] args) {
        Route route = new Route(3);
        route.add_point(2, 2, 0);
        System.out.println(route.get_length());
        route.add_point(1, 1, 0);
        System.out.println(route.get_length());
        route.add_point(3, 3, 2);
        System.out.println(route.get_length());
        System.out.println(route.points);
    }
}
