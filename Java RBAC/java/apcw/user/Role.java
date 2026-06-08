//implemented: roles, levels, descriptions and getters
package apcw.user;

//defining the role enum to define a set of named constants
public enum Role {
	
	// the roles and its levels to use for access and the description
	STUDENT(1, "Student"),
	STAFF(2, "Staff"), 
	ADMIN(3, "Admin");
	
	private final int Level;
	private final String Desc;
	
	//initiating the roles
	Role(int Level, String Desc) {
		this.Level = Level;
		this.Desc = Desc;
	}
	
	//to display the level and the description of the user
	public int getLevel() {
		return Level;
	}
	public String getDesc() {
		return Desc;
	}
}
