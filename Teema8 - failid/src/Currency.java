import java.io.Serializable;
import java.util.Objects;

public class Currency implements Serializable {

    private String code;
    private String name;

    public Currency(String code, String name) {
        this.code = code;
        this.name = name;
    }

    @Override
    public String toString() {
        return String.format("%s(%s)", name, code);
    }

    @Override
    public boolean equals(Object o) {
        return this.getClass() == o.getClass() && this.hashCode() == o.hashCode();
    }


    @Override
    public int hashCode() {
        return Objects.hash(code, name);
    }
}