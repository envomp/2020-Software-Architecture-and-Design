import java.io.Serializable;
import java.util.Objects;

public class Exchange implements Serializable {

    private Currency from;
    private Currency to;

    public Exchange(Currency from, Currency to) {
        this.from = from;
        this.to = to;
    }

    public Currency getFrom() {
        return from;
    }

    public Currency getTo() {
        return to;
    }

    @Override
    public boolean equals(Object o) {
        return this.getClass() == o.getClass() && this.hashCode() == o.hashCode();
    }

    @Override
    public int hashCode() {
        return Objects.hash(from, to);
    }
}