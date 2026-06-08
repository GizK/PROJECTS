package apcw.accesscontrol;

import apcw.user.User;
import apcw.resource.Resource;
import apcw.resource.Action;

public class Write {

    public static void perform(User user, Resource resource, AccessControlPolicyEngine engine) {

        AccessDecision decision = engine.evaluateAccess(user, resource, Action.WRITE);

        if (decision.isGranted()) {
            System.out.println("WRITE SUCCESS: " + user.getUserID() + " -> " + resource.getResourceName());
        } else {
            System.out.println("WRITE DENIED: " + decision.getMessage());
        }
    }
}