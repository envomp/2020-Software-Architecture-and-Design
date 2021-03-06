package ee.taltech.patterns.strategy;

import java.util.List;

public class Unix extends OS {

	@Override
	protected boolean kataloogSobib(String kataloog) {
		System.out.println("Kontrollin kataloogi " + kataloog + " sobivust Unixile");
		return kataloog.length() > 2;
	}

	@Override
	protected void valmistaKataloog(String kataloog) {
		System.out.println("Valmistan kataloogi " + kataloog + " Unixile");
	}

	@Override
	protected void installeeriFailid(String kataloog, List<String> failid) {
		failid.forEach(x -> System.out.println("Tekitan Unixis faili " + kataloog + "\\" + x));
	}
}
