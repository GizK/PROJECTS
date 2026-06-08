package apcw.accesscontrol;

import apcw.user.User;
import apcw.resource.Resource;
import apcw.resource.Action;

public class Read {

    public static void perform(User user, Resource resource, AccessControlPolicyEngine engine) {

        AccessDecision decision = engine.evaluateAccess(user, resource, Action.READ);

        if (decision.isGranted()) {
            System.out.println("READ SUCCESS: " + user.getUserID() + " -> " + resource.getResourceName());
        } else {
            System.out.println("READ DENIED: " + decision.getMessage());
        }
    }
}