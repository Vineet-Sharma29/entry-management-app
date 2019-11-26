import session from "./session";

export default {
    scheduleMeeting(meeting) {
        return session.post("/meeting/create/", {
            ...meeting
        })
    }
};