import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class RouteTest {

    @Test
    void create_route() {
        assertEquals(0, new Route(10).get_length());
    }

    @Test
    void testCreate_route() {
        assertEquals(0, Route.create_route().get_length());
        assertEquals(0, Route.create_route(11).get_length());
    }

    @Test
    void add_point() {
        Route route = Route.create_route();
        route.add_point(0, 1, 0);
        route.add_point(0, 2, 0);
        assertEquals(1, route.get_length());
    }

    @Test
    void remove_point() {
        Route route = Route.create_route();
        route.add_point(0, 1, 0);
        route.add_point(0, 1, 0);
        route.remove_point(0);

        assertEquals(0, route.get_length());
    }

    @Test
    void get_length() {
        Route route = Route.create_route();
        route.add_point(0, 1, 0);
        route.add_point(0, 2, 0);
        route.add_point(1, 2, 0);
        assertEquals(2, route.get_length());
    }
}