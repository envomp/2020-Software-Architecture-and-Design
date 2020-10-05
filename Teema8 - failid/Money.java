import java.security.InvalidParameterException;

public class Money {

    private Double balance;
    private Currency currency;

    public Money(Double balance, Currency currency) {
        this.balance = balance;
        this.currency = currency;
    }

    public Double decrease(Double amount) {
        this.balance -= amount;
        return this.balance;
    }

    public Double increase(Double amount) {
        this.balance += amount;
        return this.balance;
    }

    public Double transform(Currency newCurrency) {
        Double rate = ExchangeRate.getRate(currency, newCurrency);
        if (rate == null) {
            throw new InvalidParameterException("Exchange rate table does not contain such transaction");
        }

        this.currency = newCurrency;
        this.balance = (double) (Math.round(this.balance * rate * 100) / 100);
        return balance;
    }

    public Double getBalance() {
        return balance;
    }
}