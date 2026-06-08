//implemented: user class, fields, constructors and getters
package apcw.user;

//defining the user class
public class User {
	
	// these are the fields/ attributes
	private final String UserID; 
	private final Role Role; // final is used for constants, eg the role of a user is never going to change 
	
	// these are the constructors to initiate the object
	public User(String UserID, Role Role) {
		this.UserID = UserID;
		this.Role = Role;
	}
	
	//these are the methods to display the userID and the role of the user
	public String getUserID() {
		return UserID;
	}
	public Role getRole() {
		return Role;
	}
	public class UserFactory {
	    private static int userCount = 1;

	    // Static factory method
	    public static User createUser(Role role) {
	        String id = "U" + userCount++;
	        return new User(id, role);
	    }
	}
}