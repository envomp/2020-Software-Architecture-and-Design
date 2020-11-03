package ee.taltech.patterns.strategy;

import java.util.List;

public abstract class OS {

	protected abstract boolean kataloogSobib(String kataloog);

	protected abstract void valmistaKataloog(String kataloog);

	protected abstract void installeeriFailid(String kataloog, List<String> failid);
}
