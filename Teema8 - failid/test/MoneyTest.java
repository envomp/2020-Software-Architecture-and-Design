import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class MoneyTest {

    private Money money;

    @BeforeEach
    void beforeEach() {
        money = new Money(100.0, new Currency("BAN", "banana"));
    }

    @Test
    void decrease() {
        money.decrease(10.0);
        assertEquals(90.0, money.getBalance());
    }

    @Test
    void increase() {
        money.increase(10.0);
        assertEquals(110.0, money.getBalance());
    }

    @Test
    void transform() {
        Currency from = new Currency("BAN", "banana");
        Currency to = new Currency("TOM", "tomato");
        ExchangeRate.addRate(from, to, 10.0);
        assertEquals(1000.0, money.transform(to));
        assertEquals(100.0, money.transform(from));
    }
}