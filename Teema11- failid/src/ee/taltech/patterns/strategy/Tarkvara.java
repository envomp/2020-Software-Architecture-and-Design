package ee.taltech.patterns.strategy;

import java.util.List;

public class Tarkvara {

	private final OS os;
	private String baaskataloog;

	public Tarkvara(String baaskataloog, OS os) {
		this.baaskataloog = baaskataloog;
		this.os = os;
	}

	public void installeeri() {
		if (!this.os.kataloogSobib(this.baaskataloog)) {
			this.baaskataloog = "varukataloog";
		}

		this.os.valmistaKataloog(this.baaskataloog + "\\bin");
		this.os.installeeriFailid(this.baaskataloog + "\\bin", List.of("proge.exe", "proge.bat"));
		this.os.valmistaKataloog(this.baaskataloog + "\\dat");
		this.os.installeeriFailid(this.baaskataloog + "\\dat", List.of("mudelid.dat", "andmed.dat"));
	}

}
