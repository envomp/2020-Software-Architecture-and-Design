package ee.taltech.patterns.template;

import java.util.List;

public class WindowsTarkvara extends Tarkvara {

	public WindowsTarkvara(String baaskataloog) {
		super(baaskataloog);
	}

	@Override
	protected boolean kataloogSobib(String kataloog) {
		System.out.println("Kontrollin kataloogi " + kataloog + " sobivust Windowsile");
		return kataloog.length() < 8;
	}

	@Override
	protected void valmistaKataloog(String kataloog) {
		System.out.println("Valmistan kataloogi " + kataloog + " Windowsile");
	}

	@Override
	protected void installeeriFailid(String kataloog, List<String> failid) {
		failid.forEach(x -> System.out.println("Tekitan Windowsis faili " + kataloog + "\\" + x));
	}
}
