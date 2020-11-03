package ee.taltech.patterns.strategy;

import java.util.List;

/**
 * Ka tarkvara abstraktsioon võib varieeruda. Tekib silla (Bridge) muster.
 */
public class ProTarkvara extends Tarkvara {
	private final String baaskataloog;
	private final OS os;

	public ProTarkvara(String baaskataloog, OS os) {
		super(baaskataloog, os);
		this.baaskataloog = baaskataloog;
		this.os = os;
	}

	@Override
	public void installeeri() {
		super.installeeri();
		System.out.println("Paigaldame profilaiendused");
		this.os.valmistaKataloog(this.baaskataloog + "\\ext");
		this.os.installeeriFailid(this.baaskataloog + "\\ext", List.of("laiendus1.egg", "laiendus2.egg"));
	}
}
