package ee.taltech.patterns.template;

public class TemplateMain {
	public static void main(String[] args) {
		System.out.println("Demonstreerime WindowsTarkvara");
		WindowsTarkvara windowsTarkvara = new WindowsTarkvara("usr\\kataloog");
		windowsTarkvara.installeeri();
		System.out.println("\nDemonstreerime UnixTarkvara");
		UnixTarkvara unixTarkvara = new UnixTarkvara("usr\\kataloog");
		unixTarkvara.installeeri();
	}
}
