import java.util.HashMap;

public class ExchangeRate {

    private static HashMap<Exchange, Double> rateTable = new HashMap<>();

    public static void addRate(Currency from, Currency to, Double rate) {
        rateTable.put(new Exchange(from, to), rate);
        rateTable.put(new Exchange(to, from), 1 / rate);
    }

    public static Double getRate(Currency from, Currency to) {
        return rateTable.get(new Exchange(from, to));
    }

    public static void printTable() {
        StringBuilder table = new StringBuilder().append("<table><tr><th>From</th><th>To</th><th>Rate</th></tr>");

        for (Exchange exchange : rateTable.keySet()) {
            table
                    .append("<tr><td>")
                    .append(exchange.getFrom())
                    .append("</td><td>")
                    .append(exchange.getTo())
                    .append("</td><td>")
                    .append(rateTable.get(exchange))
                    .append("</td></tr>");
        }

        table.append("</table>");
        System.out.println(table.toString());
    }
}
