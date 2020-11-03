package ee.taltech.patterns.strategy;

public class StrategyMain {
	public static void main(String[] args) {
		System.out.println("Demonstreerime WindowsTarkvara");
		Tarkvara windowsTarkvara = new Tarkvara("usr\\kataloog", new Windows());
		windowsTarkvara.installeeri();
		System.out.println("\nDemonstreerime UnixTarkvara");
		ProTarkvara unixTarkvara = new ProTarkvara("usr\\kataloog", new Unix());
		unixTarkvara.installeeri();
	}
}
