package ee.taltech.patterns.template;

import java.util.List;

public abstract class Tarkvara {

	private String baaskataloog;

	public Tarkvara(String baaskataloog) {
		this.baaskataloog = baaskataloog;
	}

	public void installeeri() {

		if (!kataloogSobib(this.baaskataloog)) {
			this.baaskataloog = "varukataloog";
		}

		this.valmistaKataloog(this.baaskataloog + "\\bin");
		this.installeeriFailid(this.baaskataloog + "\\bin", List.of("proge.exe", "proge.bat"));
		this.valmistaKataloog(this.baaskataloog + "\\dat");
		this.installeeriFailid(this.baaskataloog + "\\dat", List.of("mudelid.dat", "andmed.dat"));

	}

	protected abstract boolean kataloogSobib(String kataloog);

	protected abstract void valmistaKataloog(String kataloog);

	protected abstract void installeeriFailid(String kataloog, List<String> failid);
}