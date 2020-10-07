import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ExchangeRateTest {

	@Test
	void addAndGetRate() {
		Currency from = new Currency("BAN", "banana");
		Currency to = new Currency("TOM", "tomato");
		ExchangeRate.addRate(from, to, 10.0);
		assertEquals(10.0, ExchangeRate.getRate(from, to));
		assertEquals(0.1, ExchangeRate.getRate(to, from));
	}

	@Test
	void generateTable() {
		Currency cur1 = new Currency("BAN", "banana");
		Currency cur2 = new Currency("TOM", "tomato");
		Currency cur3 = new Currency("ANA", "ananas");
		Currency cur4 = new Currency("LET", "lettuce");
		ExchangeRate.addRate(cur1, cur2, 10.0);
		ExchangeRate.addRate(cur2, cur3, 4.0);
		ExchangeRate.addRate(cur4, cur3, 16.0);
		ExchangeRate.printTable();
	}
}